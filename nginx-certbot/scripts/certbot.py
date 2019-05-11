

from sh import cp, ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php, chmod, mv
from sh.contrib import git
import sh, contextlib, os
from config import CERTBOT_BASE_DIR, CERTBOT_CONF_DIR, CERTBOT_WWW_DIR, CERTBOT_NGINX_DIR
import sys

RSA_KEY_SIZE        = 4096
DOCKER_COMPOSE_FILE = CERTBOT_BASE_DIR + '/docker-compose.yml'

def logi(msg):
    print( "[info] => " + msg )
    
def _init_certbot_env():
    logi("Creating certbot directories ...")
    if not os.path.isdir( CERTBOT_CONF_DIR ):
        mkdir("-p", CERTBOT_CONF_DIR )

    if not os.path.isdir( CERTBOT_WWW_DIR ):
        mkdir("-p", CERTBOT_WWW_DIR )

    if not os.path.isdir( CERTBOT_NGINX_DIR ):
        mkdir("-p", CERTBOT_NGINX_DIR )

    logi("Downloading recommended TLS parameters ...")
    SSL_NGINX_URL  = "https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf"
    SSL_NGINX_FILE = CERTBOT_CONF_DIR + 'options-ssl-nginx.conf'
    if not os.path.exists( SSL_NGINX_FILE ):
        wget(SSL_NGINX_URL, "-O", SSL_NGINX_FILE)

    DH_PARAMS_URL  = "https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem"
    DH_PARAMS_FILE = CERTBOT_CONF_DIR + 'ssl-dhparams.pem'
    if not os.path.exists( DH_PARAMS_FILE ):
        wget(DH_PARAMS_URL, "-O", DH_PARAMS_FILE)

    logi("Copying docker file to  ...")
    cp("-rf", 'templates/docker-compose.yml', CERTBOT_BASE_DIR + '/docker-compose.yml')



def _create_dummy_certificate(domains):
    logi("Creating dummy certificate for {} ...".format( domains ))
    base_domain = domains[0]

    CERTBOT_DOMAIN_DIR = CERTBOT_CONF_DIR + '/live/' + base_domain
    if not os.path.isdir( CERTBOT_DOMAIN_DIR ):
        mkdir("-p", CERTBOT_DOMAIN_DIR )

    path    = "/etc/letsencrypt/live/" + base_domain
    command = "openssl req -x509 -nodes -newkey rsa:1024 -days 1 -keyout '{}/privkey.pem' -out '{}/fullchain.pem' -subj '/CN=localhost'".format(path, path)
    sh.docker_compose("-f", DOCKER_COMPOSE_FILE, "run", "--rm", "--entrypoint", command ,'certbot')


def _deleting_dummy_certificate(domains):
    logi("Deleting dummy certificate for {} ...".format( domains ))
    base_domain = domains[0]
    command = "rm -Rf /etc/letsencrypt/live/{} && rm -Rf /etc/letsencrypt/archive/{} && rm -Rf /etc/letsencrypt/renewal/{}.conf".format(base_domain, base_domain, base_domain)
    sh.docker_compose("-f", DOCKER_COMPOSE_FILE, "run", "--rm", "--entrypoint", command, "certbot")


def _request_letsencrypt_certificate(domains, email, staging):
    logi( "Requesting Let's Encrypt certificate for {} ...".format( domains ) )
    #Join $domains to -d args
    domain_args = '-d '+','.join(domains)

    # Select appropriate email arg
    if email in "":
        email_arg = "--register-unsafely-without-email"
    else:
        email_arg = "--email " + email

    # Enable staging mode if needed
    if staging != 0:
        staging_arg="--staging"
    else:
        staging_arg = ""

    command = "certbot certonly --webroot -w /var/www/certbot {} {} {} --rsa-key-size {} --agree-tos --force-renewal".format(staging_arg, email_arg, domain_args, RSA_KEY_SIZE)
    sh.docker_compose("-f", DOCKER_COMPOSE_FILE, "run", "--rm", "--entrypoint", command, "certbot")

    logi( "Reloading nginx ..." )
    sh.docker_compose("-f", DOCKER_COMPOSE_FILE, "exec", "nginx", "nginx", "-s", "reload")

def request_certificate(domains, email, staging):
    _init_certbot_env()
    _create_dummy_certificate(domains)

    logi("Starting nginx ...")
    sh.docker_compose("-f", DOCKER_COMPOSE_FILE, "up", "--force-recreate", "-d","nginx")

    _deleting_dummy_certificate(domains)
    _request_letsencrypt_certificate(domains, email, staging)



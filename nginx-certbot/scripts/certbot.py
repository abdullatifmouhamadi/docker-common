

from sh import cp, ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php, chmod, mv
from sh.contrib import git
import sh, contextlib, os
from config import CERTBOT_BASE_DIR, CERTBOT_CONF_DIR, CERTBOT_WWW_DIR, CERTBOT_NGINX_DIR
import sys

def logi(msg):
    print( echo("[info] => " + msg) )
    
def init_certbot_env():
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



def create_dummy_certificate(domains):
    logi("Creating dummy certificate for domains ...")
    base_domain = domains[0]

    CERTBOT_DOMAIN_DIR = CERTBOT_CONF_DIR + '/live/' + base_domain
    if not os.path.isdir( CERTBOT_DOMAIN_DIR ):
        mkdir("-p", CERTBOT_DOMAIN_DIR )

    path    = "/etc/letsencrypt/live/" + base_domain
    command = "openssl req -x509 -nodes -newkey rsa:1024 -days 1 -keyout '{}/privkey.pem' -out '{}/fullchain.pem' -subj '/CN=localhost'".format(path, path)

    sh.docker_compose("-f", CERTBOT_BASE_DIR + '/docker-compose.yml', "run", "--rm", "--entrypoint", command ,'certbot')


"""
def domain_exists(domain_name):
    pass
"""

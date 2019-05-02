 # /usr/bin/python

from sh import ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php, chmod, mv
from sh.contrib import git
import sh, contextlib, os
from releases import RELEASES, release_filename, REPO, release_extract_dir
from config import INSTALL_DIR, CACHE_DIR, TMP_DIR, ADMIN_DIR
import sys

def log(msg):
    print( echo( msg ) )

def _pull_release(release):
    if not release in RELEASES:
        raise ValueError('Invalid release')

    filename    = release_filename(release)
    if not os.path.isdir( CACHE_DIR ):
        log( "[i] Creating cache dir {} ".format( CACHE_DIR ) )
        mkdir("-p", CACHE_DIR )

    if not os.path.exists( CACHE_DIR + filename ):
        log( "[i] Downloading release {} ".format( filename ) )
        wget( REPO + filename, "-O", CACHE_DIR + filename)


def copy_src(release):
    _pull_release(release)
    filename    = CACHE_DIR + release_filename(release)
    extract_dir = CACHE_DIR + release_extract_dir(release)
    if not os.path.isdir( extract_dir ):
        log( "[i] Extracting {} ".format( filename ) )
        unzip("-n", "-q", filename, "-d", extract_dir)

    
    log( "[i] Removing old files ... " )
    rm("-rf", INSTALL_DIR)

    log( "[i] Copying files ... " )
    unzip("-n", "-q", extract_dir + '/prestashop.zip' , "-d", INSTALL_DIR)

    log( "[i] Renaming admin as {}".format(ADMIN_DIR) )
    mv(INSTALL_DIR + 'admin', INSTALL_DIR + ADMIN_DIR)

    chown("-R", "http:http", INSTALL_DIR)
    chmod("-R", "777", INSTALL_DIR + 'var/')


# php ./install-dev/index_cli.php --domain=prestashop.ps --db_server=localhost --db_name=XXXXXXXXXX --db_user=XXXXXXXXXX --db_password="XXXXXXXXXX"

def install(domain, db_server, db_name, db_user, db_password):
    log( "[i] Installing from index_cli.php ... " )
    cli = INSTALL_DIR + 'install/index_cli.php' 

    r = php(cli, "--domain={}".format(domain),
                 "--db_server={}".format(db_server),
                 "--db_name={}".format(db_name),
                 "--db_user={}".format(db_user),
                 "--db_password={}".format(db_password),
                 "--db_create=1",
                 "--language=fr",
                 "--country=fr")
    print( r )

    log( "[i] Removing install dir ... " )
    rm("-rf", INSTALL_DIR + 'install')

    chown("-R", "http:http", INSTALL_DIR)
    chmod("-R", "777", INSTALL_DIR + 'var/')





"""
    if os.path.isdir(INSTALL_DIR):
        log( "[i] {} directory already contains files, making nginx the owner...".format(INSTALL_DIR) )
        #chown("-R", "nginx:nginx", INSTALL_DIR)
    else:
        log( "[i] {} directory not found, creating...".format(INSTALL_DIR) )
        mkdir("-p", INSTALL_DIR)
        #chown("-R", "nginx:nginx", INSTALL_DIR)
"""
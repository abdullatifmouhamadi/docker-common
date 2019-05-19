 # /usr/bin/python

from sh import ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php, chmod, mv
from sh.contrib import git
import sh, contextlib, os
from releases import RELEASES, release_filename, REPO, release_extract_dir
from config import CACHE_DIR, TMP_DIR, ADMIN_DIR, APP_OWNER
import sys

from utils import log

def _pull_release(release):
    if not release in RELEASES:
        raise ValueError('Invalid release')

    filename = release_filename(release)
    if not os.path.isdir( CACHE_DIR ):
        log( "Creating cache dir {} ".format( CACHE_DIR ) )
        mkdir("-p", CACHE_DIR )

    if not os.path.exists( CACHE_DIR + filename ):
        log( "Downloading release {} ".format( filename ) )
        wget( REPO + filename, "-O", CACHE_DIR + filename)


def copy_src(installDir, release):
    _pull_release(release)
    filename    = CACHE_DIR + release_filename(release)
    extract_dir = CACHE_DIR + release_extract_dir(release)
    if not os.path.isdir( extract_dir ):
        log( "Extracting {} ".format( filename ) )
        unzip("-n", "-q", filename, "-d", extract_dir)

    
    log( "Removing old files ... " )
    rm("-rf", installDir)

    log( "Creating install dir {} ... ".format(installDir) )
    mkdir("-p", installDir )

    log( "Copying files ... " )
    unzip("-n", "-q", extract_dir + '/prestashop.zip' , "-d", installDir)

    log( "Renaming admin as {}".format(ADMIN_DIR) )
    mv(installDir + 'admin', installDir + ADMIN_DIR)

    chown("-R", APP_OWNER, installDir)
    chmod("-R", "777", installDir + 'var/')


# php ./install-dev/index_cli.php --domain=prestashop.ps --db_server=localhost --db_name=XXXXXXXXXX --db_user=XXXXXXXXXX --db_password="XXXXXXXXXX"

def install(installDir, domain, db_server, db_name, db_user, db_password):
    log( "Installing from index_cli.php ... " )
    cli = installDir + 'install/index_cli.php' 

    r = php(cli, "--domain={}".format(domain),
                 "--db_server={}".format(db_server),
                 "--db_name={}".format(db_name),
                 "--db_user={}".format(db_user),
                 "--db_password={}".format(db_password),
                 "--db_create=1",
                 "--ssl=1",
                 "--email=admin@biachara.com",
                 "--password=admin",
                 "--language=fr",
                 "--country=fr")
    print( r )

    log( "Removing install dir ... " )
    rm("-rf", installDir + 'install')

    chown("-R", APP_OWNER, installDir)
    chmod("-R", "777", installDir + 'var/')





"""
    if os.path.isdir(INSTALL_DIR):
        log( "[i] {} directory already contains files, making nginx the owner...".format(INSTALL_DIR) )
        #chown("-R", "nginx:nginx", INSTALL_DIR)
    else:
        log( "[i] {} directory not found, creating...".format(INSTALL_DIR) )
        mkdir("-p", INSTALL_DIR)
        #chown("-R", "nginx:nginx", INSTALL_DIR)
"""
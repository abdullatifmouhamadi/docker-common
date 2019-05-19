 # /usr/bin/python

from prestashop import copy_src, install
from config import ( MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD )
import sh, os
from sh import mysqldump, cp, mysql, docker
from utils import logi
from config import INSTANCES_DIR, DOMAIN_NAME

"""
def _release_dir(release):
    return INSTANCES_DIR + release
"""



def _release_dir(release):
    return INSTANCES_DIR + release +'/'

def _install_dir(release):
    release_dir = _release_dir(release)
    return release_dir + 'app/'

def _image_name(release):
    return 'prestashop' + release.replace('.','')

def _database_name(release):
    release_name  = release.replace('.','')
    db_name = "prestashop" + release_name
    return db_name

def _dump_filename(release):
    database_name = _database_name(release)
    dump          = database_name + '.sql'
    return dump

def dump_path( release ):
    filename    = _dump_filename(release)
    release_dir = _release_dir(release)
    path        = release_dir + filename
    return path

def loge(msg):
    print( "[error] => " + msg )

def dump_database(release, db_user, db_password):
    database_name = _database_name(release)
    release_dir   = _release_dir(release)
    filename = _dump_filename(release)

    src_database = database_name
    target       = release_dir + '/' + filename
    mysqldump("-u", db_user, "-p" + db_password, src_database, '--result-file', target )


def remove_database(db_user, db_password, db_name):
    logi("Removing db '{}' ...".format(db_name))
    mysql("-u", db_user, "-p" + db_password , "-e", "DROP DATABASE IF EXISTS {}".format( db_name ) )

def copy_templates(release):
    release_dir   = _release_dir(release)
    cp("-arf", './images/files', release_dir)
    cp("./images/Dockerfile", release_dir)


def setup(release):
    install_dir = _install_dir(release)
    database_name = _database_name(release)

    if not os.path.isdir( install_dir ):

        remove_database(MYSQL_USER, MYSQL_PASSWORD, database_name)
        copy_src(installDir = install_dir, release = release)

        install(installDir  = install_dir, 
                domain      = DOMAIN_NAME, 
                db_server   = MYSQL_HOST,
                db_name     = database_name, 
                db_user     = MYSQL_USER, 
                db_password = MYSQL_PASSWORD)

        dump_database(release, db_user = MYSQL_USER, db_password = MYSQL_PASSWORD)
    else:
        logi( "The instance '{}' ".format(release) + 'already exist ...' )
    copy_templates(release)


def _image_exists(image_name):
    r = docker("images", "-q", image_name)
    if r=="":
        return False
    return True
    


def build_image(release):
    image_name = _image_name(release)
    release_dir = _release_dir(release)

    if _image_exists(image_name) == True:
        loge("Image {} already exists".format(image_name))
    else:
        logi("Building docker image {}".format(image_name))
        for line in docker('image', 'build', '-t', image_name, release_dir, _iter=True):
            logi(line)


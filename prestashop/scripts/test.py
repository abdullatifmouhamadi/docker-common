 # /usr/bin/python

from prestashop import copy_src, install
from config import ( MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, DOMAIN )
import sh, os
from sh import mysqldump, cp, mysql
from prestashop import logi

release       = '1.7.5.1'
instances_dir = '/home/prestashopd/instances/'
release_dir   = instances_dir + release
install_dir   = release_dir + '/app/'
release_name  = release.replace('.','')
database_name = "prestashop" + release_name


def loge(msg):
    print( "[error] => " + msg )

def dump_database(db_user, db_password):
    src_database = database_name
    target       = release_dir + '/' + database_name + '.sql'
    mysqldump("-u", db_user, "-p" + db_password, src_database, '--result-file', target )


def remove_database(db_user, db_password, db_name):
    logi("Removing db '{}' ...".format(db_name))
    mysql("-u", db_user, "-p" + db_password , "-e", "DROP DATABASE IF EXISTS {}".format( db_name ) )


def duplicate_db(src_dump, target_db):


    pass


def copy_templates():
    cp("-arf", './images/files', release_dir)
    cp("./images/Dockerfile", release_dir)


if not os.path.isdir( install_dir ):

    remove_database('root', 'root', database_name)

    copy_src(installDir = install_dir, release = release)

    

    install(installDir  = install_dir, 
            domain      = 'localhost:9095', 
            db_server   = 'localhost',
            db_name     = database_name, 
            db_user     = 'root', 
            db_password = 'root')

    dump_database(db_user = 'root', db_password = 'root')

else:
    loge( "The instance '{}' ".format(release) + 'already exist ...' )


copy_templates()





"""
# change database_name from '/app/config/parameters.php' then :
mysql -u root -proot -e "create database prestashop_houda";
mysqldump -u root -proot prestashop > backup.sql
mysql -u root -proot prestashop_houda < backup.sql

# external host
mysql -h 172.18.0.2 -P 3306 -u root -p1234 -e "create database prestashop_houda";
mysql -h 172.18.0.2 -P 3306 -u root -p1234 prestashop_houda < backup.sql

"""


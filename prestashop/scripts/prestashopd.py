
from sh import ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php, chmod, mv
import sh, contextlib, os
from config import PRESTASHOPD_USERS_DIR
import sys
from utils import logi
from instances import dump_path, _dump_filename

from sh import cp, sed, mysql
from config import DOMAIN_NAME

def domain_path(domain, release):
    path = PRESTASHOPD_USERS_DIR + domain + '/'
    return path


def configure_mysqldump(sql_file, domain):
    sed("-i", "s/{}/{}/g".format(DOMAIN_NAME, domain), sql_file)


def init_domain(domain, release):
    if not os.path.isdir( PRESTASHOPD_USERS_DIR ):
        logi( "Creating main directory {} ".format( PRESTASHOPD_USERS_DIR ) )
        mkdir("-p", PRESTASHOPD_USERS_DIR )


    DOMAIN_DIR = PRESTASHOPD_USERS_DIR + domain
    if not os.path.isdir( DOMAIN_DIR ):
        logi( "Creating domain directory {} ".format( DOMAIN_DIR ) )
        mkdir("-p", DOMAIN_DIR )

    
    sqldump_file = dump_path( release )
    domain_dir   = domain_path(domain, release)
    logi("Copying sql dump file '{}' to '{}'".format(sqldump_file, domain_dir))
    cp("-arf", sqldump_file, domain_dir)


    sql_filename = _dump_filename(release)
    copied_sqldump_file = domain_dir + sql_filename
    logi("Configuring mysql dump file {}".format(copied_sqldump_file))
    configure_mysqldump(copied_sqldump_file, domain)



def dump_to_db(db, domain, release):

    #mysql -h 172.18.0.2 -P 3306 -u root -p1234 -e "create database prestashop_houda";
    #mysql -h 172.18.0.2 -P 3306 -u root -p1234 prestashop_houda < backup.sql

    logi("Removing db '{}' ...".format(db['MYSQL_DATABASE']))
    sql(db, request = "DROP DATABASE IF EXISTS {}".format( db['MYSQL_DATABASE'] ))

    logi("Creating db '{}' ...".format(db['MYSQL_DATABASE']))
    sql(db, request = "CREATE DATABASE IF EXISTS {}".format( db['MYSQL_DATABASE'] ))

    

def sql(db, request):
    mysql("-h", db['MYSQL_HOST'], '-P', '3306', "-u", db['MYSQL_USER'], "-p" + db['MYSQL_PASSWORD'] , "-e", request )




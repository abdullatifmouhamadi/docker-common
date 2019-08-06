
from sh import ls, printenv, Command, echo, chown, mkdir, wget, unzip, rm, php, chmod, mv
import sh, contextlib, os
from config import PRESTASHOPD_USERS_DIR
import sys
from utils import logi, loge, replace
from instances import dump_path, _dump_filename, _install_dir, _database_name, _release_dir
from config import ( MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD )

from sh import cp, sed, mysql
from config import DOMAIN_NAME

def domain_path(domain, release):
    path = PRESTASHOPD_USERS_DIR + domain + '/'
    return path

def sql_filepath(domain, release):
    domain_dir   = domain_path(domain, release)
    sql_filename = _dump_filename(release)
    return domain_dir + sql_filename

def configure_mysqldump(sql_file, domain):
    sed("-i", "s/{}/{}/g".format(DOMAIN_NAME, domain), sql_file)

def configure_configfiles(db, user_config):
    domain        = user_config['HOST_DOMAIN']
    release       = user_config['PRESTASHOP_RELEASE']
    user_database = db['MYSQL_DATABASE']
    template_db   = _database_name(release)

    # parameters config
    domain_dir     = domain_path(domain, release)
    parameter_dir  = domain_dir + 'app/config/'
    parameter_file = parameter_dir + 'parameters.php'
    if not os.path.isdir( parameter_dir ):
        mkdir("-p", parameter_dir )

    parameter_srcpath = _install_dir(release) + 'app/config/parameters.php'
    cp("-rf", parameter_srcpath, parameter_dir)


    # startup script config
    startupscript_dir  = domain_dir + 'usr/html/'
    startupscript_file = startupscript_dir + 'startup.php'
    if not os.path.isdir( startupscript_dir ):
        mkdir("-p", startupscript_dir )

    startupscript_srcpath = _release_dir(release) + 'files/startup.php'
    cp("-rf", startupscript_srcpath, startupscript_dir)




    replace(old  = "'database_host' => 'localhost',", 
            new  = "'database_host' => '{}',".format(db['MYSQL_HOST']), 
            file = parameter_file)
    replace(old  = "'database_port' => '',", 
            new  = "'database_port' => '{}',".format(3306), 
            file = parameter_file)
    replace(old  = "'database_name' => '{}',".format(template_db), 
            new  = "'database_name' => '{}',".format(user_database), 
            file = parameter_file)
    replace(old  = "'database_user' => '{}',".format(MYSQL_USER), 
            new  = "'database_user' => '{}',".format(db['MYSQL_USER']), 
            file = parameter_file)
    replace(old  = "'database_password' => '{}',".format(MYSQL_PASSWORD), 
            new  = "'database_password' => '{}',".format(db['MYSQL_PASSWORD']), 
            file = parameter_file)





def init_domain(db, user_config):
    domain  = user_config['HOST_DOMAIN']
    release = user_config['PRESTASHOP_RELEASE']


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


    copied_sqldump_file = sql_filepath(domain, release)
    logi("Configuring mysql dump file {}".format(copied_sqldump_file))
    configure_mysqldump(copied_sqldump_file, domain)

    logi( "Configuring config files ... " )
    configure_configfiles(db, user_config)




def remove_db(db, domain, release):
    logi("Removing db '{}' ...".format(db['MYSQL_DATABASE']))
    sql(db, request = "DROP DATABASE IF EXISTS {}".format( db['MYSQL_DATABASE'] ))

def db_exists(db):
    r = sql(db, request = "SHOW DATABASES LIKE '{}';".format( db['MYSQL_DATABASE'] ))
    if r == "":
        return False
    return True


def copy_db(db, user_config):
    domain  = user_config['HOST_DOMAIN']
    release = user_config['PRESTASHOP_RELEASE']

    if db_exists(db):
        loge("Database '{}' already exists".format(db['MYSQL_DATABASE']))
    else:
        logi("Creating db '{}' ...".format(db['MYSQL_DATABASE']))
        sql(db, request = "CREATE DATABASE {}".format( db['MYSQL_DATABASE'] ))

        copied_sqldump_file = sql_filepath(domain, release)
        logi("Importing dump file '{}' to database {}...".format(copied_sqldump_file, db['MYSQL_DATABASE']))
        #mysql("-h", db['MYSQL_HOST'], '-P', '3306', "-u", db['MYSQL_USER'], "-p" + db['MYSQL_PASSWORD'] , db['MYSQL_DATABASE'], '<', copied_sqldump_file )
        mysql("-h", db['MYSQL_HOST'], '-P', '3306', "-u", db['MYSQL_USER'], "-p" + db['MYSQL_PASSWORD'] , db['MYSQL_DATABASE'], _in = sh.cat(copied_sqldump_file) )


def sql(db, request):
    return mysql("-h", db['MYSQL_HOST'], '-P', '3306', "-u", db['MYSQL_USER'], "-p" + db['MYSQL_PASSWORD'] , "-e", request )



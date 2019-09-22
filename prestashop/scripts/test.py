
from instances import setup as setup_instance, build_image
from prestashopd import init_domain, copy_db

GENERATE_DOCKER_IMAGE = 1
CREATE_SHOP           = 2
DB_HOST               = '172.17.0.3'
DB_USER               = 'root'
DB_PWD                = '1234'

# config
RELEASE               = '1.7.6.1'
ACTION                = CREATE_SHOP#GENERATE_DOCKER_IMAGE #CREATE_SHOP

# create docker image
DOCKER_IMAGE_HOST     = 'localhost:9086'
DOCKER_IMAGE_DB_NAME  = 'prestashop1761'


# create shop
CREATE_SHOP_HOST      = 'localhost:9087'
CREATE_SHOP_DB_NAME   = 'prestashop1761_9087'


setup_instance(release = RELEASE)


if ACTION == GENERATE_DOCKER_IMAGE:
    user_config = {
        'HOST_DOMAIN':DOCKER_IMAGE_HOST,#'douka-prive.biachara.com',
        'PRESTASHOP_RELEASE':RELEASE,
    }
    db_config = {
        'MYSQL_HOST':DB_HOST,
        'MYSQL_DATABASE':DOCKER_IMAGE_DB_NAME,
        'MYSQL_USER':DB_USER,
        'MYSQL_PASSWORD':DB_PWD,
    }
    init_domain(db = db_config, user_config = user_config)
    build_image(user_config['PRESTASHOP_RELEASE'])
    
elif ACTION == CREATE_SHOP:
    user_config = {
        'HOST_DOMAIN':CREATE_SHOP_HOST,
        'PRESTASHOP_RELEASE':RELEASE,
    }
    db_config = {
        'MYSQL_HOST':DB_HOST,
        'MYSQL_DATABASE':CREATE_SHOP_DB_NAME,
        'MYSQL_USER':DB_USER,
        'MYSQL_PASSWORD':DB_PWD,
    }
    init_domain(db = db_config, user_config = user_config)
    copy_db(db = db_config, user_config = user_config)
    
else:
    print("ERROR")






# bugs to correct
#1 /home/prestashopd/instances/1.7.6.0/app/config/themes/classic/shop1.json -> replace directory to /usr/html/
#2 rm /home/prestashopd/instances/1.7.6.0/app/var/cache


# todo
"""
chmod -R 777 /usr/html/var

"""

# install php
"""
php php-gd php-intl


/etc/php/php.ini
curl,zip
gd, iconv, intl, pdo_mysql

"""


"""
# change database_name from '/app/config/parameters.php' then :
mysql -u root -proot -e "create database prestashop_houda";
mysqldump -u root -proot prestashop > backup.sql
mysql -u root -proot prestashop_houda < backup.sql

# external host
mysql -h 172.18.0.2 -P 3306 -u root -p1234 -e "create database prestashop_houda";
mysql -h 172.18.0.2 -P 3306 -u root -p1234 prestashop_houda < backup.sql

"""


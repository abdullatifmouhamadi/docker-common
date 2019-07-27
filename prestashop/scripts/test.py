
from instances import setup as setup_instance, build_image
from prestashopd import init_domain, copy_db

user_config = {
    'HOST_DOMAIN':'localhost:9086',#'douka-prive.biachara.com',
    'PRESTASHOP_RELEASE':'1.7.6.0',
}

db_config = {
    'MYSQL_HOST':'172.17.0.2',
    'MYSQL_DATABASE':'prestashop1760_douka_prive',
    'MYSQL_USER':'root',
    'MYSQL_PASSWORD':'1234',
}

setup_instance(release = user_config['PRESTASHOP_RELEASE'])

init_domain(db = db_config, user_config = user_config)


copy_db(db = db_config, user_config = user_config)

build_image(user_config['PRESTASHOP_RELEASE'])





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


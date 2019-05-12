 # /usr/bin/python

from utils import copy_src, install
from config import ( MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, DOMAIN )


install_dir = '/home/prestashopd/app/'
# 1.7.5.1
copy_src(installDir = install_dir, release = '1.7.5.1')
# copy_src(release = '1.7.4.4')

"""
install(domain      = DOMAIN, 
        db_server   = MYSQL_HOST, 
        db_name     = MYSQL_DATABASE, 
        db_user     = MYSQL_USER, 
        db_password = MYSQL_PASSWORD)
"""
# docker
install(installDir  = install_dir, 
        domain      = 'localhost:8080', 
        db_server   = '172.18.0.2',
        db_name     = 'prestashop1751', 
        db_user     = 'root', 
        db_password = '1234')


"""
# change database_name from '/app/config/parameters.php' then :
mysql -u root -proot -e "create database prestashop_houda";
mysqldump -u root -proot prestashop > backup.sql
mysql -u root -proot prestashop_houda < backup.sql

# external host
mysql -h 172.18.0.2 -P 3306 -u root -p1234 -e "create database prestashop_houda";
mysql -h 172.18.0.2 -P 3306 -u root -p1234 prestashop_houda < backup.sql


"""


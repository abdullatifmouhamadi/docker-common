 # /usr/bin/python

from utils import copy_src, install
from config import ( MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, DOMAIN )

# 1.7.5.1
copy_src(release = '1.7.5.1')
# copy_src(release = '1.7.4.4')


install(domain      = DOMAIN, 
        db_server   = MYSQL_HOST, 
        db_name     = MYSQL_DATABASE, 
        db_user     = MYSQL_USER, 
        db_password = MYSQL_PASSWORD)


"""
# change database_name from '/app/config/parameters.php' then :
mysql -u root -proot -e "create database prestashop_houda";
mysqldump -u root -proot prestashop > backup.sql
mysql -u root -proot prestashop_houda < backup.sql
"""

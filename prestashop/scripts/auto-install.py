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




        
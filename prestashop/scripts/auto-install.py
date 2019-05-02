 # /usr/bin/python

from utils import copy_src, install




# 1.7.5.1
copy_src(release = '1.7.5.1')
# copy_src(release = '1.7.4.4')


install(domain      = "localhost:9090", 
        db_server   = "localhost", 
        db_name     = "prestashop", 
        db_user     = "root", 
        db_password = "root")




        
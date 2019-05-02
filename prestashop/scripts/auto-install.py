 # /usr/bin/python

from utils import copy_src, install





copy_src(release = '1.7.4.4')


install(domain      = "localhost", 
        db_server   = "localhost", 
        db_name     = "prestashop5", 
        db_user     = "root", 
        db_password = "root")




        
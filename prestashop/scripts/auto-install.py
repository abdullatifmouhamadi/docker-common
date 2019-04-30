 # /usr/bin/python

from sh import ls, printenv, Command
import sh

import contextlib
import os
from sh.contrib import git
import os

print(os.path.isdir("/srv/http/"))
print(os.path.exists("/home/el/myfile.txt"))


REPO = 'https://github.com/PrestaShop/PrestaShop'
WORKING_DIR = '/home/abdullatif/Bureau/test'


print(sh.whoami())
#sh.cd(WORKING_DIR)
#print(sh.git('clone', REPO, depth=1, b='1.7.4.4'))


#my_password = "verybad\n"
#my_sudo = sh.sudo.bake("-S", _in=my_password)
#print(my_sudo.pwd())



#docker container exec -it test-mariadb bash
#git('clone',WORKING_DIR, REPO)

"""
sh.cd('/')

print("coucou : {}".format(''))
output = ls("/")
print(printenv('SHELL')) # should be 0

"""


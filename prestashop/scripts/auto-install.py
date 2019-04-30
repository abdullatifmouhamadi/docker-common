 # /usr/bin/python

from sh import ls, printenv




print("coucou")
output = ls("/")
print(printenv('SHELL')) # should be 0





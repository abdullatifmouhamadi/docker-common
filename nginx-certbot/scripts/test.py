 # /usr/bin/python
import sh
from certbot import request_certificate



request_certificate(domains=['maoredev.com', 'www.maoredev.com'], email="maoredev.biachara@gmail.com", staging=0)





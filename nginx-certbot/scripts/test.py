 # /usr/bin/python
import sh
from certbot import init_certbot_env, create_dummy_certificate

init_certbot_env()

create_dummy_certificate(['example.com', 'www.example.com'])
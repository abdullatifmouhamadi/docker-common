# nginx-proxy

http://jasonwilder.com/
https://medium.com/@mq5037204/docker-nginx-reverse-proxy-f568d148d3bd

https://github.com/jwilder/nginx-proxy
https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion

https://ie-concept.fr/docker-nginx-letsencrypt/





#

```
docker pull jwilder/nginx-proxy:alpine
docker pull jrcs/letsencrypt-nginx-proxy-companion




docker run --detach \
--name nginx-proxy \
--publish 80:80 \
--publish 443:443 \
--mount type=bind,source=/home/docker/nginx-proxy/certs,target=/etc/nginx/certs \
--mount type=bind,source=/home/docker/nginx-proxy/vhost.d,target=/etc/nginx/vhost.d \
--mount type=bind,source=/home/docker/nginx-proxy/html,target=/usr/share/nginx/html \
--mount type=bind,source=/home/docker/nginx-proxy/conf.d,target=/etc/nginx/conf.d \
--volume /var/run/docker.sock:/tmp/docker.sock:ro \
jwilder/nginx-proxy:alpine



docker run --detach \
--name nginx-proxy-letsencrypt \
--volumes-from nginx-proxy \
--volume /var/run/docker.sock:/var/run/docker.sock:ro \
jrcs/letsencrypt-nginx-proxy-companion


docker run --detach \
--name your-proxyed-app \
--env "VIRTUAL_HOST=www.douka-prive.biachara.com,douka-prive.biachara.com" \
--env "LETSENCRYPT_HOST=www.douka-prive.biachara.com,douka-prive.biachara.com" \
--env "LETSENCRYPT_EMAIL=maoredev.biachara@gmail.com" \
nginx




## Configure nginx 

https://github.com/jwilder/nginx-proxy/blob/master/README.md#custom-nginx-configuration

client_max_body_size 128M;

$ { echo 'proxy_cache my-cache;'; echo 'proxy_cache_valid  200 302  60m;'; echo 'proxy_cache_valid  404 1m;' } > /home/docker/nginx-proxy/vhost.d/douka-prive.biachara.com




####################################################################################################################################



################################################################################
## shop 0 - douka-prive.biachara.com
docker run --detach \
--name douka-prive.biachara.com \
--env "VIRTUAL_HOST=www.douka-prive.biachara.com,douka-prive.biachara.com" \
--env "LETSENCRYPT_HOST=www.douka-prive.biachara.com,douka-prive.biachara.com" \
--env "LETSENCRYPT_EMAIL=maoredev.biachara@gmail.com" \
--mount type=bind,source=/home/prestashopd/domains/douka-prive.biachara.com/app/config/parameters.php,target=/usr/html/app/config/parameters.php \
--mount type=bind,source=/home/prestashopd/domains/douka-prive.biachara.com/usr/html/startup.php,target=/usr/html/startup.php \
prestashop1760:latest

docker exec douka-prive.biachara.com bash -c "php /usr/html/startup.php"
docker container restart douka-prive.biachara.com

################################################################################
## shop 1 - douka.prive.yt
docker run --detach \
--name douka.prive.yt \
--env "VIRTUAL_HOST=www.douka.prive.yt,douka.prive.yt" \
--env "LETSENCRYPT_HOST=www.douka.prive.yt,douka.prive.yt" \
--env "LETSENCRYPT_EMAIL=maoredev.biachara@gmail.com" \
--mount type=bind,source=/home/prestashopd/domains/douka.prive.yt/app/config/parameters.php,target=/usr/html/app/config/parameters.php \
--mount type=bind,source=/home/prestashopd/domains/douka.prive.yt/usr/html/startup.php,target=/usr/html/startup.php \
prestashop1760:latest

docker exec douka.prive.yt bash -c "php /usr/html/startup.php"
docker container restart douka.prive.yt


################################################################################
## shop 2 - elec.prive.yt
docker run --detach \
--name elec.prive.yt \
--env "VIRTUAL_HOST=www.elec.prive.yt,elec.prive.yt" \
--env "LETSENCRYPT_HOST=www.elec.prive.yt,elec.prive.yt" \
--env "LETSENCRYPT_EMAIL=maoredev.biachara@gmail.com" \
--mount type=bind,source=/home/prestashopd/domains/elec.prive.yt/app/config/parameters.php,target=/usr/html/app/config/parameters.php \
--mount type=bind,source=/home/prestashopd/domains/elec.prive.yt/usr/html/startup.php,target=/usr/html/startup.php \
prestashop1760:latest

docker exec elec.prive.yt bash -c "php /usr/html/startup.php"
docker container restart elec.prive.yt

```

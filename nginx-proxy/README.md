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




```
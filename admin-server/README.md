# Datastore for mariadb datastore
-> nginx
-> phpmyadmin

# images

https://hub.docker.com/_/nginx
https://hub.docker.com/r/phpmyadmin/phpmyadmin

https://github.com/phpmyadmin/docker


nginx:1.15-alpine
phpmyadmin/phpmyadmin:4.8

# phpmyadmin


```
# 
docker run --name test-phpmyadmin -d -e PMA_ARBITRARY=1 -p 8080:80 phpmyadmin/phpmyadmin:4.8

# erase
docker container stop test-phpmyadmin && docker container rm test-phpmyadmin && docker volume rm test-phpmyadmin

```

# adminer


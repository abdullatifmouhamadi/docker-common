# Prestashop images


https://hub.docker.com/r/yobasystems/alpine-prestashop


yobasystems/alpine-prestashop

```
# -v test-prestashop:/usr/html

docker run --name test-prestashop \
-e PS_INSTALL_AUTO="1" \
-e URL="localhost" \
-e VIRTUAL_HOST="localhost" \
-e MYSQL_HOST="172.17.0.2" \
-e MYSQL_DATABASE="test_prestashop" \
-e MYSQL_USER="root" \
-e MYSQL_PASSWORD="1234" \
-d yobasystems/alpine-prestashop


# commons
docker container logs test-prestashop
docker container inspect test-prestashop
docker container exec -it test-prestashop bash


# erase
docker container stop test-prestashop && docker container rm test-prestashop && docker volume rm test-prestashop 

```
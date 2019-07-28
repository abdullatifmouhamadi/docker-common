# Prestashop images


https://hub.docker.com/r/yobasystems/alpine-prestashop


yobasystems/alpine-prestashop

```
# -v test-prestashop:/usr/html
# -v $(pwd):/usr/share/nginx/html
docker run --name test-prestashop \
-e PS_INSTALL_AUTO="1" \
-e URL="localhost" \
-e VIRTUAL_HOST="localhost" \
-e MYSQL_HOST="172.17.0.2" \
-e MYSQL_DATABASE="test_prestashop" \
-e MYSQL_USER="root" \
-e MYSQL_PASSWORD="1234" \
--mount type=bind,source=/home/prestashopd,target=/home/prestashopd \
--mount type=bind,source=$(pwd),target=/scripts \
--net my_app_net \
-p 8080:8080 \
-d yobasystems/alpine-prestashop


# commons
docker container logs test-prestashop
docker container inspect test-prestashop
docker container exec -it test-prestashop bash


# erase
docker container stop test-prestashop && docker container rm test-prestashop && docker volume rm test-prestashop 

```

# my
```
apk update && apk add --no-cache python3 && pip3 install --no-cache-dir --upgrade pip && pip3 install sh

```


# manual build
```
docker container run --name presta -it alpine sh



docker image build -t prestashop1751 /home/prestashopd/instances/1.7.5.1/
docker container run --name presta -p 9095:80 -d prestashop1751

docker container run --rm -p 80:80 -it prestashop1751 bash


docker container logs presta
docker container exec -it presta sh




docker container rm presta


```


# prestashop auto install
https://gist.github.com/Ilshidur/5d6425e0b697bd87b8e9b8d195ff1047?fbclid=IwAR25quV5AxT1tI1Sve37M1YHrMgDZO0HAgcOuRxzDoc47KTjpo5apDSMZUA

https://github.com/PrestaShop/docker/issues/109?fbclid=IwAR3mnOAd-NGHUrtFZPZSbYoQEmpiDZLo7AGLedO9DWCsjZ0BkfXgw-CAGtQ

https://gist.github.com/adamczykjac/1d49b1f663a3cb632ba46579bce00897?fbclid=IwAR3UOBkANt-X8batM875M13HDcn35RTi-HcWN-utpumcyVKr7ZRx3zvEDKE

https://gist.github.com/julienbourdeau/205df55bcf8aa290bd9e


# to deploy

```
docker run --detach \
--name presta \
--publish 9086:80 \
--mount type=bind,source=/home/prestashopd/domains/localhost:9086/app/config/parameters.php,target=/usr/html/app/config/parameters.php \
prestashop1760:latest





docker container exec -it presta bash


docker container rm presta


```




# bugs

https://github.com/PrestaShop/PrestaShop/issues/10998


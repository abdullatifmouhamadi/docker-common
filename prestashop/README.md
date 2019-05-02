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



# prestashop auto install
https://gist.github.com/Ilshidur/5d6425e0b697bd87b8e9b8d195ff1047?fbclid=IwAR25quV5AxT1tI1Sve37M1YHrMgDZO0HAgcOuRxzDoc47KTjpo5apDSMZUA

https://github.com/PrestaShop/docker/issues/109?fbclid=IwAR3mnOAd-NGHUrtFZPZSbYoQEmpiDZLo7AGLedO9DWCsjZ0BkfXgw-CAGtQ

https://gist.github.com/adamczykjac/1d49b1f663a3cb632ba46579bce00897?fbclid=IwAR3UOBkANt-X8batM875M13HDcn35RTi-HcWN-utpumcyVKr7ZRx3zvEDKE

https://gist.github.com/julienbourdeau/205df55bcf8aa290bd9e

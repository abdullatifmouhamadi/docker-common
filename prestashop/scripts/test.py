
from instances import setup as setup_instance
from prestashopd import init_domain


r = '1.7.5.2'
setup_instance(release = r)

init_domain(domain = 'mouha.biachara.com', release = r)


db_config = {
    'MYSQL_HOST':'172.17.0.3',
    'MYSQL_DATABASE':'prestashop_gedo',
    'MYSQL_USER':'root',
    'MYSQL_PASSWORD':'1234',
}



"""
# change database_name from '/app/config/parameters.php' then :
mysql -u root -proot -e "create database prestashop_houda";
mysqldump -u root -proot prestashop > backup.sql
mysql -u root -proot prestashop_houda < backup.sql

# external host
mysql -h 172.18.0.2 -P 3306 -u root -p1234 -e "create database prestashop_houda";
mysql -h 172.18.0.2 -P 3306 -u root -p1234 prestashop_houda < backup.sql

"""


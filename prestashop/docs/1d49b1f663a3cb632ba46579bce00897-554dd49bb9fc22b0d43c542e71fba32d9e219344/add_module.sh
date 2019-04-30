## REMOVE THIS LINE - Invoke me in your Docker image inheriting from prestashop/prestashop REMOVE THIS LINE ##
#!/usr/bin/env bash

set -e

# Constants
MODULES_TMP_DIR='/tmp/modules'
ARCHIVE_EXT='tar.gz'
PS_ROOT='/var/www/html'
PS_MODULES_DIR='/var/www/html/modules'
PS_INSTALL_FILE='src/PrestaShopBundle/Install/Install.php'

mkdir -p $MODULES_TMP_DIR
# source: stackoverflow.com/questions/10929453/read-a-file-line-by-line-assigning-the-value-to-a-variable
while IFS=',' read -r url module_name; do
    wget -q $url -O "$MODULES_TMP_DIR/$module_name.$ARCHIVE_EXT"
    tar xfz "$MODULES_TMP_DIR/$module_name.$ARCHIVE_EXT" -C $MODULES_TMP_DIR
    # source: stackoverflow.com/questions/1506521/select-row-and-element-in-awk
    cd $MODULES_TMP_DIR
    MODULE_DIR="$(ls -d */ | head -1)"
    # Copy module content to PrestaShop modules directory
    mkdir -p "$PS_MODULES_DIR/$module_name"
    # MODULE_DIR includes slash at its end
    cp -R "$MODULES_TMP_DIR/$MODULE_DIR$module_name" $PS_MODULES_DIR
    # Add module name to the preinstalled list after default 'Welcome' module
    sed -i "/'welcome',/a '$module_name'," "$PS_ROOT/$PS_INSTALL_FILE"
    # Cleanup
    rm -rf $MODULES_TMP_DIR
done < "$1"
# Remove 'welcome' module, as it is not needed
sed -i "/'welcome',/d" "$PS_ROOT/$PS_INSTALL_FILE"
<?php

// Workaround for redirection on init
$_POST['id_shop'] = 1;

require_once 'config/config.inc.php';

if (!defined('_PS_VERSION_'))
        exit;


class WebserviceKeyMD extends ObjectModel {
    public static function getAccountId($auth_key)
    {
        return Db::getInstance(_PS_USE_SQL_SLAVE_)->getValue('
                SELECT id_webservice_account
                FROM `' . _DB_PREFIX_ . 'webservice_account`
                WHERE `key` = "' . pSQL($auth_key) . '"');
    }
}


//$methods = array('GET', 'PUT', 'POST', 'DELETE', 'HEAD');
$methods = array('GET'=>true, 'PUT'=>true, 'POST'=>true, 'DELETE'=>true, 'HEAD'=>true);

$methods_put_post_delete = array('PUT'=>true, 'POST'=>true, 'DELETE'=>true,);
$methods_post_delete = array('POST'=>true, 'DELETE'=>true);
$methods_delete = array('DELETE'=>true);
$permissions = array(
    'addresses' => $methods,
    'carriers' => $methods,
    'carts' => $methods,
    'cart_rules' => $methods,
    'categories' => $methods,
    'combinations' => $methods,
    'configurations' => $methods,
    'contacts' => $methods,
    'countries' => $methods,
    'currencies' => $methods,
    'customers' => $methods,
    'customer_threads' => $methods,
    'customer_messages' => $methods,
    'deliveries' => $methods,
    'groups' => $methods,
    'guests' => $methods,
    'images' => $methods,
    'image_types' => $methods,
    'languages' => $methods,
    'manufacturers' => $methods,
    'messages' => $methods,
    'order_carriers' => $methods,
    'order_details' => $methods,
    'order_histories' => $methods,
    'order_invoices' => $methods,
    'orders' => $methods,
    'order_payments' => $methods,
    'order_states' => $methods,
    'order_slip' => $methods,
    'price_ranges' => $methods,
    'product_features' => $methods,
    'product_feature_values' => $methods,
    'product_options' => $methods,
    'product_option_values' => $methods,
    'products' => $methods,
    'states' => $methods,
    'stores' => $methods,
    'suppliers' => $methods,
    'tags' => $methods,
    'translated_configurations' => $methods,
    'weight_ranges' => $methods,
    'zones' => $methods,
    'employees' => $methods,
    'search' => $methods_put_post_delete,
    'content_management_system' => $methods,
    'shops' => $methods,
    'shop_groups' => $methods,
    'taxes' => $methods,
    'stock_movements' => $methods_put_post_delete,
    'stock_movement_reasons' => $methods,
    'warehouses' => $methods_delete,
    'stocks' => $methods_put_post_delete,
    'stock_availables' => $methods_post_delete,
    'warehouse_product_locations' => $methods_put_post_delete,
    'supply_orders' => $methods_put_post_delete,
    'supply_order_details' => $methods_put_post_delete,
    'supply_order_states' => $methods_put_post_delete,
    'supply_order_histories' => $methods_put_post_delete,
    'supply_order_receipt_histories' => $methods_put_post_delete,
    'product_suppliers' => $methods,
    'tax_rules' => $methods,
    'tax_rule_groups' => $methods,
    'specific_prices' => $methods,
    'specific_price_rules' => $methods,
    'shop_urls' => $methods,
    'product_customization_fields' => $methods,
    'customizations' => $methods,
);



$api_key = "84247accade94a95b2d7a553842df989";

//$a = Configuration::get('PS_WEBSERVICE');

Configuration::updateValue('PS_REWRITING_SETTINGS', "1");
Configuration::updateValue('PS_WEBSERVICE', "1");
$exists = WebserviceKey::isKeyActive($api_key);

if(!$exists) {
        $ws = new WebserviceKey;
        $ws->key = $api_key;
        $res = $ws->add();
}

$exists = WebserviceKey::isKeyActive($api_key);
$id_account = WebserviceKeyMD::getAccountId($api_key);

WebserviceKey::setPermissionForAccount($id_account, $permissions);

var_dump($id_account);



die();

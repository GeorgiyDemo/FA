/*
Отображаем все продукты и их кол-во для определенного заказа
*/
SELECT products.title Продукт, products.price Цена, products_count.count "Кол-во продуктов", orders.cost "Общая стоиммость заказа" FROM products_count
INNER JOIN products ON products_count.product_id=products.id
INNER JOIN orders ON products_count.order_id=orders.id WHERE order_id=1;

/*
Отображаем клиентов, которые не делали заказ в ресторане
*/
SELECT clients.* FROM clients
LEFT JOIN orders ON orders.client_id = clients.id
WHERE orders.client_id IS NULL


/*
Получение тех домов, которые простаивают
*/


/*
Удаляем все данные из СУБД
*/
SET SQL_SAFE_UPDATES = 0;
DELETE FROM staffs_houses;
DELETE FROM products_count;
DELETE FROM products;
DELETE FROM orders;
DELETE FROM houses;
DELETE FROM bookings;
DELETE FROM staffs;
DELETE FROM clients;
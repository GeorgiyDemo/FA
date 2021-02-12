/*
Задача 1
Отображаем все продукты и их цену для определенного заказа
*/
SELECT
	products.title Продукт,
    products.price Цена,
    products_count.count "Кол-во продуктов",
    orders.cost "Общая стоиммость заказа"
    
FROM products_count

INNER JOIN products ON products_count.product_id=products.id
INNER JOIN orders ON products_count.order_id=orders.id WHERE order_id=1;

/*
Задача 2
Отображаем клиентов, которые не делали заказ в ресторане
*/
SELECT clients.* FROM clients
LEFT JOIN orders ON orders.client_id = clients.id
WHERE orders.client_id IS NULL


/*
Задача 3
TODO: Получение тех домов, которые простаивают
*/
SELECT * FROM HOUSES WHERE BOOKING_ID is NULL

/*
Задача 4
TODO: Получение домов, которые когда-либо заказывал опеределенный клиент
*/

/*
Задача 5
Сколько всего денег определенный клиент потратил на номера и ресторан (по имени)
*/

/*
Задача 6
Получаем название домов и их стоимость за ночь по определенному бронированию
*/
SELECT
	houses.name "Название дома",
    houses.price "Стоимость дома",
    bookings.cost "Общая стоимость заказа",
    bookings.date_out-bookings.date_in "Кол-во дней"
FROM bookings
INNER JOIN houses
	ON houses.booking_id = bookings.id WHERE bookings.id=53;

/*
Задача 7
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
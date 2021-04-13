/* 
Задача 1 
Отображаем все продукты и их цену для определенного заказа (макс/мин стоимость) 
*/ 

SELECT 
products.title Продукт, 
products.price Цена, 
products_count.count "Кол-во продуктов", 
orders.cost "Общая стоиммость заказа" 
FROM products_count
INNER JOIN products ON products_count.product_id=products.id 
INNER JOIN orders ON products_count.order_id=orders.id WHERE order_id=1; 


SELECT
orders.id "Номер самого дешевого заказа",
products.title Продукт, 
products.price Цена, 
products_count.count "Кол-во продуктов", 
orders.cost "Общая стоиммость заказа"
FROM products_count
INNER JOIN products ON products_count.product_id=products.id
INNER JOIN orders ON products_count.order_id=orders.id WHERE order_id=(SELECT id FROM orders WHERE cost=(SELECT MIN(cost) FROM orders)); 

SELECT
orders.id "Номер самого дешевого заказа",
products.title Продукт, 
products.price Цена, 
products_count.count "Кол-во продуктов", 
orders.cost "Общая стоиммость заказа"
FROM products_count
INNER JOIN products ON products_count.product_id=products.id
INNER JOIN orders ON products_count.order_id=orders.id WHERE order_id=(SELECT id FROM orders WHERE cost=(SELECT MIN(cost) FROM orders)); 

/* 
Задача 2 
Отображаем кол-во клиентов, которые делали заказ в ресторане за каждый год
*/
SELECT TO_CHAR(orders.order_date, 'YYYY') AS year, COUNT(DISTINCT clients.id) AS "Кол-во клиентов ресторана" FROM clients
INNER JOIN orders ON orders.client_id = clients.id GROUP BY TO_CHAR(orders.order_date, 'YYYY') ORDER BY year DESC

/* 
Задача 3
Отображаем кол-во клиентов, которые делали бронирование за каждый год
*/
SELECT TO_CHAR(bookings.date_out, 'YYYY') AS year, COUNT(DISTINCT clients.id) AS "Кол-во клиентов с бронированиями" FROM clients
INNER JOIN bookings ON bookings.client_id = clients.id GROUP BY TO_CHAR(bookings.date_out, 'YYYY') ORDER BY year DESC


/*
Задача 4
Получение кол-ва бронирований по каждому из домов за все время
*/
SELECT houses.id "Идентификатор дома", COUNT(bookings.id) "Кол-во бронирований" FROM bookings
INNER JOIN houses 
ON bookings.house_id=houses.id
GROUP BY bookings.house_id

/*
Задача 5
Получаем название домов, кол-во дней бронирования, стоимость за ночь
и общую стоимость заказа по определенному пользователю 
*/
SELECT
houses.name AS "Название дома",
houses.price AS "Цена за ночь",
bookings.date_out-bookings.date_in AS "Кол-во ночей",
bookings.cost AS "Общая стоимость"
FROM bookings
INNER JOIN houses ON bookings.house_id=houses.id
WHERE bookings.client_id=3
 
/*
Задача 6
Получение самых непопулярных домов для заказа
*/
SELECT house_id, COUNT(*) counter
FROM bookings
GROUP BY house_id ORDER BY counter

/*
Задача 7
Сколько всего денег определенный клиент потратил на номера и ресторан за определенный промежуток времени (ДИАПАЗОН ДАТ)
Вывести всех за период и сортировка по кол-ву потраченных денег
*/

/*
Задача 8
Получение дохода отеля (с ресторана и бронирований) за определенный промежуток времени (ДИАПАЗОН ДАТ)
*/

/*
Задача 9
Получение ФИО работников, которые обслуживали бронирования клиента
*/

/*
Задача 10
Подсчет по месяцам кол-ва бронирований за период (2019-2021)
*/

/*
Задача 11
Подсчет по месяцам кол-ва заказов в ресторане за период (2019-2021)
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
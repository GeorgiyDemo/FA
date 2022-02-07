/*  
Задача 1  
Отображаем все продукты и их цену для определенного заказа (макс/мин стоимость)  
*/  

SELECT 
products.title Продукт,  
products.price Цена,  
products_count.count "Кол-во продуктов",  
orders.cost "Общая стоимость заказа" 

FROM products_count  
JOIN products ON products_count.product_id=products.id 
JOIN orders ON products_count.order_id=orders.id WHERE order_id=1; 

SELECT  
orders.id "Номер самого дешевого заказа",  
products.title Продукт,  
products.price Цена,  
products_count.count "Кол-во продуктов",  
orders.cost "Общая стоимость заказа"  
FROM products_count  

JOIN products ON products_count.product_id=products.id  
JOIN orders ON products_count.order_id=orders.id 
WHERE order_id=( 
    SELECT id FROM orders WHERE cost=(SELECT MIN(cost) FROM orders) 
);  
 
SELECT  
orders.id "Номер самого дорогого заказа",
products.title Продукт,
products.price Цена,
products_count.count "Кол-во продуктов",
orders.cost "Общая стоимость заказа"

FROM products_count  
JOIN products ON products_count.product_id=products.id  
JOIN orders ON products_count.order_id=orders.id 
WHERE order_id= 
    (SELECT id FROM orders WHERE cost=(SELECT MAX(cost) FROM orders)
);  

/*  
Задача 2  
Отображаем кол-во клиентов, которые делали заказ в ресторане за каждый год 
*/
SELECT
TO_CHAR(o.order_date, 'YYYY') AS year,  
COUNT(DISTINCT c.id) AS "Кол-во клиентов ресторана"  
FROM clients c
JOIN orders o ON o.client_id = c.id
GROUP BY TO_CHAR(o.order_date, 'YYYY')
ORDER BY year DESC  

/*
Задача 3
Отображаем кол-во клиентов, которые делали бронирование за каждый год
*/ 

SELECT
TO_CHAR(b.date_out, 'YYYY') AS year,
COUNT(DISTINCT c.id) AS "Кол-во клиентов с бронированиями"
FROM clients c
JOIN bookings b ON b.client_id = c.id
GROUP BY TO_CHAR(b.date_out, 'YYYY')
ORDER BY year DESC

/*
Задача 4
Получение кол-ва бронирований по каждому из домов за все время
*/

SELECT
h.id "Идентификатор дома",
COUNT(b.id) "Кол-во бронирований"
FROM bookings b
JOIN houses h
ON b.house_id=h.id
GROUP BY b.house_id

/*
Задача 5
Получаем название домов, кол-во дней бронирования, стоимость за ночь
и общую стоимость заказа по определенному пользователю
*/

SELECT
h.name AS "Название дома",
h.price AS "Цена за ночь",
b.date_out-b.date_in AS "Кол-во ночей",
b.cost AS "Общая стоимость"
FROM bookings b
INNER JOIN houses h ON b.house_id=h.id
WHERE b.client_id=3

/*
Задача 6
Получение самых непопулярных домов для заказа
*/

SELECT house_id, COUNT(*) counter
FROM bookings
GROUP BY house_id ORDER BY counter

/* Задача 7
Вывод наиболее растратных клиентов в ресторане
*/

SELECT
orders_new.sum_cost,
clients.first_name || ' ' || clients.last_name name
FROM
(SELECT client_id, SUM(cost) sum_cost
FROM orders
GROUP BY client_id) orders_new
INNER JOIN clients ON orders_new.client_id=clients.id
ORDER BY orders_new.sum_cost DESC

/*
Задача 8
Сколько всего денег клиенты потратили на номера по годам
*/

SELECT
TO_CHAR(date_out, 'YYYY') year,
SUM(cost) sum_cost
FROM bookings
GROUP BY TO_CHAR(date_out, 'YYYY')
ORDER BY year DESC

/*Задача 9
Сколько всего потратил каждый клиент
*/ 

SELECT id, name, SUM(sum_cost) sum_cost
FROM (
SELECT
c.id,
c.first_name || ' ' || c.last_name name,
NVL(o.cost,0)+NVL(b.cost,0) sum_cost
FROM clients c
LEFT JOIN orders o ON c.id = o.client_id
LEFT JOIN bookings b ON c.id = b.client_id
)
GROUP BY id, name
ORDER BY sum_cost DESC

/*
Задача 10
Получение ФИО работников, которые обслуживали бронирования клиента
*/

SELECT
sh.staff_id id,
s.first_name || ' ' || s.last_name name,
s.position,
s.phone
FROM bookings b
JOIN staffs_houses sh ON b.house_id=sh.house_id
JOIN staffs s ON sh.staff_id=s.id
WHERE s.type='staff_house' AND b.client_id=3
use classicmodels;
show tables;
select * from employees;
SHOW CREATE TABLE orderdetails;
SHOW CREATE TABLE orderdetails;
desc orderdetails;

---- sirf quantity dikhane ke liye
select quantityOrdered from orderdetails; 

--- products naame dikhane ke liye
select productName from products;

-- dono ko connect krte h hume productname or q.ordered ek sath cahiye --
select p.productName,od.quantityOrdered from
orderdetails od join products p on od.productCode = p.productCode;

--- quantity order ka sum kro or same group ko group by se combine kro car bar bar aa rha h
select 
    p.productName,sum(od.quantityOrdered) from orderdetails od
join products p on od.productCode = p.ProductCode -- productcide donu m common coloumn h
group by p.productName; 

--- higesht value upper aa gyi order by se or limit 10 se top ke 10
select 
    p.productName,sum(od.quantityOrdered) from orderdetails od
join products p on od.productCode = p.ProductCode 
group by p.productName
order by sum(od.quantityOrdered) desc
limit 10 ;



create view top_selling_products as
select 
    p.productName,sum(od.quantityOrdered) from orderdetails od
join products p on od.productCode = p.ProductCode 
group by p.productName
order by sum(od.quantityOrdered) desc
limit 10 ;

select * from top_selling_products;

-- pahle individual revenue dekhte h 
select quantityOrdered, priceEach, quantityOrdered * priceEach as revenue 
from orderdetails;

-- ab day/month order table se aayge isko join krte h od se sath
select o.orderDate, od.quantityOrdered,od.priceEach
from orders o join orderdetails od on o.orderNumber = od.orderNumber;

-- ab revenue calculagte krte h
SELECT
    o.orderDate,
    od.quantityOrdered * od.priceEach AS revenue
FROM orders o
JOIN orderdetails od
ON o.orderNumber = od.orderNumber;

-- ab month ke hisab se nikalte h
CREATE VIEW monthly_revenue AS
SELECT
    MONTH(o.orderDate) AS month,
    SUM(od.quantityOrdered * od.priceEach) AS total_revenue
FROM orders o
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
GROUP BY MONTH(o.orderDate);

select * from monthly_revenue;

-- repeated customers
-- cnum or cname dikha diye 
select c.customerName,o.customerNumber from customers c JOIN orders o
ON c.customerNumber = o.customerNumber;


-- repeated customer  phle c.name or c.num combine kye group by se combine kiya having count 1 se jyada order wala customer
CREATE VIEW repeat_customers AS
SELECT
    c.customerName,
    COUNT(o.orderNumber) AS total_orders
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
GROUP BY c.customerName
HAVING COUNT(o.orderNumber) > 1
ORDER BY total_orders DESC;

select * from repeat_customers;

-- repeat customer or customer retention same hote h distinct month same month ko repeat nhi hon dete
CREATE VIEW customer_retention_analysis AS
SELECT
    c.customerName,
    COUNT(DISTINCT MONTH(o.orderDate)) AS active_months
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
GROUP BY c.customerName
HAVING active_months > 1
ORDER BY active_months DESC;

select * from customer_retention_analysis;

-- country wise round digit ko 2 decimal tk round krta h

create view region_wise_sales as
SELECT
    c.country,
    ROUND(SUM(od.quantityOrdered * od.priceEach),2) AS total_sales
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
GROUP BY c.country
ORDER BY total_sales DESC;

select * from region_wise_sales;













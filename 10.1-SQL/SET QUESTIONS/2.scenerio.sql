create database set_New_scenerio;
use set_New_scenerio;

CREATE TABLE salary (
    employee_id INT,
    year INT,
    salary INT
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE
);


CREATE TABLE sales (
    product_id INT,
    month INT,
    sales INT,
    sales_date DATE
);

CREATE TABLE customer (
    customer_id INT,
    name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);


CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(50)
);



INSERT INTO salary VALUES
(1, 2021, 50000),
(1, 2022, 55000),
(1, 2023, 60000),
(2, 2021, 40000),
(2, 2022, 42000),
(2, 2023, 41000),
(3, 2021, 30000),
(3, 2022, 35000),
(3, 2023, 40000);

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 101, DATE_SUB(CURDATE(), INTERVAL 2 MONTH)),
(2, 102, DATE_SUB(CURDATE(), INTERVAL 4 MONTH)),
(3, 103, DATE_SUB(CURDATE(), INTERVAL 8 MONTH)),
(4, 101, DATE_SUB(CURDATE(), INTERVAL 10 MONTH)),
(5, 104, DATE_SUB(CURDATE(), INTERVAL 1 MONTH)),
(6, 105, DATE_SUB(CURDATE(), INTERVAL 7 MONTH));

INSERT INTO sales VALUES
(1, 1, 1000, '2023-01-01'),
(1, 2, 600,  '2023-02-01'),
(2, 1, 800,  '2023-01-01'),
(2, 2, 700,  '2023-02-01'),
(3, 1, 500,  '2023-01-01'),
(3, 2, 900,  '2023-02-01'),
(1, 3, 500,  '2023-03-01'),
(1, 4, 400,  '2023-04-01');


INSERT INTO customer VALUES
(1, 'John', 'john@mail.com', '1111111111'),
(2, 'Jane', 'jane@mail.com', '2222222222'),
(3, 'Jake', 'john@mail.com', '1111111111'),
(4, 'Mary', 'mary@mail.com', '3333333333'),
(5, 'Sam',  'jane@mail.com', '2222222222');


INSERT INTO products VALUES
(1, 'Laptop'),
(2, 'Mobile'),
(3, 'Tablet'),
(4, 'Camera');

Scenario 1: Identify Consistent High Performers
Question: Find employees who have consistently received a salary increase for the past 3 years.

SELECT s1.employee_id
FROM salary s1
JOIN salary s2 
    ON s1.employee_id = s2.employee_id 
    AND s2.year = s1.year + 1
JOIN salary s3 
    ON s2.employee_id = s3.employee_id 
    AND s3.year = s2.year + 1
WHERE s2.salary > s1.salary
  AND s3.salary > s2.salary;

Scenario 2: Customer Retention Analysis
Question: Find customers who made purchases in the last 6 months but not in the previous 6 months.
SELECT DISTINCT customer_id
FROM orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
AND customer_id NOT IN (
    SELECT customer_id
    FROM orders
    WHERE order_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
                          AND DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
);
Scenario 3: Identify Products with Declining Sales
Question: Find products whose sales decreased by more than 30% compared to the previous month

SELECT 
    s1.product_id,
    s1.sales AS current_sales,
    s2.sales AS previous_sales,
    ((s2.sales - s1.sales) * 100.0 / s2.sales) AS decline_percentage
FROM sales s1
JOIN sales s2
    ON s1.product_id = s2.product_id
    AND s1.month = s2.month + 1
WHERE ((s2.sales - s1.sales) * 100.0 / s2.sales) > 30;

Scenario 4: Calculate Moving Average of Sales
Question: Calculate a 3-month moving average for product sales.
SELECT 
    product_id,
    sales_date,
    AVG(sales) OVER (
        PARTITION BY product_id 
        ORDER BY sales_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3_months
FROM sales;
Scenario 5: Detect Duplicate Records
Question: Find all duplicate records from a customer table based on email and phone number
SELECT email, phone, COUNT(*) AS duplicate_count
FROM customer
GROUP BY email, phone
HAVING COUNT(*) > 1;

Scenario 6: Identify Products with No Sales for 3 Consecutive Months
Question: List products that have not had any sales for 3 consecutive months

SELECT DISTINCT p.product_id
FROM products p
LEFT JOIN sales s1 
    ON p.product_id = s1.product_id 
    AND MONTH(s1.sales_date) = MONTH(CURDATE())
LEFT JOIN sales s2 
    ON p.product_id = s2.product_id 
    AND MONTH(s2.sales_date) = MONTH(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
LEFT JOIN sales s3 
    ON p.product_id = s3.product_id 
    AND MONTH(s3.sales_date) = MONTH(DATE_SUB(CURDATE(), INTERVAL 2 MONTH))
WHERE s1.product_id IS NULL
  AND s2.product_id IS NULL
  AND s3.product_id IS NULL;
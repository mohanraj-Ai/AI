use prac_db
create table employers_salary(
employee_id int auto_increment primary key,
employee_name varchar(50) not null,
salary int
);
SELECT * FROM employers_salary
insert into employers_salary (employee_name,salary)
values 
('mohan',25000),
('raj',56500),
('vishal',65000),
('raju',50000);
select employee_name
from employers_salary 
where salary>(select avg(salary) from employers_salary);
Scenario 2: Customer Orders without Matching Records
Question:
 Retrieve a list of customer names who have not placed any orders

select * from customers_orders
create table customers_orders(
customer_id int auto_increment primary key,
customer_name varchar(50) not null
);
insert into customers_orders (customer_name)
values 
('mohan'),
('raj'),
('vishal'),
('raju');

create table orderss(
order_id int,
customer_id int,
foreign key(customer_id) references customers_orders(customer_id)
);
insert into orderss (order_id,customer_id)
values 
(101,1),
(102,1),
(103,2),
(104,3);
select customer_name
from customers_orders
left join orderss
on customers_orders.customer_id=orderss.customer_id
WHERE orderss.customer_id IS NULL;

Scenario 3: Product Sales Summary
Question:
 Display the total sales amount for each product.
select * from sales
create table products_sales(
order_id int auto_increment primary key,
product varchar(50) not null,
sales int
);
insert into
 products_sales(product,sales)
values
('tv',50000),
('tv',10000),
('ac',5000),
('ac',32222),
('fridge',100000);
select product,sum(sales) as total_sales
from products_sales
group by product;
Scenario 4: Department-Wise Employee Count
Question:
 List each department name with the number of employees working in it.
select * from employees
SELECT 
    d.department_name, 
    COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
Scenario 5: Top 3 Highest Sales
Question:
 Find the top 3 highest sales transactions

elect * from sales
SELECT *
FROM sales
ORDER BY amount DESC
LIMIT 3;
select * from employees
Scenario 6: Calculate Employee Salary Ranks by Department
Question:
 Write a query to display each employee’s name, department name, salary, and their salary rank within their respective department.
SELECT 
    e.name,
    d.department_name,
    e.salary,
    RANK() OVER (PARTITION BY d.department_name ORDER BY e.salary DESC) AS salary_rank
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;
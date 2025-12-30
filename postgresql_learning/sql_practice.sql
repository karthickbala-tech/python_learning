/* =====================================================
   DAY 1 – DATABASE & TABLES
   ===================================================== */

-- Create database
CREATE DATABASE myDB;

-- Use database
USE myDB;

-- -----------------------------------------------------
-- Create employees table
-- -----------------------------------------------------
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5,2),
    hire_date DATE
);

-- View table
SELECT * FROM employees;

-- Rename table
RENAME TABLE employees TO workers;

-- Rename back
RENAME TABLE workers TO employees;

-- Add column
ALTER TABLE employees
ADD phone_number VARCHAR(15);

-- Rename column
ALTER TABLE employees
RENAME COLUMN phone_number TO email;

-- Modify column size
ALTER TABLE employees
MODIFY email VARCHAR(100);

-- Change column position (MySQL only)
ALTER TABLE employees
MODIFY email VARCHAR(100) AFTER last_name;

-- Drop column
ALTER TABLE employees
DROP COLUMN email;


/* =====================================================
   DAY 2 – INSERT & SELECT
   ===================================================== */

-- Insert single row
INSERT INTO employees
VALUES (1, 'Eugene', 'Krabs', 25.50, '2023-01-02');

-- Insert multiple rows
INSERT INTO employees
VALUES
(2, 'Spongebob', 'Squarepants', 12.50, '2023-01-04'),
(3, 'Patrick', 'Star', 12.50, '2023-01-05'),
(4, 'Sandy', 'Cheeks', 17.50, '2023-01-06'),
(5, 'Squidward', 'Tentacles', 15.00, '2023-01-06');

-- Insert specific columns
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (6, 'Sheldon', 'Plankton');

-- Select all
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name FROM employees;

-- WHERE conditions
SELECT * FROM employees WHERE employee_id = 3;
SELECT * FROM employees WHERE hourly_pay >= 15;
SELECT * FROM employees WHERE hire_date IS NULL;
SELECT * FROM employees WHERE hire_date IS NOT NULL;


/* =====================================================
   DAY 3 – UPDATE & DELETE
   ===================================================== */

-- Update one column
UPDATE employees
SET hourly_pay = 10.25
WHERE employee_id = 6;

-- Update multiple columns
UPDATE employees
SET hourly_pay = 10.25,
    hire_date = '2023-01-07'
WHERE employee_id = 6;

-- Set column to NULL
UPDATE employees
SET hourly_pay = NULL
WHERE employee_id = 6;

-- Update all rows
UPDATE employees
SET hourly_pay = 10.25;

-- Delete specific row
DELETE FROM employees
WHERE employee_id = 6;

-- Delete all rows (structure remains)
DELETE FROM employees;


/* =====================================================
   TRANSACTIONS – AUTOCOMMIT / COMMIT / ROLLBACK
   ===================================================== */

-- MySQL
SET AUTOCOMMIT = 0;

-- PostgreSQL
-- BEGIN;

COMMIT;

UPDATE employees
SET first_name = 'Eugenes'
WHERE employee_id = 1;

ROLLBACK;


/* =====================================================
   DATE & TIME
   ===================================================== */

CREATE TABLE test (
    my_date DATE,
    my_time TIME,
    my_datetime DATETIME
);

INSERT INTO test
VALUES (CURRENT_DATE(), CURRENT_TIME(), NOW());

INSERT INTO test
VALUES (CURRENT_DATE() + INTERVAL 1 DAY, NULL, NULL);

INSERT INTO test
VALUES (CURRENT_DATE() - INTERVAL 1 DAY, NULL, NULL);

SELECT * FROM test;


/* =====================================================
   CONSTRAINTS
   ===================================================== */

-- UNIQUE
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(25) UNIQUE,
    price DECIMAL(4,2)
);

-- NOT NULL
ALTER TABLE products
MODIFY price DECIMAL(4,2) NOT NULL;

-- CHECK
ALTER TABLE employees
ADD CONSTRAINT chk_hourly_pay CHECK (hourly_pay >= 10);

-- DEFAULT
ALTER TABLE products
ALTER price SET DEFAULT 0;


/* =====================================================
   PRIMARY KEY & AUTO INCREMENT
   ===================================================== */

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5,2)
);

INSERT INTO transactions (amount)
VALUES (4.99), (3.97), (7.88);

-- Start AUTO_INCREMENT from 1000
ALTER TABLE transactions AUTO_INCREMENT = 1000;


/* =====================================================
   FOREIGN KEY & JOINS
   ===================================================== */

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

INSERT INTO customers (first_name, last_name)
VALUES ('Fred', 'Fish'),
       ('Larry', 'Lobster'),
       ('Bubble', 'Bass');

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- INNER JOIN
SELECT *
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;

-- LEFT JOIN
SELECT *
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.customer_id;

-- RIGHT JOIN
SELECT *
FROM orders
RIGHT JOIN customers
ON orders.customer_id = customers.customer_id;

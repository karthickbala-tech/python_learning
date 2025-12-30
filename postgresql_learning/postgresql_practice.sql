-- Create database
CREATE DATABASE mydb;

-- Connect to database (VS Code auto-connects, pgAdmin needs this)
-- \c mydb


-- Create employees table
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5,2),
    hire_date DATE
);

SELECT * FROM employees;

-- ALTER TABLE OPERATIONS

-- Add column
ALTER TABLE employees
ADD COLUMN email VARCHAR(100);

-- Rename column
ALTER TABLE employees
RENAME COLUMN email TO contact_email;

-- Modify column size
ALTER TABLE employees
ALTER COLUMN contact_email TYPE VARCHAR(150);

-- Drop column
ALTER TABLE employees
DROP COLUMN contact_email;

-- INSERTING ROWS

INSERT INTO employees
VALUES (1, 'Eugene', 'Krabs', 25.50, '2023-01-02');

INSERT INTO employees
VALUES
(2, 'Spongebob', 'Squarepants', 12.50, '2023-01-04'),
(3, 'Patrick', 'Star', 12.50, '2023-01-05'),
(4, 'Sandy', 'Cheeks', 17.50, '2023-01-06'),
(5, 'Squidward', 'Tentacles', 15.00, '2023-01-06');

-- Insert into specific columns
INSERT INTO employees (employee_id, first_name, last_name)
VALUES (6, 'Sheldon', 'Plankton');

SELECT * FROM employees;

-- SELECT & WHERE

SELECT * FROM employees;

SELECT first_name, last_name FROM employees;

SELECT * FROM employees
WHERE employee_id = 3;

SELECT * FROM employees
WHERE hourly_pay >= 15;

SELECT * FROM employees
WHERE hire_date IS NULL;

SELECT * FROM employees
WHERE hire_date IS NOT NULL;

--UPDATE & DELETE

UPDATE employees
SET hourly_pay = 10.25
WHERE employee_id = 6;

UPDATE employees
SET hourly_pay = 10.25,
    hire_date = '2023-01-07'
WHERE employee_id = 6;

UPDATE employees
SET hourly_pay = NULL
WHERE employee_id = 6;

DELETE FROM employees
WHERE employee_id = 6;

-- TRANSACTIONS (COMMIT & ROLLBACK)

BEGIN;

UPDATE employees
SET first_name = 'Eugenes'
WHERE employee_id = 1;

-- Undo changes
ROLLBACK;

-- OR save changes
-- COMMIT;

--DATE & TIME (PostgreSQL)

CREATE TABLE test (
    my_date DATE,
    my_time TIME,
    my_timestamp TIMESTAMP
);

INSERT INTO test
VALUES (CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP);

INSERT INTO test
VALUES (CURRENT_DATE + INTERVAL '1 day', NULL, NULL);

INSERT INTO test
VALUES (CURRENT_DATE - INTERVAL '1 day', NULL, NULL);

SELECT * FROM test;

--CONSTRAINTS  

--UNIQUE
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(25) UNIQUE,
    price DECIMAL(4,2)
);

--NOT NULL
ALTER TABLE products
ALTER COLUMN price SET NOT NULL;

--CHECK
ALTER TABLE employees
ADD CONSTRAINT chk_hourly_pay CHECK (hourly_pay >= 10);

--DEFAULT
ALTER TABLE products
ALTER COLUMN price SET DEFAULT 0;

--PRIMARY KEY & AUTO INCREMENT (PostgreSQL WAY
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    amount DECIMAL(5,2)
);

INSERT INTO transactions (amount)
VALUES (4.99), (3.97), (7.88);

SELECT * FROM transactions;

--FOREIGN KEY
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

INSERT INTO customers (first_name, last_name)
VALUES
('Fred', 'Fish'),
('Larry', 'Lobster'),
('Bubble', 'Bass');

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    amount DECIMAL(5,2),
    customer_id INT,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

--JOINS

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

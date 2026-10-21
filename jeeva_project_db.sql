-- =========================================
-- BOOK STORE MANAGEMENT SYSTEM
-- MySQL Database
-- =========================================

CREATE DATABASE jeeva_project;

USE jeeva_project;


-- =========================================
-- 1. CATEGORIES TABLE
-- =========================================

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL
);


-- =========================================
-- 2. CUSTOMERS TABLE
-- =========================================

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(200)
);


-- =========================================
-- 3. BOOKS TABLE
-- =========================================

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,

    FOREIGN KEY (category_id)
    REFERENCES categories(category_id)
);


-- =========================================
-- 4. ORDERS TABLE
-- =========================================

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);


-- =========================================
-- 5. ORDER DETAILS TABLE
-- =========================================

CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    FOREIGN KEY (book_id)
    REFERENCES books(book_id)
);
USE book_store_management;

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(150) NOT NULL,
    phone VARCHAR(25),
    email VARCHAR(150),
    address VARCHAR(300),
    joining_date DATE,
    salary DECIMAL(10,2)
);
-- Sample data only (no CREATE TABLE statements).
-- 40 customers, 40 books, 40 orders, and 40 order_details.
-- Assumes these columns from the provided reference:
-- categories(category_id, category_name)
-- customers(customer_id, customer_name, phone, email, address)
-- books(book_id, title, author, category_id, price, stock)
-- orders(order_id, customer_id, order_date, total_amount)
-- order_details(order_detail_id, order_id, book_id, quantity, price)

INSERT INTO categories (category_name) VALUES
  ('Fiction'),
  ('Education'),
  ('Technology'),
  ('Biography'),
  ('Comics');

INSERT INTO customers (customer_name, phone, email, address) VALUES
  ('Rahul Kumar', '9876500001', 'customer01@example.com', '1 Main Road, Chennai'),
  ('Priya Sharma', '9876500002', 'customer02@example.com', '2 Main Road, Bangalore'),
  ('Arun Raj', '9876500003', 'customer03@example.com', '3 Main Road, Coimbatore'),
  ('Anitha Devi', '9876500004', 'customer04@example.com', '4 Main Road, Madurai'),
  ('Kavin Rajan', '9876500005', 'customer05@example.com', '5 Main Road, Salem'),
  ('Nila Nair', '9876500006', 'customer06@example.com', '6 Main Road, Chennai'),
  ('Sanjay Patel', '9876500007', 'customer07@example.com', '7 Main Road, Bangalore'),
  ('Meena Iyer', '9876500008', 'customer08@example.com', '8 Main Road, Coimbatore'),
  ('Vignesh Kumar', '9876500009', 'customer09@example.com', '9 Main Road, Madurai'),
  ('Divya Sharma', '9876500010', 'customer10@example.com', '10 Main Road, Salem'),
  ('Hari Raj', '9876500011', 'customer11@example.com', '11 Main Road, Chennai'),
  ('Kavitha Devi', '9876500012', 'customer12@example.com', '12 Main Road, Bangalore'),
  ('Manoj Rajan', '9876500013', 'customer13@example.com', '13 Main Road, Coimbatore'),
  ('Lakshmi Nair', '9876500014', 'customer14@example.com', '14 Main Road, Madurai'),
  ('Naveen Patel', '9876500015', 'customer15@example.com', '15 Main Road, Salem'),
  ('Janani Iyer', '9876500016', 'customer16@example.com', '16 Main Road, Chennai'),
  ('Surya Kumar', '9876500017', 'customer17@example.com', '17 Main Road, Bangalore'),
  ('Deepa Sharma', '9876500018', 'customer18@example.com', '18 Main Road, Coimbatore'),
  ('Ajay Raj', '9876500019', 'customer19@example.com', '19 Main Road, Madurai'),
  ('Swetha Devi', '9876500020', 'customer20@example.com', '20 Main Road, Salem'),
  ('Karthik Rajan', '9876500021', 'customer21@example.com', '21 Main Road, Chennai'),
  ('Ramya Nair', '9876500022', 'customer22@example.com', '22 Main Road, Bangalore'),
  ('Gokul Patel', '9876500023', 'customer23@example.com', '23 Main Road, Coimbatore'),
  ('Harini Iyer', '9876500024', 'customer24@example.com', '24 Main Road, Madurai'),
  ('Bala Kumar', '9876500025', 'customer25@example.com', '25 Main Road, Salem'),
  ('Keerthana Sharma', '9876500026', 'customer26@example.com', '26 Main Road, Chennai'),
  ('Prakash Raj', '9876500027', 'customer27@example.com', '27 Main Road, Bangalore'),
  ('Revathi Devi', '9876500028', 'customer28@example.com', '28 Main Road, Coimbatore'),
  ('Dinesh Rajan', '9876500029', 'customer29@example.com', '29 Main Road, Madurai'),
  ('Pavithra Nair', '9876500030', 'customer30@example.com', '30 Main Road, Salem'),
  ('Ashwin Patel', '9876500031', 'customer31@example.com', '31 Main Road, Chennai'),
  ('Sneha Iyer', '9876500032', 'customer32@example.com', '32 Main Road, Bangalore'),
  ('Vijay Kumar', '9876500033', 'customer33@example.com', '33 Main Road, Coimbatore'),
  ('Yazhini Sharma', '9876500034', 'customer34@example.com', '34 Main Road, Madurai'),
  ('Ramesh Raj', '9876500035', 'customer35@example.com', '35 Main Road, Salem'),
  ('Bhavani Devi', '9876500036', 'customer36@example.com', '36 Main Road, Chennai'),
  ('Kishore Rajan', '9876500037', 'customer37@example.com', '37 Main Road, Bangalore'),
  ('Aishwarya Nair', '9876500038', 'customer38@example.com', '38 Main Road, Coimbatore'),
  ('Santhosh Patel', '9876500039', 'customer39@example.com', '39 Main Road, Madurai');

INSERT INTO books (title, author, category_id, price, stock)
SELECT d.title, d.author, c.category_id, d.price, d.stock
FROM (
  SELECT 'The Alchemist' AS title, 'Paulo Coelho' AS author, 'Fiction' AS category_name, 228 AS price, 15 AS stock
  UNION ALL
  SELECT 'Database Management Systems' AS title, 'Raghu Ramakrishnan' AS author, 'Education' AS category_name, 257 AS price, 22 AS stock
  UNION ALL
  SELECT 'Python Programming' AS title, 'Mark Lutz' AS author, 'Technology' AS category_name, 286 AS price, 29 AS stock
  UNION ALL
  SELECT 'Wings of Fire' AS title, 'A.P.J. Abdul Kalam' AS author, 'Biography' AS category_name, 315 AS price, 36 AS stock
  UNION ALL
  SELECT 'The Adventures of Tintin' AS title, 'Herge' AS author, 'Comics' AS category_name, 344 AS price, 43 AS stock
  UNION ALL
  SELECT 'Atomic Habits' AS title, 'James Clear' AS author, 'Fiction' AS category_name, 373 AS price, 50 AS stock
  UNION ALL
  SELECT 'Introduction to Algorithms' AS title, 'Thomas H. Cormen' AS author, 'Education' AS category_name, 402 AS price, 14 AS stock
  UNION ALL
  SELECT 'The God of Small Things' AS title, 'Arundhati Roy' AS author, 'Technology' AS category_name, 431 AS price, 21 AS stock
  UNION ALL
  SELECT 'Rich Dad Poor Dad' AS title, 'Robert Kiyosaki' AS author, 'Biography' AS category_name, 460 AS price, 28 AS stock
  UNION ALL
  SELECT 'The Hobbit' AS title, 'J.R.R. Tolkien' AS author, 'Comics' AS category_name, 489 AS price, 35 AS stock
  UNION ALL
  SELECT 'Clean Code' AS title, 'Paulo Coelho' AS author, 'Fiction' AS category_name, 518 AS price, 42 AS stock
  UNION ALL
  SELECT 'A Brief History of Time' AS title, 'Raghu Ramakrishnan' AS author, 'Education' AS category_name, 547 AS price, 49 AS stock
  UNION ALL
  SELECT 'The White Tiger' AS title, 'Mark Lutz' AS author, 'Technology' AS category_name, 576 AS price, 13 AS stock
  UNION ALL
  SELECT 'Head First Java' AS title, 'A.P.J. Abdul Kalam' AS author, 'Biography' AS category_name, 605 AS price, 20 AS stock
  UNION ALL
  SELECT 'Sapiens' AS title, 'Herge' AS author, 'Comics' AS category_name, 634 AS price, 27 AS stock
  UNION ALL
  SELECT 'The Jungle Book' AS title, 'James Clear' AS author, 'Fiction' AS category_name, 663 AS price, 34 AS stock
  UNION ALL
  SELECT 'Deep Work' AS title, 'Thomas H. Cormen' AS author, 'Education' AS category_name, 692 AS price, 41 AS stock
  UNION ALL
  SELECT 'Computer Networks' AS title, 'Arundhati Roy' AS author, 'Technology' AS category_name, 721 AS price, 48 AS stock
  UNION ALL
  SELECT 'Ponniyin Selvan' AS title, 'Robert Kiyosaki' AS author, 'Biography' AS category_name, 750 AS price, 12 AS stock
  UNION ALL
  SELECT 'The Little Prince' AS title, 'J.R.R. Tolkien' AS author, 'Comics' AS category_name, 779 AS price, 19 AS stock
  UNION ALL
  SELECT 'Think and Grow Rich' AS title, 'Paulo Coelho' AS author, 'Fiction' AS category_name, 207 AS price, 26 AS stock
  UNION ALL
  SELECT 'Operating System Concepts' AS title, 'Raghu Ramakrishnan' AS author, 'Education' AS category_name, 236 AS price, 33 AS stock
  UNION ALL
  SELECT 'The Book Thief' AS title, 'Mark Lutz' AS author, 'Technology' AS category_name, 265 AS price, 40 AS stock
  UNION ALL
  SELECT 'C Programming Language' AS title, 'A.P.J. Abdul Kalam' AS author, 'Biography' AS category_name, 294 AS price, 47 AS stock
  UNION ALL
  SELECT 'Ikigai' AS title, 'Herge' AS author, 'Comics' AS category_name, 323 AS price, 11 AS stock
  UNION ALL
  SELECT 'The Martian' AS title, 'James Clear' AS author, 'Fiction' AS category_name, 352 AS price, 18 AS stock
  UNION ALL
  SELECT 'Harry Potter and the Philosopher’s Stone' AS title, 'Thomas H. Cormen' AS author, 'Education' AS category_name, 381 AS price, 25 AS stock
  UNION ALL
  SELECT 'Learning SQL' AS title, 'Arundhati Roy' AS author, 'Technology' AS category_name, 410 AS price, 32 AS stock
  UNION ALL
  SELECT 'The Discovery of India' AS title, 'Robert Kiyosaki' AS author, 'Biography' AS category_name, 439 AS price, 39 AS stock
  UNION ALL
  SELECT 'Data Structures in C' AS title, 'J.R.R. Tolkien' AS author, 'Comics' AS category_name, 468 AS price, 46 AS stock
  UNION ALL
  SELECT 'The Secret Garden' AS title, 'Paulo Coelho' AS author, 'Fiction' AS category_name, 497 AS price, 10 AS stock
  UNION ALL
  SELECT 'Artificial Intelligence Basics' AS title, 'Raghu Ramakrishnan' AS author, 'Education' AS category_name, 526 AS price, 17 AS stock
  UNION ALL
  SELECT 'The Guide' AS title, 'Mark Lutz' AS author, 'Technology' AS category_name, 555 AS price, 24 AS stock
  UNION ALL
  SELECT 'JavaScript: The Good Parts' AS title, 'A.P.J. Abdul Kalam' AS author, 'Biography' AS category_name, 584 AS price, 31 AS stock
  UNION ALL
  SELECT 'Malgudi Days' AS title, 'Herge' AS author, 'Comics' AS category_name, 613 AS price, 38 AS stock
  UNION ALL
  SELECT 'Cloud Computing' AS title, 'James Clear' AS author, 'Fiction' AS category_name, 642 AS price, 45 AS stock
  UNION ALL
  SELECT 'The Diary of a Young Girl' AS title, 'Thomas H. Cormen' AS author, 'Education' AS category_name, 671 AS price, 9 AS stock
  UNION ALL
  SELECT 'Effective Python' AS title, 'Arundhati Roy' AS author, 'Technology' AS category_name, 700 AS price, 16 AS stock
  UNION ALL
  SELECT 'The Blue Umbrella' AS title, 'Robert Kiyosaki' AS author, 'Biography' AS category_name, 729 AS price, 23 AS stock
  UNION ALL
  SELECT 'Design Patterns' AS title, 'J.R.R. Tolkien' AS author, 'Comics' AS category_name, 758 AS price, 30 AS stock
) AS d
JOIN categories c ON c.category_name = d.category_name;

INSERT INTO orders (customer_id, order_date, total_amount)
SELECT c.customer_id, d.order_date, d.total_amount
FROM (
  SELECT 'Rahul Kumar' AS customer_name, 'customer01@example.com' AS email, '2026-01-03' AS order_date, 456 AS total_amount
  UNION ALL
  SELECT 'Priya Sharma' AS customer_name, 'customer02@example.com' AS email, '2026-02-06' AS order_date, 771 AS total_amount
  UNION ALL
  SELECT 'Arun Raj' AS customer_name, 'customer03@example.com' AS email, '2026-03-09' AS order_date, 286 AS total_amount
  UNION ALL
  SELECT 'Anitha Devi' AS customer_name, 'customer04@example.com' AS email, '2026-04-12' AS order_date, 630 AS total_amount
  UNION ALL
  SELECT 'Kavin Rajan' AS customer_name, 'customer05@example.com' AS email, '2026-05-15' AS order_date, 1032 AS total_amount
  UNION ALL
  SELECT 'Nila Nair' AS customer_name, 'customer06@example.com' AS email, '2026-06-18' AS order_date, 373 AS total_amount
  UNION ALL
  SELECT 'Sanjay Patel' AS customer_name, 'customer07@example.com' AS email, '2026-07-21' AS order_date, 804 AS total_amount
  UNION ALL
  SELECT 'Meena Iyer' AS customer_name, 'customer08@example.com' AS email, '2026-08-24' AS order_date, 1293 AS total_amount
  UNION ALL
  SELECT 'Vignesh Kumar' AS customer_name, 'customer09@example.com' AS email, '2026-09-27' AS order_date, 460 AS total_amount
  UNION ALL
  SELECT 'Divya Sharma' AS customer_name, 'customer10@example.com' AS email, '2026-01-02' AS order_date, 978 AS total_amount
  UNION ALL
  SELECT 'Hari Raj' AS customer_name, 'customer11@example.com' AS email, '2026-02-05' AS order_date, 1554 AS total_amount
  UNION ALL
  SELECT 'Kavitha Devi' AS customer_name, 'customer12@example.com' AS email, '2026-03-08' AS order_date, 547 AS total_amount
  UNION ALL
  SELECT 'Manoj Rajan' AS customer_name, 'customer13@example.com' AS email, '2026-04-11' AS order_date, 1152 AS total_amount
  UNION ALL
  SELECT 'Lakshmi Nair' AS customer_name, 'customer14@example.com' AS email, '2026-05-14' AS order_date, 1815 AS total_amount
  UNION ALL
  SELECT 'Naveen Patel' AS customer_name, 'customer15@example.com' AS email, '2026-06-17' AS order_date, 634 AS total_amount
  UNION ALL
  SELECT 'Janani Iyer' AS customer_name, 'customer16@example.com' AS email, '2026-07-20' AS order_date, 1326 AS total_amount
  UNION ALL
  SELECT 'Surya Kumar' AS customer_name, 'customer17@example.com' AS email, '2026-08-23' AS order_date, 2076 AS total_amount
  UNION ALL
  SELECT 'Deepa Sharma' AS customer_name, 'customer18@example.com' AS email, '2026-09-26' AS order_date, 721 AS total_amount
  UNION ALL
  SELECT 'Ajay Raj' AS customer_name, 'customer19@example.com' AS email, '2026-01-01' AS order_date, 1500 AS total_amount
  UNION ALL
  SELECT 'Swetha Devi' AS customer_name, 'customer20@example.com' AS email, '2026-02-04' AS order_date, 2337 AS total_amount
  UNION ALL
  SELECT 'Karthik Rajan' AS customer_name, 'customer21@example.com' AS email, '2026-03-07' AS order_date, 207 AS total_amount
  UNION ALL
  SELECT 'Ramya Nair' AS customer_name, 'customer22@example.com' AS email, '2026-04-10' AS order_date, 472 AS total_amount
  UNION ALL
  SELECT 'Gokul Patel' AS customer_name, 'customer23@example.com' AS email, '2026-05-13' AS order_date, 795 AS total_amount
  UNION ALL
  SELECT 'Harini Iyer' AS customer_name, 'customer24@example.com' AS email, '2026-06-16' AS order_date, 294 AS total_amount
  UNION ALL
  SELECT 'Bala Kumar' AS customer_name, 'customer25@example.com' AS email, '2026-07-19' AS order_date, 646 AS total_amount
  UNION ALL
  SELECT 'Keerthana Sharma' AS customer_name, 'customer26@example.com' AS email, '2026-08-22' AS order_date, 1056 AS total_amount
  UNION ALL
  SELECT 'Prakash Raj' AS customer_name, 'customer27@example.com' AS email, '2026-09-25' AS order_date, 381 AS total_amount
  UNION ALL
  SELECT 'Revathi Devi' AS customer_name, 'customer28@example.com' AS email, '2026-01-28' AS order_date, 820 AS total_amount
  UNION ALL
  SELECT 'Dinesh Rajan' AS customer_name, 'customer29@example.com' AS email, '2026-02-03' AS order_date, 1317 AS total_amount
  UNION ALL
  SELECT 'Pavithra Nair' AS customer_name, 'customer30@example.com' AS email, '2026-03-06' AS order_date, 468 AS total_amount
  UNION ALL
  SELECT 'Ashwin Patel' AS customer_name, 'customer31@example.com' AS email, '2026-04-09' AS order_date, 994 AS total_amount
  UNION ALL
  SELECT 'Sneha Iyer' AS customer_name, 'customer32@example.com' AS email, '2026-05-12' AS order_date, 1578 AS total_amount
  UNION ALL
  SELECT 'Vijay Kumar' AS customer_name, 'customer33@example.com' AS email, '2026-06-15' AS order_date, 555 AS total_amount
  UNION ALL
  SELECT 'Yazhini Sharma' AS customer_name, 'customer34@example.com' AS email, '2026-07-18' AS order_date, 1168 AS total_amount
  UNION ALL
  SELECT 'Ramesh Raj' AS customer_name, 'customer35@example.com' AS email, '2026-08-21' AS order_date, 1839 AS total_amount
  UNION ALL
  SELECT 'Bhavani Devi' AS customer_name, 'customer36@example.com' AS email, '2026-09-24' AS order_date, 642 AS total_amount
  UNION ALL
  SELECT 'Kishore Rajan' AS customer_name, 'customer37@example.com' AS email, '2026-01-27' AS order_date, 1342 AS total_amount
  UNION ALL
  SELECT 'Aishwarya Nair' AS customer_name, 'customer38@example.com' AS email, '2026-02-02' AS order_date, 2100 AS total_amount
  UNION ALL
  SELECT 'Santhosh Patel' AS customer_name, 'customer39@example.com' AS email, '2026-03-05' AS order_date, 729 AS total_amount
) AS d
JOIN customers c ON c.customer_name = d.customer_name AND c.email = d.email;

INSERT INTO order_details (order_id, book_id, quantity, price)
SELECT o.order_id, b.book_id, d.quantity, d.price
FROM (
  SELECT 'Rahul Kumar' AS customer_name, 'customer01@example.com' AS email, '2026-01-03' AS order_date, 'The Alchemist' AS title, 2 AS quantity, 228 AS price
  UNION ALL
  SELECT 'Priya Sharma' AS customer_name, 'customer02@example.com' AS email, '2026-02-06' AS order_date, 'Database Management Systems' AS title, 3 AS quantity, 257 AS price
  UNION ALL
  SELECT 'Arun Raj' AS customer_name, 'customer03@example.com' AS email, '2026-03-09' AS order_date, 'Python Programming' AS title, 1 AS quantity, 286 AS price
  UNION ALL
  SELECT 'Anitha Devi' AS customer_name, 'customer04@example.com' AS email, '2026-04-12' AS order_date, 'Wings of Fire' AS title, 2 AS quantity, 315 AS price
  UNION ALL
  SELECT 'Kavin Rajan' AS customer_name, 'customer05@example.com' AS email, '2026-05-15' AS order_date, 'The Adventures of Tintin' AS title, 3 AS quantity, 344 AS price
  UNION ALL
  SELECT 'Nila Nair' AS customer_name, 'customer06@example.com' AS email, '2026-06-18' AS order_date, 'Atomic Habits' AS title, 1 AS quantity, 373 AS price
  UNION ALL
  SELECT 'Sanjay Patel' AS customer_name, 'customer07@example.com' AS email, '2026-07-21' AS order_date, 'Introduction to Algorithms' AS title, 2 AS quantity, 402 AS price
  UNION ALL
  SELECT 'Meena Iyer' AS customer_name, 'customer08@example.com' AS email, '2026-08-24' AS order_date, 'The God of Small Things' AS title, 3 AS quantity, 431 AS price
  UNION ALL
  SELECT 'Vignesh Kumar' AS customer_name, 'customer09@example.com' AS email, '2026-09-27' AS order_date, 'Rich Dad Poor Dad' AS title, 1 AS quantity, 460 AS price
  UNION ALL
  SELECT 'Divya Sharma' AS customer_name, 'customer10@example.com' AS email, '2026-01-02' AS order_date, 'The Hobbit' AS title, 2 AS quantity, 489 AS price
  UNION ALL
  SELECT 'Hari Raj' AS customer_name, 'customer11@example.com' AS email, '2026-02-05' AS order_date, 'Clean Code' AS title, 3 AS quantity, 518 AS price
  UNION ALL
  SELECT 'Kavitha Devi' AS customer_name, 'customer12@example.com' AS email, '2026-03-08' AS order_date, 'A Brief History of Time' AS title, 1 AS quantity, 547 AS price
  UNION ALL
  SELECT 'Manoj Rajan' AS customer_name, 'customer13@example.com' AS email, '2026-04-11' AS order_date, 'The White Tiger' AS title, 2 AS quantity, 576 AS price
  UNION ALL
  SELECT 'Lakshmi Nair' AS customer_name, 'customer14@example.com' AS email, '2026-05-14' AS order_date, 'Head First Java' AS title, 3 AS quantity, 605 AS price
  UNION ALL
  SELECT 'Naveen Patel' AS customer_name, 'customer15@example.com' AS email, '2026-06-17' AS order_date, 'Sapiens' AS title, 1 AS quantity, 634 AS price
  UNION ALL
  SELECT 'Janani Iyer' AS customer_name, 'customer16@example.com' AS email, '2026-07-20' AS order_date, 'The Jungle Book' AS title, 2 AS quantity, 663 AS price
  UNION ALL
  SELECT 'Surya Kumar' AS customer_name, 'customer17@example.com' AS email, '2026-08-23' AS order_date, 'Deep Work' AS title, 3 AS quantity, 692 AS price
  UNION ALL
  SELECT 'Deepa Sharma' AS customer_name, 'customer18@example.com' AS email, '2026-09-26' AS order_date, 'Computer Networks' AS title, 1 AS quantity, 721 AS price
  UNION ALL
  SELECT 'Ajay Raj' AS customer_name, 'customer19@example.com' AS email, '2026-01-01' AS order_date, 'Ponniyin Selvan' AS title, 2 AS quantity, 750 AS price
  UNION ALL
  SELECT 'Swetha Devi' AS customer_name, 'customer20@example.com' AS email, '2026-02-04' AS order_date, 'The Little Prince' AS title, 3 AS quantity, 779 AS price
  UNION ALL
  SELECT 'Karthik Rajan' AS customer_name, 'customer21@example.com' AS email, '2026-03-07' AS order_date, 'Think and Grow Rich' AS title, 1 AS quantity, 207 AS price
  UNION ALL
  SELECT 'Ramya Nair' AS customer_name, 'customer22@example.com' AS email, '2026-04-10' AS order_date, 'Operating System Concepts' AS title, 2 AS quantity, 236 AS price
  UNION ALL
  SELECT 'Gokul Patel' AS customer_name, 'customer23@example.com' AS email, '2026-05-13' AS order_date, 'The Book Thief' AS title, 3 AS quantity, 265 AS price
  UNION ALL
  SELECT 'Harini Iyer' AS customer_name, 'customer24@example.com' AS email, '2026-06-16' AS order_date, 'C Programming Language' AS title, 1 AS quantity, 294 AS price
  UNION ALL
  SELECT 'Bala Kumar' AS customer_name, 'customer25@example.com' AS email, '2026-07-19' AS order_date, 'Ikigai' AS title, 2 AS quantity, 323 AS price
  UNION ALL
  SELECT 'Keerthana Sharma' AS customer_name, 'customer26@example.com' AS email, '2026-08-22' AS order_date, 'The Martian' AS title, 3 AS quantity, 352 AS price
  UNION ALL
  SELECT 'Prakash Raj' AS customer_name, 'customer27@example.com' AS email, '2026-09-25' AS order_date, 'Harry Potter and the Philosopher’s Stone' AS title, 1 AS quantity, 381 AS price
  UNION ALL
  SELECT 'Revathi Devi' AS customer_name, 'customer28@example.com' AS email, '2026-01-28' AS order_date, 'Learning SQL' AS title, 2 AS quantity, 410 AS price
  UNION ALL
  SELECT 'Dinesh Rajan' AS customer_name, 'customer29@example.com' AS email, '2026-02-03' AS order_date, 'The Discovery of India' AS title, 3 AS quantity, 439 AS price
  UNION ALL
  SELECT 'Pavithra Nair' AS customer_name, 'customer30@example.com' AS email, '2026-03-06' AS order_date, 'Data Structures in C' AS title, 1 AS quantity, 468 AS price
  UNION ALL
  SELECT 'Ashwin Patel' AS customer_name, 'customer31@example.com' AS email, '2026-04-09' AS order_date, 'The Secret Garden' AS title, 2 AS quantity, 497 AS price
  UNION ALL
  SELECT 'Sneha Iyer' AS customer_name, 'customer32@example.com' AS email, '2026-05-12' AS order_date, 'Artificial Intelligence Basics' AS title, 3 AS quantity, 526 AS price
  UNION ALL
  SELECT 'Vijay Kumar' AS customer_name, 'customer33@example.com' AS email, '2026-06-15' AS order_date, 'The Guide' AS title, 1 AS quantity, 555 AS price
  UNION ALL
  SELECT 'Yazhini Sharma' AS customer_name, 'customer34@example.com' AS email, '2026-07-18' AS order_date, 'JavaScript: The Good Parts' AS title, 2 AS quantity, 584 AS price
  UNION ALL
  SELECT 'Ramesh Raj' AS customer_name, 'customer35@example.com' AS email, '2026-08-21' AS order_date, 'Malgudi Days' AS title, 3 AS quantity, 613 AS price
  UNION ALL
  SELECT 'Bhavani Devi' AS customer_name, 'customer36@example.com' AS email, '2026-09-24' AS order_date, 'Cloud Computing' AS title, 1 AS quantity, 642 AS price
  UNION ALL
  SELECT 'Kishore Rajan' AS customer_name, 'customer37@example.com' AS email, '2026-01-27' AS order_date, 'The Diary of a Young Girl' AS title, 2 AS quantity, 671 AS price
  UNION ALL
  SELECT 'Aishwarya Nair' AS customer_name, 'customer38@example.com' AS email, '2026-02-02' AS order_date, 'Effective Python' AS title, 3 AS quantity, 700 AS price
  UNION ALL
  SELECT 'Santhosh Patel' AS customer_name, 'customer39@example.com' AS email, '2026-03-05' AS order_date, 'The Blue Umbrella' AS title, 1 AS quantity, 729 AS price
) AS d
JOIN customers c ON c.customer_name = d.customer_name AND c.email = d.email
JOIN orders o ON o.customer_id = c.customer_id AND o.order_date = d.order_date
JOIN books b ON b.title = d.title;

-- 40th customer/order/detail (included to make each main table contain 40 sample rows).
INSERT INTO customers (customer_name, phone, email, address)
VALUES ('Jeeva Kumar', '9876500040', 'customer40@example.com', '40 Main Road, Chennai');

INSERT INTO orders (customer_id, order_date, total_amount)
SELECT c.customer_id, '2026-10-21', b.price
FROM customers c
JOIN books b ON b.title = 'Design Patterns'
WHERE c.email = 'customer40@example.com';

INSERT INTO order_details (order_id, book_id, quantity, price)
SELECT o.order_id, b.book_id, 1, b.price
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN books b ON b.title = 'Design Patterns'
WHERE c.email = 'customer40@example.com'
  AND o.order_date = '2026-10-21';
  -- Add 20 more rows to categories, employees, and orders.
-- Run this AFTER your earlier sample data has been inserted.
-- These INSERTs do not delete or replace existing rows.

INSERT INTO categories (category_name) VALUES
  ('Romance'),
  ('Mystery'),
  ('Horror'),
  ('Adventure'),
  ('Poetry'),
  ('Travel'),
  ('Cooking'),
  ('Health'),
  ('Sports'),
  ('Philosophy'),
  ('Art'),
  ('Drama'),
  ('Language Learning'),
  ('Reference'),
  ('Religion'),
  ('Self Help'),
  ('Comics and Graphic Novels'),
  ('Economics'),
  ('Engineering'),
  ('Children Fiction');

INSERT INTO employees
(employee_name, phone, email, address, joining_date, salary)
VALUES
  ('Akhil Kumar', '9200000001', 'employee03@example.com', '1 Staff Quarters, Chennai', '2022-02-10', 24750),
  ('Bhuvana Raj', '9200000002', 'employee04@example.com', '2 Staff Quarters, Chennai', '2023-03-10', 25500),
  ('Chandru Sharma', '9200000003', 'employee05@example.com', '3 Staff Quarters, Chennai', '2024-04-10', 26250),
  ('Dharani Devi', '9200000004', 'employee06@example.com', '4 Staff Quarters, Chennai', '2025-05-10', 27000),
  ('Ezhil Nair', '9200000005', 'employee07@example.com', '5 Staff Quarters, Chennai', '2021-06-10', 27750),
  ('Fathima Kumar', '9200000006', 'employee08@example.com', '6 Staff Quarters, Chennai', '2022-07-10', 28500),
  ('Ganesh Raj', '9200000007', 'employee09@example.com', '7 Staff Quarters, Chennai', '2023-08-10', 29250),
  ('Hema Sharma', '9200000008', 'employee10@example.com', '8 Staff Quarters, Chennai', '2024-09-10', 30000),
  ('Indira Devi', '9200000009', 'employee11@example.com', '9 Staff Quarters, Chennai', '2025-01-10', 30750),
  ('Jagan Nair', '9200000010', 'employee12@example.com', '10 Staff Quarters, Chennai', '2021-02-10', 31500),
  ('Kalai Kumar', '9200000011', 'employee13@example.com', '11 Staff Quarters, Chennai', '2022-03-10', 32250),
  ('Logesh Raj', '9200000012', 'employee14@example.com', '12 Staff Quarters, Chennai', '2023-04-10', 33000),
  ('Mithun Sharma', '9200000013', 'employee15@example.com', '13 Staff Quarters, Chennai', '2024-05-10', 33750),
  ('Nandhini Devi', '9200000014', 'employee16@example.com', '14 Staff Quarters, Chennai', '2025-06-10', 34500),
  ('Omprakash Nair', '9200000015', 'employee17@example.com', '15 Staff Quarters, Chennai', '2021-07-10', 35250),
  ('Pooja Kumar', '9200000016', 'employee18@example.com', '16 Staff Quarters, Chennai', '2022-08-10', 36000),
  ('Qadir Raj', '9200000017', 'employee19@example.com', '17 Staff Quarters, Chennai', '2023-09-10', 36750),
  ('Rithika Sharma', '9200000018', 'employee20@example.com', '18 Staff Quarters, Chennai', '2024-01-10', 37500),
  ('Suresh Devi', '9200000019', 'employee21@example.com', '19 Staff Quarters, Chennai', '2025-02-10', 38250),
  ('Thenmozhi Nair', '9200000020', 'employee22@example.com', '20 Staff Quarters, Chennai', '2021-03-10', 39000);

-- Add 20 orders for customers already present in the earlier 40-customer sample.
-- The email lookup uses the existing customer IDs, even if AUTO_INCREMENT values differ.
INSERT INTO orders (customer_id, order_date, total_amount)
SELECT c.customer_id, d.order_date, d.total_amount
FROM (
  SELECT 'customer01@example.com' AS email, '2026-10-01' AS order_date, 436 AS total_amount
  UNION ALL
  SELECT 'customer02@example.com' AS email, '2026-10-02' AS order_date, 573 AS total_amount
  UNION ALL
  SELECT 'customer03@example.com' AS email, '2026-10-03' AS order_date, 710 AS total_amount
  UNION ALL
  SELECT 'customer04@example.com' AS email, '2026-10-04' AS order_date, 847 AS total_amount
  UNION ALL
  SELECT 'customer05@example.com' AS email, '2026-10-05' AS order_date, 984 AS total_amount
  UNION ALL
  SELECT 'customer06@example.com' AS email, '2026-10-06' AS order_date, 1121 AS total_amount
  UNION ALL
  SELECT 'customer07@example.com' AS email, '2026-10-07' AS order_date, 1258 AS total_amount
  UNION ALL
  SELECT 'customer08@example.com' AS email, '2026-10-08' AS order_date, 1395 AS total_amount
  UNION ALL
  SELECT 'customer09@example.com' AS email, '2026-10-09' AS order_date, 332 AS total_amount
  UNION ALL
  SELECT 'customer10@example.com' AS email, '2026-10-10' AS order_date, 469 AS total_amount
  UNION ALL
  SELECT 'customer11@example.com' AS email, '2026-10-11' AS order_date, 606 AS total_amount
  UNION ALL
  SELECT 'customer12@example.com' AS email, '2026-10-12' AS order_date, 743 AS total_amount
  UNION ALL
  SELECT 'customer13@example.com' AS email, '2026-10-13' AS order_date, 880 AS total_amount
  UNION ALL
  SELECT 'customer14@example.com' AS email, '2026-10-14' AS order_date, 1017 AS total_amount
  UNION ALL
  SELECT 'customer15@example.com' AS email, '2026-10-15' AS order_date, 1154 AS total_amount
  UNION ALL
  SELECT 'customer16@example.com' AS email, '2026-10-16' AS order_date, 1291 AS total_amount
  UNION ALL
  SELECT 'customer17@example.com' AS email, '2026-10-17' AS order_date, 1428 AS total_amount
  UNION ALL
  SELECT 'customer18@example.com' AS email, '2026-10-18' AS order_date, 365 AS total_amount
  UNION ALL
  SELECT 'customer19@example.com' AS email, '2026-10-19' AS order_date, 502 AS total_amount
  UNION ALL
  SELECT 'customer20@example.com' AS email, '2026-10-20' AS order_date, 639 AS total_amount
) AS d
JOIN customers c ON c.email = d.email;
-- Add 20 more order detail rows to existing customers/orders/books.
-- Run after the sample customers, books, and orders have been inserted.
INSERT INTO order_details (order_id, book_id, quantity, price)
SELECT o.order_id, b.book_id, d.quantity, b.price
FROM (
  SELECT 'customer01@example.com' AS email, 'The Alchemist' AS title, 2 AS quantity
  UNION ALL
  SELECT 'customer02@example.com' AS email, 'Database Management Systems' AS title, 3 AS quantity
  UNION ALL
  SELECT 'customer03@example.com' AS email, 'Python Programming' AS title, 4 AS quantity
  UNION ALL
  SELECT 'customer04@example.com' AS email, 'Wings of Fire' AS title, 1 AS quantity
  UNION ALL
  SELECT 'customer05@example.com' AS email, 'The Adventures of Tintin' AS title, 2 AS quantity
  UNION ALL
  SELECT 'customer06@example.com' AS email, 'Atomic Habits' AS title, 3 AS quantity
  UNION ALL
  SELECT 'customer07@example.com' AS email, 'Introduction to Algorithms' AS title, 4 AS quantity
  UNION ALL
  SELECT 'customer08@example.com' AS email, 'The God of Small Things' AS title, 1 AS quantity
  UNION ALL
  SELECT 'customer09@example.com' AS email, 'Rich Dad Poor Dad' AS title, 2 AS quantity
  UNION ALL
  SELECT 'customer10@example.com' AS email, 'The Hobbit' AS title, 3 AS quantity
  UNION ALL
  SELECT 'customer11@example.com' AS email, 'Clean Code' AS title, 4 AS quantity
  UNION ALL
  SELECT 'customer12@example.com' AS email, 'A Brief History of Time' AS title, 1 AS quantity
  UNION ALL
  SELECT 'customer13@example.com' AS email, 'The White Tiger' AS title, 2 AS quantity
  UNION ALL
  SELECT 'customer14@example.com' AS email, 'Head First Java' AS title, 3 AS quantity
  UNION ALL
  SELECT 'customer15@example.com' AS email, 'Sapiens' AS title, 4 AS quantity
  UNION ALL
  SELECT 'customer16@example.com' AS email, 'The Jungle Book' AS title, 1 AS quantity
  UNION ALL
  SELECT 'customer17@example.com' AS email, 'Deep Work' AS title, 2 AS quantity
  UNION ALL
  SELECT 'customer18@example.com' AS email, 'Computer Networks' AS title, 3 AS quantity
  UNION ALL
  SELECT 'customer19@example.com' AS email, 'Ponniyin Selvan' AS title, 4 AS quantity
  UNION ALL
  SELECT 'customer20@example.com' AS email, 'The Little Prince' AS title, 1 AS quantity
) AS d
JOIN customers c ON c.email = d.email
JOIN orders o ON o.order_id = (
    SELECT MIN(o2.order_id)
    FROM orders o2
    WHERE o2.customer_id = c.customer_id
)
JOIN books b ON b.title = d.title;






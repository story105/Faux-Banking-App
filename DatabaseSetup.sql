%-- Assignment 3 Charlie Story
-- Creating the database/tables
CREATE TABLE Customer (
	customer_id INT PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	SSN INT,
	ON UPDATE CASCADE
	ON DELETE SET NULL
);

CREATE TABLE Account_xref (
	customer_id INT PRIMARY KEY,
	account_num INT,
	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
	ON UPDATE CASCADE
	ON DELETE SET NULL
);

CREATE TABLE Account (
	account_num INT PRIMARY KEY,
	account_type VARCHAR(50),
	balance DECIMAL(50,2),
	FOREIGN KEY (account_num) REFERENCES Account_xref(account_num),
	ON UPDATE CASCADE
	ON DELETE SET NULL
);

CREATE TABLE Transaction_log (
	timestamp TIMESTAMP,
	trans_id INT,
	account_num INT,
	trans_type VARCHAR(50),
	trans_amount DECIMAL(20,2),
	FOREIGN KEY (account_num) REFERENCES Account_xref(account_num),
	ON UPDATE CASCADE
	ON DELETE SET NULL
);

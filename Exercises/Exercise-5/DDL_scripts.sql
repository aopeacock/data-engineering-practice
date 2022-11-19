-- CREATE TABLE account_roles (
--   user_id INT NOT NULL,
--   role_id INT NOT NULL,
--   grant_date TIMESTAMP,
--   PRIMARY KEY (user_id, role_id),
--   FOREIGN KEY (role_id)
--       REFERENCES roles (role_id),
--   FOREIGN KEY (user_id)
--       REFERENCES accounts (user_id)
-- );

CREATE TABLE accounts (
    customer_id INT NOT NULL, 
    first_name VARCHAR(50),
    last_name VARCHAR(50), 
    address_1 VARCHAR(200),
    address_2 VARCHAR(200),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    join_date DATE,
    PRIMARY KEY (customer_id)
);

CREATE INDEX idx_accounts_customer_id on accounts(customer_id);

CREATE TABLE products (
    product_id INT NOT NULL,
    product_code VARCHAR(20),
    product_description VARCHAR(50),
    PRIMARY KEY (product_id)
);

CREATE INDEX idx_products_product_id on products(product_id);

CREATE TABLE transactions (
    transaction_id VARCHAR(50) NOT NULL,
    transaction_date DATE,
    product_id INT,
    product_code VARCHAR(20),
    product_description VARCHAR(50),
    quantity INT,
    account_id INT,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id),
    FOREIGN KEY (account_id)
        REFERENCES accounts(customer_id)
);

CREATE INDEX idx_transactions_transaction_id on transactions(transaction_id);
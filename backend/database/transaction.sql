# Epic Title: Develop a User-Friendly Dashboard

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount FLOAT,
    transaction_type VARCHAR(50),
    date TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
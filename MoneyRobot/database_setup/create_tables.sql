USE moneyrobot;

CREATE TABLE transactions (
    transaction_id MEDIUMINT NOT NULL AUTO_INCREMENT primary key,
    transaction_date DATE DEFAULT (CURRENT_DATE),
    transactor TEXT NOT NULL,
    transaction_category TEXT NOT NULL,
    items TEXT NOT NULL,
    transaction_amount DECIMAL(8,2),
    time_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
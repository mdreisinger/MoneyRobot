USE moneyrobot;

CREATE TABLE expenses (
    expense_id BINARY(16) default (uuid_to_bin(uuid())) not null primary key,
    expense_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    expense DECIMAL(8,2),
    payee TEXT NOT NULL,
    expense_category TEXT NOT NULL,
    items TEXT NOT NULL,
    time_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE expense_notes (
    expense_note_id BINARY(16) default (uuid_to_bin(uuid())) not null primary key,
    note TEXT NOT NULL,
    time_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    time_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    expense_id BINARY(16)
);

CREATE TABLE income (
    income_id BINARY(16) default (uuid_to_bin(uuid())) not null primary key,
    income_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    income DECIMAL(8,2),
    payor TEXT NOT NULL,
    income_category TEXT NOT NULL,
    time_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE income_notes (
    income_note_id BINARY(16) default (uuid_to_bin(uuid())) not null primary key,
    note TEXT NOT NULL,
    time_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    time_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    income_id BINARY(16)
);

ALTER TABLE expense_notes
ADD FOREIGN KEY (expense_id)
REFERENCES expenses(expense_id)
ON DELETE CASCADE;

ALTER TABLE income_notes
ADD FOREIGN KEY (income_id)
REFERENCES income(income_id)
ON DELETE CASCADE;
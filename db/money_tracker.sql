DROP TABLE transactions;
DROP TABLE merchants;

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255));

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    merchant_id INTEGER REFERENCES merchants(id) ON DELETE CASCADE,
    tag VARCHAR(255),);
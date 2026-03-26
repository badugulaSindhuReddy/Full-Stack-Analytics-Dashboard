CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    category VARCHAR(50),
    amount FLOAT,
    created_at DATE
);

INSERT INTO transactions (category, amount, created_at) VALUES
('Food', 120, '2024-01-01'),
('Travel', 300, '2024-01-02'),
('Shopping', 200, '2024-01-03');

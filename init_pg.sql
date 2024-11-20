CREATE TABLE IF NOT EXISTS demo_table(
    id SERIAL PRIMARy KEY,
    name VARCHAR(100), 
    age INT,
    salary INT
);

INSERT INTO demo_table(name, age, salary)
VALUES ('Alice', 30, 70000),
('Bob', 25, 50000),
('Charlie', 35, 100000),
('David', 40, 120000),
('Eve', 28, 60000),
('Frank', 50, 150000),
('Grace', 33, 80000),
('Hank', 29, 55000),
('Ivy', 42, 110000),
('Jack', 31, 90000);
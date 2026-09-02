# TinaSQL

Скачать проект можно примерно так же как и в инструкции README.md

https://github.com/keyserkrause/Tina


-- Пример: таблица пользователей
CREATE TABLE test_users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    is_active BOOLEAN NOT NULL
);

-- Пример герерации: таблица пользователей
INSERT INTO test_users (username, email, created_at, is_active)
SELECT
    'user_' || g.id,
    'user' || g.id || '@example.com',
    NOW() - (random() * 365 * interval '1 day'),
    (random() > 0.3)
FROM generate_series(1, 1000) AS g(id);

-- Пример: таблица категорий
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
-- Пример: добавление категорий
INSERT INTO categories (name) VALUES ('Electronics'), ('Books'), ('Clothing');

-- Приемер: добавление таблицы товаров
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category_id INT NOT NULL REFERENCES categories(id),
    price NUMERIC(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

--Пример: генерация данных для таблицы товаров
INSERT INTO products (name, category_id, price, stock_quantity)
SELECT
    'Product ' || g.id,
    (floor(random() * 3) + 1)::int,
    (floor(random() * 500) + 10)::numeric,
    (floor(random() * 100) + 1)::int
FROM generate_series(1, 500) AS g(id);

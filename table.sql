CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    published_year INT,
    genre VARCHAR(50)
);
import psycopg2

# Параметри підключення до Aiven PostgreSQL
connection = psycopg2.connect(
    dbname="defaultdb",
    user="avnadmin",
    password="password",
    host="pg-3282bb18-maxk-project1.k.aivencloud.com",
    port="17444"
)

try:
    # Створення таблиці `book`
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS book (
        id SERIAL PRIMARY KEY,
        title VARCHAR(200),
        author VARCHAR(100),
        published_year INT,
        genre VARCHAR(50)
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблицю 'book' успішно створено!")

    # Додавання даних до таблиці
    insert_query = """
    INSERT INTO book (title, author, published_year, genre)
    VALUES
        ('Harry Potter and the Philosophers Stone', 'J.K. Rowling', 1997, 'Fantasy'),
        ('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 1998, 'Fantasy'),
        ('Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling', 1999, 'Fantasy');
    """
    cursor.execute(insert_query)
    connection.commit()
    print("Дані успішно додано до таблиці 'book'!")

    # Отримання даних із таблиці
    select_query = "SELECT * FROM book;"
    cursor.execute(select_query)
    results = cursor.fetchall()
    print("Дані з таблиці 'book':")
    for row in results:
        print(row)

    # Закриття курсора
    cursor.close()

finally:
    # Закриття з'єднання
    connection.close()
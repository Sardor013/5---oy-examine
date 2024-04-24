import psycopg2
from decimal import Decimal

connection = psycopg2.connect(
    host="localhost",
    database="university",
    user="postgres",
    password="sardor123",
    port=5432
)

cursor = connection.cursor()

create_table_query = (f"""
    CREATE TABLE IF NOT EXISTS product
    (
    id serial primary key,
    name varchar(50),
    color varchar(20),
    price serial
    )
    """)

cursor.execute(create_table_query)
connection.commit()
print("Jadval yaratildi .")

product_data = (1, 'Samsung A72', Decimal('452.125478'), 'black')
insert_query = "INSERT INTO Product (ID, NAME, PRICE, COLOR) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_query, product_data)
connection.commit()
print("Ma'lumotlar muvaffaqiyatli qo'shildi.")

cursor.close()
connection.close()















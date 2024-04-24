import psycopg2
import threading


def select():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="sardor123",
            host="localhost",
            port="5432",
            database="examine"
        )

        cursor = connection.cursor()
        query = "SELECT * FROM product;"
        cursor.execute(query)

        records = cursor.fetchall()

        for row in records:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error")

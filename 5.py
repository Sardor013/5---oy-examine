import psycopg2
def connect(user, dbname, password, host):
    connection = psycopg2.connect(
        host="localhost",
        dbname="university",
        user="postgres",
        password="sardor123"
    )


    connection = psycopg2.connect(connection)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

    return connect

select_function = connect("user", "dbname", "password", "host")
result = select_function()
print(result)

import psycopg2

def connect():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="vending",
            user="pmontgomery",
            password="")

        cursor = connection.cursor()
        query = "select * from prerolls"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print( row )

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    connect()
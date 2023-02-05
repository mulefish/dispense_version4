
import sqlite3

conn = sqlite3.connect('dispense.db')

populate_merchants_sql = [
    {
        "id":1,
        "username": "admin",
        "password": "topsecret"
    },
    {
        "id":2,
        "username": "kermitt",
        "password": "Happy$100"
    }]


if __name__ == "__main__":
    TABLE_NAME = "merchants"
    cursor = conn.cursor()

    table = """ CREATE TABLE merchants (
            id INT,
            name VARCHAR(20),
            password VARCHAR(255)
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    cursor.execute(table)

    for x in populate_merchants_sql:
        sql = "INSERT INTO {} VALUES ({}, '{}','{}')".format(
            TABLE_NAME, x["id"], x["username"], x["password"])
        #print( sql )
        cursor.execute(sql)

    print("Created the table '{}' and inserted {} rows into it".format(
        TABLE_NAME, len(populate_merchants_sql)))
    conn.commit()
    conn.close()

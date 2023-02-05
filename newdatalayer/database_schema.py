import sqlite3
conn = sqlite3.connect('new_dispense.db')

cursor = conn.cursor()

def create_orders():
    table_name = "Orders"

    table = """CREATE TABLE Orders (
            orderId_pk INTEGER PRIMARY KEY AUTOINCREMENT,
            storeId_fk INTEGER,
            vendingId_fk INTEGER,
            customerId_fk VARCHAR(255),
            orderTime INTEGer,
            qrCode VARCHAR(255)
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()


def create_order_item():
    table_name = "OrderItem"
    cursor = conn.cursor()

    table = """CREATE TABLE OrderItem (
            order_item_pk INTEGER PRIMARY KEY AUTOINCREMENT,
            itemId_fk INTEGER,
            orderId_fk INTEGER,
            quantity INTEGER
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()


def create_customer(): 
    table_name = "Customer"
    cursor = conn.cursor()

    # sqlite does not have actual booleans. The KEYWORDS 'TRUE' and 'FALSE' are actually the ints 1 and 0 
    table = """CREATE TABLE Customer (
            customerId INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255),
            accountName VARCHAR(255),
            password_secretKey VARCHAR(255),
            validated INTEGER(1) 
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()


def create_store(): 
    table_name = "Store"
    cursor = conn.cursor()

    table = """CREATE TABLE Store (
            storeId INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            address VARCHAR(255),
            lat REAL,
            lon REAL, 
            phone VARCHAR(11),
            merchantId_fk INTEGER
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()


def create_merchant(): 
    table_name = "Merchant"
    cursor = conn.cursor()

    table = """CREATE TABLE Merchant (
            merchantId  INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            billing_address VARCHAR(255),
            phone VARCHAR(11),
            bank_account_info VARCH(255),
            logo_location VARCHAR(255)
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()


def create_associate(): 
    table_name = "Associate"
    cursor = conn.cursor()

    table = """CREATE TABLE Associate (
            associateid INTEGER PRIMARY KEY AUTOINCREMENT,
            merchantId_fk INTEGER,
            name VARCHAR(255)
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()



if __name__ == "__main__":
    create_orders()
    # INSERT INTO Orders (storeId_fk, vendingId_fk, customerId_fk, orderTime, qrCode) VALUES (1,2,3, 1675637122776, "hello")
    create_order_item()
    create_customer()
    create_store()
    create_merchant()
    create_associate()
    conn.close()

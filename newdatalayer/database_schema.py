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
            orderTime INTEGER,
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
            name VARCHAR(100),
            password VARCHAR(100),
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


# def create_item(): 
#     table_name = "Item"
#     cursor = conn.cursor()

#     table = """CREATE TABLE Item (
#             itemId INTEGER PRIMARY KEY AUTOINCREMENT,
#             merchantId_fk INTEGER,
#             name VARCHAR(255),
#             brand VARCHAR(255),
#             JSON BLOB
#         ); """

#     cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
#     cursor.execute(table)


#     print("Created the table '{}'".format(table_name))

#     conn.commit()



def create_item2(): 
    table_name = "Item2"
    cursor = conn.cursor()

    table = """CREATE TABLE Item2 (
            itemId INTEGER PRIMARY KEY AUTOINCREMENT,
            merchantId_fk INTEGER,
            price REAL, 
            instock INTEGER,
            deployed INTEGER,
            brand VARCHAR(20),
            cbd REAL, 
            desc VARCHAR(40),
            farm VARCHAR(20),
            harvest VARCHAR(9),
            name VARCHAR(20),
            strain VARCHAR(20),
            thc REAL,
            type VARCHAR(20),
            weight REAL, 
            count INTEGER,
            product VARCHAR(20)
        ); """


    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()



def create_item(): 
    table_name = "Item"
    cursor = conn.cursor()

    table = """CREATE TABLE Item (
            itemId INTEGER PRIMARY KEY AUTOINCREMENT,
            merchantId_fk INTEGER,
            price REAL, 
            instock INTEGER,
            deployed INTEGER,
            JSON BLOB
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()

def create_stock(): 
    table_name = "stock"
    cursor = conn.cursor()

    table = """CREATE TABLE stock (
            stockId INTEGER PRIMARY KEY AUTOINCREMENT,
            itemId_fk INTEGER,
            vendingId_fk INTEGER,
            row INTEGER(2),
            col INTEGER(2),
            quantity INTEGER(2)
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)


    print("Created the table '{}'".format(table_name))

    conn.commit()

def create_vendingMachine(): 
    table_name = "vendingMachine"
    cursor = conn.cursor()

    table = """CREATE TABLE vendingMachine (
            vendingId INTEGER PRIMARY KEY AUTOINCREMENT,
            storeId_fk INTEGER,
            vendingName VARCHAR(20),
            merchantId_fk INTEGER,
            version VARCHAR(10),
            averageMark REAL,
            JSON BLOB

        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)

 
    print("Created the table '{}'".format(table_name))

    conn.commit()


def create_portlandVendingMachine(): 
    table_name = "portlandVendingMachine"
    cursor = conn.cursor()

    table = """CREATE TABLE portlandVendingMachine (
            rowId INTEGER PRIMARY KEY AUTOINCREMENT,
            storeId_fk INTEGER,
            merchantId_fk INTEGER,
            machineId VARCHAR(30),
            spoolId VARCHAR(2),
            uid VARCHAR(20),
            instock INTEGER, 
            price REAL,
            JSON BLOB

        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)

 
    print("Created the table '{}'".format(table_name))

    conn.commit()

def create_portlandProducts(): 
    table_name = "portlandProducts"
    cursor = conn.cursor()

    table = """CREATE TABLE {} (
            rowId INTEGER PRIMARY KEY AUTOINCREMENT,
            uid VARCHAR(30) NOT NULL,
            desc VARCHAR(100) NOT NULL,
            img_path VARCHAR(200) NOT NULL
        ); """.format(table_name)

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)

 
    print("Created the table '{}'".format(table_name))

    conn.commit()



if __name__ == "__main__":
    create_orders()
    create_order_item()
    create_customer()
    create_store()
    create_merchant()
    create_associate()
    create_item()
    create_stock()
    create_vendingMachine()
    create_item2()
    create_portlandVendingMachine() 
    create_portlandProducts()
    conn.close()

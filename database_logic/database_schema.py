import sqlite3
import sys
import os
current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)
from common import cyan

pathToDatabase="../database/april.db"
conn = sqlite3.connect(pathToDatabase)
cyan("Writing to {}".format(pathToDatabase))

cursor = conn.cursor()


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


#     print("Created the table '{}'".format(table_name))

#     conn.commit()


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
            img_path VARCHAR(200) NOT NULL,
            score INTEGER DEFAULT 0
        ); """.format(table_name)

    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute(table)

 
    print("Created the table '{}'".format(table_name))

    conn.commit()



if __name__ == "__main__":
    create_customer()
    create_store()
    create_merchant()
    create_associate()
    create_portlandVendingMachine() 
    create_portlandProducts()
    conn.close()

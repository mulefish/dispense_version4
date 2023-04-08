import sqlite3

conn = sqlite3.connect("../database/april.db")

cursor = conn.cursor()


def select_Item_table():
    print("\tselect_Item_table()")
    cursor.execute("""SELECT * FROM Item where merchantId_fk = 1 limit 2""")
    list_of_objs = cursor.fetchall()
    for item in list_of_objs:
        print(item)

    conn.commit()

def select_Item_table_count():
    print("\tselect_Item_table()")
    cursor.execute("""SELECT * FROM Item""")
    list_of_objs = cursor.fetchall()
    print("Items count {}".format( len(list_of_objs)))
    conn.commit()




def select_Mercant():
    print("\tselect_Mercant()")
    cursor = conn.cursor()
    sqlfetch = "select merchantId, name, password from merchant limit 2"
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        merchantId = x[0]
        username = x[1]
        password = x[2]
        msg = f"{merchantId} {username} {password}"
        print(msg)
    conn.commit()


def select_Store():
    print("\tselect_Store()")
    cursor = conn.cursor()
    sqlfetch = "select * from Store limit 2;"
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        print(x)
    conn.commit()


def select_vendingMachines():
    print("\tselect_vendingMachines()")
    cursor = conn.cursor()
    sqlfetch = "select * from vendingMachine limit 2;"
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        print(x)
    conn.commit()

def select_Associate():
    print("\tselect_Associate()")
    cursor = conn.cursor()
    sqlfetch = "select * from Associate limit 2;"
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        print(x)
    conn.commit()

if __name__ == "__main__":

    # select_Item_table()
    select_Item_table_count()
    # select_Mercant()
    # select_Store()
    # select_vendingMachines()
    conn.close()

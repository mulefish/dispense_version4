import sqlite3
conn = sqlite3.connect('new_dispense.db')
cursor = conn.cursor()

def select_Item_table():

    cursor.execute('''SELECT * FROM Item''')
    list_of_objs = cursor.fetchall()
    for item in list_of_objs:
        print( item )

    conn.commit()

def select_Mercant():
    cursor = conn.cursor()
    sqlfetch = "select merchantId, name, password from merchant"; 
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
    cursor = conn.cursor()
    sqlfetch = "select * from Store"; 
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        print(x)
    conn.commit()



if __name__ == "__main__":
    
    select_Item_table()
    select_Mercant()
    select_Store()
    conn.close()

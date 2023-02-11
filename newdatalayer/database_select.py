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
    conn.close()


if __name__ == "__main__":
    
    # select_Item_table()
    select_Mercant()
    conn.close()

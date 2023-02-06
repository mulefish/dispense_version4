import sqlite3
conn = sqlite3.connect('new_dispense.db')
cursor = conn.cursor()

def select_Item_table():

    cursor.execute('''SELECT * FROM Item''')
    list_of_objs = cursor.fetchall()
    for item in list_of_objs:
        print( item )

    conn.commit()

if __name__ == "__main__":
    
    select_Item_table()
    conn.close()

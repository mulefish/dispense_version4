import sqlite3
import json

def do_select(sqlfetch):
    # print("do_select !! |{}".format( sqlfetch))
    conn = sqlite3.connect('./datalayer/dispense.db')
    cursor = conn.cursor()
    cursor.execute(sqlfetch)
    rows = cursor.fetchall()
    conn.close()
    return rows
    
if __name__ == "__main__":
    # self test
    query = "select * from vending_flowers where vendingId = 1 and merchantId = 1 and storeId = 1"
    rows = do_select(query)
    print(rows)
    
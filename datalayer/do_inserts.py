import sqlite3
# import json
import traceback
import sys

def do_insert(sql_insert):
    conn = sqlite3.connect('./datalayer/dispense.db')
    try:
        print("do_select !|{}".format( sql_insert))
        cursor = conn.cursor()
        cursor.execute(sql_insert)
        conn.commit()

    except sqlite3.Error as er:
        print("INSERT THAT FAILED:{}".format(sql_insert))
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    conn.close()
    
if __name__ == "__main__":
    # self test
    TABLE_NAME= "vending_machines"
    vendingId = "10"
    merchantId = "1"
    storeId = "1"
    version = "delete_this_entry"
    insert = "INSERT INTO {} VALUES ({},{},{},'{}')".format(TABLE_NAME, vendingId, merchantId, storeId, version)
    do_insert(insert)
    



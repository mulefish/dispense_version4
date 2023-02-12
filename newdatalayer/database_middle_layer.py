
import sqlite3
import json

def do_select(sqlfetch):
    # print("do_select !! |{}".format( sqlfetch))
    conn = sqlite3.connect('./newdatalayer/new_dispense.db')
    cursor = conn.cursor()
    cursor.execute(sqlfetch)
    rows = cursor.fetchall()
    conn.close()
    return rows
    
if __name__ == "__main__":
    # self test
    #
    # REMEMBER: Run the self test one directory up
    query = 'select b.merchantId, a.storeId, a.name as storeName,  b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "kermitt"'
    rows = do_select(query)
    print(rows)
    







import sqlite3
import json

def do_select(sqlfetch):
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
    

def get_vending_machines_of_stores_for_a_merchant(nameOfTheMerchant): 
    sqlfetch = f'select b.merchantId, a.vendingId, a.storeId_fk from vendingMachine a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{nameOfTheMerchant}"'
    data = do_select(sqlfetch)
    machines_by_store = {}
    for row in data:
        merchantId = row[0]
        vendingId = row[1]
        storeId = row[2]

        if storeId in machines_by_store:
            machines_by_store[storeId].append(vendingId)
        else:
            machines_by_store[storeId] = []
            machines_by_store[storeId].append(vendingId)

    # return something like {58: [19, 20], 59: [21]} where '58' and '59' are storeIds and the [19, 20] and [21] are vendingId
    return machines_by_store


def get_merchantId_from_merchantName(merchantName): 
    id = 0 
    sqlfetch = "select merchantId from Merchant where name == '{}'".format(merchantName)
    rows = do_select(sqlfetch)
    for row in rows:
        id = row[0]
    return id



def get_inventory_for_a_merchant_as_json(merchantName): 
    merchantId = get_merchantId_from_merchantName(merchantName)
    # Mixed JSON + SQLite is a pain.
    # Convert everything into JSON and send that. 
    # Downside? On the over 'ingestion' side of the house I will need to remember this goof-around
    ary = [] 
    sqlfetch = f'select itemId, price, instock, deployed, json from Item where merchantId_fk == {merchantId}'

    rows = do_select(sqlfetch)
    for row in rows:
        itemId = row[0]
        price = row[1]
        instock = row[2]
        deployed = row[3]
        j = json.loads(row[4])
        j['itemId'] = itemId
        j['price'] = price
        j['instock'] = instock
        j['deployed'] = deployed


        ary.append(j)
    return ary


def line94(merchantName): 
    merchantId = get_merchantId_from_merchantName(merchantName)
    # Mixed JSON + SQLite is a pain.
    # Convert everything into JSON and send that. 
    # Downside? On the over 'ingestion' side of the house I will need to remember this goof-around
    ary = [] 
    sqlfetch = f'select * from Item2 where merchantId_fk == {merchantId}'

    rows = do_select(sqlfetch)
    for row in rows:
        ary.append(row)
    return ary


def insert_new_product(row_to_insert): 
    conn = sqlite3.connect('./newdatalayer/new_dispense.db')
    cursor = conn.cursor()
    result = "NILL"
    try: 
        # row_to_insert = [-1,99,88,77,'{"brand":"brand","cbd":0,"desc":"this is a description","farm":"some farm","harvest":"01/01/1900","name":"name test","strain":"strain test","thc":99.99,"type":"test","Wt_Num":99,"product":"test product"}']
        merchantId_fk = row_to_insert[0]
        price = row_to_insert[1]
        instock = row_to_insert[2]
        deployed = row_to_insert[3]
        json = row_to_insert[4]
        sql = "insert into Item(merchantId_fk, price, instock, deployed, JSON) values ({}, {},{},{}, '{}');".format(
             merchantId_fk, price, instock, deployed, json
        )
        print(sql)
        cursor.execute(sql)
        conn.commit() 
        result = "OK"
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        result = er
    conn.close()   
    return result     

def delete_Items_for_given_merchantId_fk(merchantId_fk): 
    # This is to clean up a test from the tdd.py
    conn = sqlite3.connect('./newdatalayer/new_dispense.db')
    cursor = conn.cursor()
    try: 
        sql = "delete from Item where merchantId_fk = {}".format(merchantId_fk)
        print(sql)
        cursor.execute(sql)
        conn.commit() 
        result = "OK"
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        result = er
    conn.close()   
    return result     





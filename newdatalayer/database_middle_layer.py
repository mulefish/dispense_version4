
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


def get_inventory_for_a_merchant(merchantId): 
    sqlfetch = f'select itemId, name, brand, json from Item where merchantId_fk == {merchantId}'
    print("get_inventory_for_a_merchant: {}".format(sqlfetch))

    data = do_select(sqlfetch)
    data = []
    for row in data:
        results = {} 
        results['itemId'] = row[0]
        results['name'] = row[1]
        results['brand'] = row[2]
        results['json'] = row[3]
        data.append(results)

    # return something like {58: [19, 20], 59: [21]} where '58' and '59' are storeIds and the [19, 20] and [21] are vendingId
    print(" I got this many {}".format( len(data )))
    return data







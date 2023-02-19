from common import yellow, cyan, log, green, verdict, getUsers
from newdatalayer.database_middle_layer import get_merchantId_from_merchantName, do_select, get_vending_machines_of_stores_for_a_merchant, get_inventory_for_a_merchant_as_json

def get_stores_test():
    name = "kermitt"
    # sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{name}"'
    sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{name}"'
    stores = do_select(sqlfetch)
    actualLength = len(stores)
    isOk = actualLength > 0
    verdict(isOk, True, "get_users_test got {} results ".format(len(stores)))


def get_vending_machines_of_stores_for_a_merchant_test(): 
    data = get_vending_machines_of_stores_for_a_merchant("kermitt")
    result = len(data)
    # result something like {58: [19, 20], 59: [21]} where '58' and '59' are storeIds and the [19, 20] and [21] are vendingId
    isOk = result > 0
    verdict(isOk, True, "get_vending_machines_of_stores_for_a_merchant_test has {} stores ".format(result))

def get_vending_machine_test():
    # Step 1: Get an ID of some vending machine - any one will do
    sql = "select * from vendingMachine where vendingId = 1"
    raw = do_select(sql)
    #                  select * from vendingMachine where vendingId = 1
    # vendingId = raw[-1][-1] 
    # Step 2: Use the vendingId to get the info of that machine.
    print(raw)
    # query = "select * from vendingMachine where vendingId = {}".format(vendingId)
    # result = do_select(query)
    # print(result)
    # n = len(result)
    # isOk = n > 0
    # verdict(isOk, True, "get_vending_machine_test got results of len {} back".format(n))



def get_inventory_for_a_merchant_as_json_test():

    # The table has rows of ints and strings with a ball of json. 
    # Looking for a result set that is entirely JSONifiable for the client side of the house
    x = get_inventory_for_a_merchant_as_json("admin")
    isJsonified = isinstance(x, list)
    isPopulated = len(x) > 0
    isOk = True and isPopulated == True
    verdict(isOk, True, "get_inventory_for_a_merchant_as_json_test got type {} and a count of {} ".format(type(x), len(x)))


def get_merchantId_from_merchantName_test():
    name = "admin"
    merchantId = get_merchantId_from_merchantName(name)
    isOk = False 
    if merchantId > 0: 
        isOk = True 
    verdict(isOk, True, "get_merchantId_from_merchantName_test got merchantId {} from merchantName {} ".format(merchantId, name))

def insert_new_product_test(): 
    try: 
        test_product = [1000,99,88,77,'{"brand":"brand","cbd":0,"desc":"this is a description","farm":"some farm","harvest":"01/01/1900","name":"name test","strain":"strain test","thc":99.99,"type":"test","Wt_Num":99,"product":"test product"}']
        merchantId_fk = test_product[0]
        price = test_product[1]
        instock = test_product[2]
        deployed = test_product[3]
        json = test_product[4]
        sql = "insert into Item(merchantId_fk, price, instock, deployed, JSON) values ({}, {},{},{}, '{}');".format(
             merchantId_fk, price, instock, deployed, json
        )
        cursor.execute(sql)
        conn.commit() 
    except:
        print("An exception occurred")




if __name__ == "__main__":
    get_stores_test()
    get_vending_machines_of_stores_for_a_merchant_test()
    get_inventory_for_a_merchant_as_json_test()
    get_merchantId_from_merchantName_test()
    # insert_new_product_test() 


from common import yellow, cyan, log, green, verdict, getUsers
from newdatalayer.database_middle_layer import get_entire_inventory_of_a_table, selectVendingMachines_ofStores_forGivenUser, selectStores_forGivenUser, get_column_names_of_a_table, get_stores_for_user_and_storeName, delete_Items_for_given_merchantId_fk, get_merchantId_from_merchantName, do_select, get_vending_machines_of_stores_for_a_merchant

def get_column_names_of_a_table_test(): 
    table_name = "store"    
    column_names = get_column_names_of_a_table(table_name)
    expected = ['storeId', 'name', 'address', 'lat', 'lon', 'phone', 'merchantId_fk']
    isOk = False
    if set(expected) == set(column_names):
        isOk = True
    verdict(isOk, True, "get_column_names_of_a_table_test got {} ".format(column_names))




    

def getStoresForUser_oughtToBeGood_test():
    found = get_stores_for_user_and_storeName("kermitt", "Kitty Buds")
    stores = [] 
    for obj in found:
        stores.append( obj["storeName"])

    isOk = False 
    if "Kitty Buds" in stores:
        isOk = True 

    verdict(isOk, True, "getStoresForUser_oughtToBeGood_test got {} ".format(stores))

# def getStoresForUser_oughtToBeFail_withWrongName_test():
#     found = get_stores_for_user("This name is not in the database")

#     stores = [] 
#     for obj in found:
#         stores.append( obj["storeName"])

#     isOk = len(stores) == 0 
#     verdict(isOk, True, "getStoresForUser_oughtToBeFail_withWrongName_test got {} ".format(stores))





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
    verdict(isOk, True, "get_vending_machines_of_stores_for_a_merchant_test got {}".format(data))


def get_merchantId_from_merchantName_test():
    name = "admin"
    merchantId = get_merchantId_from_merchantName(name)
    isOk = False 
    if merchantId > 0: 
        isOk = True 
    verdict(isOk, True, "get_merchantId_from_merchantName_test got merchantId {} from merchantName {} ".format(merchantId, name))

DUMMY_MERCHANT_ID_FK = -1
def cleanup_dummy_insert():
    merchantId_fk = DUMMY_MERCHANT_ID_FK
    result = delete_Items_for_given_merchantId_fk(merchantId_fk)
    isOk = result == "OK"
    verdict(isOk, True, "cleanup_dummy_insert for merchantId_fk {}".format(merchantId_fk))



def select_star_from_portlandVendingMachine(): 
    sql="select price from portlandVendingMachine where price is not null;"
    raw = do_select(sql)
    print(raw)


def selectStores_forGivenUser_test(merchantName): 
    LoH = selectStores_forGivenUser(merchantName)
    isOk = True
    for store in LoH:
        if len(store) != 7:
            isOk = False
    verdict(isOk, True, "selectStores_forGivenUser_test for uses {}".format(merchantName))


def selectVendingMachines_ofStores_forGivenUser_test(merchantName):
    LoH = selectVendingMachines_ofStores_forGivenUser(merchantName)
    #     columns = ["machineId", "storeid_fk", "merchantId_fk" ]
    isOk = True
    for store in LoH:
        if len(store) != 3:
            isOk = False
    verdict(isOk, True, "selectVendingMachines_ofStores_forGivenUser_test for uses {}".format(merchantName))


def get_entire_inventory_of_a_table_test(merchantId_fk):
    rows = get_entire_inventory_of_a_table(1, merchantId_fk, "WarmMoon")
    n = len(rows)
    isOk = n > 0 
    verdict(isOk, True, "get_entire_inventory_of_a_table_test row count {}".format(n))


if __name__ == "__main__":
    get_stores_test()
    get_vending_machines_of_stores_for_a_merchant_test()
    get_merchantId_from_merchantName_test()
    getStoresForUser_oughtToBeGood_test() 
    get_column_names_of_a_table_test()
    get_vending_machines_of_stores_for_a_merchant_test()
    select_star_from_portlandVendingMachine()
    selectStores_forGivenUser_test("kermitt")
    selectVendingMachines_ofStores_forGivenUser_test("kermitt")
    merchantIdForKermitt = get_merchantId_from_merchantName("kermitt")
    # # yellow(merchantIdForKermitt)
    get_entire_inventory_of_a_table_test(merchantIdForKermitt)
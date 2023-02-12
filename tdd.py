from common import yellow, cyan, log, green, verdict, getUsers
from newdatalayer.database_middle_layer import do_select, get_vending_machines_of_stores_for_a_merchant

def get_stores_test():
    name = "kermitt"
    # sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{name}"'
    sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{name}"'
    stores = do_select(sqlfetch)
    print(stores)
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
    raw = do_select("select vendingId  from vendingMachine limit 1")
    vendingId = raw[-1][-1] 
    # Step 2: Use the vendingId to get the info of that machine.
    query = "select * from vendingMachine where vendingId = {}".format(vendingId)
    result = do_select(query)
    print(result)
    n = len(result)
    isOk = n > 0
    verdict(isOk, True, "get_vending_machine_test got results of len {} back".format(n))

if __name__ == "__main__":
    get_stores_test()
    get_vending_machines_of_stores_for_a_merchant_test()
    get_vending_machine_test()

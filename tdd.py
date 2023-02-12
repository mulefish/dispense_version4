from common import yellow, cyan, log, green, verdict, getUsers
from newdatalayer.database_middle_layer import do_select

def get_stores_test():
    name = "kermitt"
    # sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{name}"'
    sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{name}"'

    stores = do_select(sqlfetch)
    print(stores)
    actualLength = len(stores)
    verdict(actualLength, 2, "get_users_test got {} results ".format(len(stores)))


if __name__ == "__main__":
    get_stores_test()
from common import yellow, cyan, log, green, verdict, getUsers
import sqlite3
import json

# Remember! While yes is does seem funny to have the directory here in the name
# because this very file is a sibling to 'april.db' but remember!
# When flask runs these functions it will run from the flask context, therefore 
# have the path here DOES make sense. Odd but true. 
databasePathAndName = "database/april.db"


def updateSpools(storeId, merchantId, machineId, spools):
    green("storeId={} merchantId={} machineId={} ".format(storeId, merchantId, machineId))
    counter = 0 
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    status="tbd"
    try:
        for row in spools:  
            mandatory = row['mandatory']
            optional = row['optional']
            keys=mandatory['keys']
            spoolId = mandatory["spool"]
            uid=mandatory["uid"]
            instock=mandatory["count"]
            price=mandatory['price']
 
            sql="UPDATE portlandVendingMachine SET price={}, uid='{}', instock={}, JSON='{}' WHERE machineId='{}' and spoolId='{}';".format(price,uid, instock, json.dumps(optional), machineId, spoolId)
            counter += 1 
            cursor.execute(sql)
        conn.commit()
        status="OK"
    except Exception as e:
        conn.rollback()
        print('Error:', e)
        status=e
    finally:
        conn.close()

    result = {}
    result["rowsUpdated"]=counter
    result["status"]=status
    return result

def get_column_names_of_a_table(table_name):
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return column_names


def getVendingMachine_fromMerchantIdAndMachineId(merchantId, machineName):
    sqlfetch = f'select count(*) from portlandVendingMachine where merchantId_fk = 1 and machineId = "WarmMoon";'
    spoolCount = do_select(sqlfetch)
    return spoolCount[0][0]

def getStore_where_merchantIdAndStoreName(merchantId, storeName):
    sqlfetch = f'select * from store where merchantId_fk = {merchantId} and name = "{storeName}";'
    stores = do_select(sqlfetch)
    columns = {
        "storeId":0,
        "storeName":1,
        "storeAddress":2, 
        "lat":3,
        "lon":4,
        "phone":5
    }
    found = []
    for ary in stores: 
        obj = {} 
        for k in columns: 
            index = columns[k]
            obj[k] = ary[index]
        found.append(obj)
    return found




def get_stores_for_user_and_storeName(username, storeName): 
    # sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}"'
    sqlfetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}" and a.name = "{storeName}"'
    stores = do_select(sqlfetch)
    columns = {
        "merchantId":0,
        "storeId":1,
        "storeName":2,
        "storeAddress":3, 
        "nerchantName":4,
        "billing_address":5,
        "phone":6
    }
    found = []
    for ary in stores: 
        obj = {} 
        for k in columns: 
            index = columns[k]
            obj[k] = ary[index]
        found.append(obj)
    return found

def do_select(sqlfetch):
    # Nice debug, but NOISY
    # green("do_select {} ".format( sqlfetch) )

    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    cursor.execute(sqlfetch)
    rows = cursor.fetchall()
    conn.close()
    return rows

def getAllProducts():
    """Return an List of Lists of the products """
    sql = "select rowId, uid, desc, img_path from portlandProducts"; 
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    LoL = []
    for row in rows:
        rowId = row[0]
        uid = row[1]
        desc = row[2]
        img_path = row[3]
        L = [ rowId, uid, desc, img_path]
        LoL.append(L)
    conn.close()
    return LoL



# def selectStoresForGivenUser(username):
def selectStores_forGivenUser(username):
    """Return an List of Hashes"""

    sql = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}"'
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    columns = ["merchantId", "storeId", "storeName", "storeAddress", "merchantName", "billing_address", "phone" ]
    LoH = []
    for row in rows:
        H = {} 
        for i in range(len(columns)):
            k = columns[i]
            v = row[i]
            H[k] = v
        LoH.append(H)

    conn.close()
    return LoH

def selectVendingMachines_ofStores_forGivenUser(nameOfTheMerchant): 
    """Return an List of Hashes"""

    sql = f'select  distinct a.machineId, a.storeid_fk, a.merchantId_fk from portlandVendingMachine a, merchant b where  b.merchantId == a.merchantId_fk and b.name = "{nameOfTheMerchant}"'

    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = ["machineId", "storeid_fk", "merchantId_fk" ]
    LoH = []
    for row in rows:
        H = {} 
        for i in range(len(columns)):
            k = columns[i]
            v = row[i]
            H[k] = v
        LoH.append(H)
    conn.close()
    return LoH


    
if __name__ == "__main__":
    # self test
    #
    # REMEMBER: Run the self test one directory up
    query = 'select b.merchantId, a.storeId, a.name as storeName,  b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "kermitt"'
    rows = do_select(query)
    print(rows)
    

def get_vending_machines_of_stores_for_a_merchant(nameOfTheMerchant): 
    sqlfetch = f'select b.merchantId, a.machineId, a.storeId_fk from portlandVendingMachine a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{nameOfTheMerchant}"'
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



def delete_Items_for_given_merchantId_fk(merchantId_fk): 
    # This is to clean up a test from the tdd.py
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    try: 
        sql = "delete from Item where merchantId_fk = {}".format(merchantId_fk)
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



def get_entire_inventory_of_a_table(storeId_fk, merchantId_fk, machineId):
    sql = f'select spoolId, uid, instock, price, JSON from portlandVendingMachine where storeId_fk={storeId_fk} and merchantId_fk={merchantId_fk} and machineid="{machineId}"'
    green(sql)
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    LoH = [] 
    for row in rows:
        mandatory = {
            "spoolId":row[0],
            "uid":row[1],
            "instock":row[2],
            "price":row[3]
        } 
        optional = json.loads(row[4]) 
        obj = {
            "mandatory":mandatory, 
            "optional":optional
        }
        LoH.append(obj)


    return LoH
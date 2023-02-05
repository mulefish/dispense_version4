import sys
sys.path.append('../')
from common import yellow, cyan, log, yellow, green
# from populate_store_and_address import populate_store_and_address_data 
import sqlite3
import json
from convertObjToJson import o2j
conn = sqlite3.connect('dispense.db')

def getStoresInfo_ofAMerchant(merchantId):

    cursor = conn.cursor()
    query1 = f"SELECT * FROM stores where merchantId = {merchantId}"
    cursor.execute(query1)
    list_of_just_one_row = cursor.fetchall()

    return o2j(list_of_just_one_row)

# -- select * from vending_machines where merchantId = 1; 
def getVendingMachines_ofAStore(merchantId, storeId):

    cursor = conn.cursor()
    query1 = f"select * from vending_machines where merchantId = {merchantId} and storeId  = {storeId} ; "
    cursor.execute(query1)
    list_of_just_one_row = cursor.fetchall()

    return o2j(list_of_just_one_row)

def getVendingFlowers_ofAStore(merchantId, storeId): 
    cursor = conn.cursor()
    query1 = f"select * from vending_flowers where merchantId = {merchantId} and storeId  = {storeId} ; "
    cursor.execute(query1)
    list_of_just_one_row = cursor.fetchall()

    return o2j(list_of_just_one_row)


def getVendingPrerolls_ofAStore(merchantId, storeId): 
    cursor = conn.cursor()
    query1 = f"select * from vending_prerolls where merchantId = {merchantId} and storeId  = {storeId} ; "
    cursor.execute(query1)
    list_of_just_one_row = cursor.fetchall()

    return o2j(list_of_just_one_row)




if __name__ == "__main__":
    # Merchant # 1 
    merchantId = 1
    stores = getStoresInfo_ofAMerchant(merchantId)

    # Store # 1 of Merchant # 1 
    storeId = 1 
    vendingMachines = getVendingMachines_ofAStore(merchantId, storeId)


    flowers = getVendingFlowers_ofAStore(merchantId, storeId)
    prerolls = getVendingPrerolls_ofAStore(merchantId, storeId)

    print( prerolls )
import sqlite3
import csv
import sys
import os
current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)
from common import cyan

pathToDatabase="../database/april.db"
conn = sqlite3.connect(pathToDatabase)
cyan("Writing to {}".format(pathToDatabase))



cursor = conn.cursor()
# tables = ["Item","Merchant", "Store", "vendingMachine", "Associate", "Item2", "portlandVendingMachine", "portlandProducts"]
tables = ["Merchant", "Store", "portlandVendingMachine", "portlandProducts"]
def count_the_rows():
    print("count_the_rows")
    for table in tables:
      sql = "select count(*) from {}".format(table)
      cursor.execute(sql)
      row = cursor.fetchall()
      count = row[-1][-1]
      print("\t\t{} rows in '{}'".format(count, table))


def truncate_tables():
    print("truncate_tables()")
    for table in tables:   
      sql = "delete from {}".format(table)
      cursor.execute(sql)

    conn.commit()



def insert_merchants():
    print("insert_merchants()")
    merchants = [
        {
            "name": "kermitt",
            "password": "Happy$100",
            "billing_address": "308 E. Florida, Urbana Il, 61801",
            "phone": "217.367.3196",
            "bank_account_info": "TBD",
            "logo_location": "TBD",
        },
        {
            "name": "admin",
            "password": "topsecret",
            "billing_address": "1017 Lynn St., Urbana Il, 61801",
            "phone": "217.367.4449",
            "bank_account_info": "TBD",
            "logo_location": "TBD",
        },
    ]
    for i in range(len(merchants)):
        name = merchants[i]["name"]
        password = merchants[i]["password"]
        billing_address = merchants[i]["billing_address"]
        phone = merchants[i]["phone"]
        bank_account_info = merchants[i]["bank_account_info"]
        logo_location = merchants[i]["logo_location"]

        sql = "insert into Merchant(name, password,billing_address,phone,bank_account_info,logo_location) values ('{}','{}','{}','{}','{}','{}');".format(
          name, password,billing_address,phone,bank_account_info,logo_location
        )
        
        cursor.execute(sql)
        # print( sql )

    conn.commit()

def insert_stores():
    print("insert_stores()")
    merchants = {}

    sqlfetch = "select merchantId, name from merchant"; 
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        merchantId = x[0]
        username = x[1]
        merchants[username] = merchantId

    stores = [
      {
        "name":"Kitty Buds",
        "address":"232 Alameda, Portland, OR",
        "lat":45.553,
        "lon":-122.636,
        "phone":"5032492584",
        "merchantId_fk": merchants["kermitt"]
      }, 
      {
        "name":"Bright Flower",
        "address":"3000 NE Alberta, Portland, OR",
        "lat":45.558,
        "lon":-122.635,
        "phone":"5032492999",
        "merchantId_fk": merchants["kermitt"]
      }, 
      {
        "name":"House of Johnson",
        "address":"223 SW 18th ave, Portland, OR",
        "lat":45.522,
        "lon":-122.689,
        "phone":"9714342669",
        "merchantId_fk": merchants["admin"]
      }
    ]

    for store in stores:
        name = store['name']
        address = store['address']
        lat = store['lat']
        lon = store['lon']
        phone = store['phone']
        merchantId_fk = store['merchantId_fk']
        sql = "insert into Store(name, address, lat, lon, phone, merchantId_fk) values ('{}','{}','{}','{}','{}','{}');".format(
          name, address, lat, lon, phone, merchantId_fk
        )
        
        cursor.execute(sql)
    conn.commit()



def insert_portlandVendingMachine_step1(): 
    vendingMachines = [
      {
        "storeId_fk":1,
        "merchantId_fk":1,
        "machineId":"WarmMoon"
      },
      {
        "storeId_fk":1,
        "merchantId_fk":1,
        "machineId":"Jupiter"
      },
      {
        "storeId_fk":2,
        "merchantId_fk":1,
        "machineId":"PepsiCoke"
      },
      {
        "storeId_fk":3,
        "merchantId_fk":2,
        "machineId":"FlightyDirt"
      }
    ]

    spoolIds = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

    for machine in vendingMachines: 
      storeId_fk = machine["storeId_fk"]
      merchantId_fk = machine["merchantId_fk"]
      machineId = machine["machineId"]
      blankJson = {} 
      for spool in spoolIds:
        sql = "insert into portlandVendingMachine(storeId_fk,merchantId_fk,machineId, spoolId, JSON) values ({},{},'{}','{}','{}' );".format(storeId_fk,merchantId_fk,machineId,spool, blankJson)
        # print(sql )
        cursor.execute(sql)
    conn.commit()

def insert_uid_products(): 
  products = [
    ['15643151 - A1', 'tincture indica highly | relaxation, energy, calm', '#'],
    ['15643151 - A2', 'Pre-roll flower indica | happy, relax, laughter', '#'],
    ['15643151 - A3', 'Pre-roll flower sativa | vivid Colors, spacey, relax', '#'],
    ['1545615-J5', 'Pre-roll flower Hybrid | introspection, hungery, creative', '#'],
    ['1545615-J6', 'Pre-roll flower Ruderalis | hungery, relaxation, energy', '#'],
    ['1545615-J7', 'edibel THC | energy, energy, vivid Colors', '#'],
    ['54845613-J5', 'edibel gummies | introspection, spacey, relaxation', '#'],
    ['54845613-J6', 'edibel gummies | introspection, laughter, introspection', '#'],
    ['54845613-J7', 'edibel gummies | laughter, relaxation, energy', '#'],
    ['coke candy', 'concentrate crumble | laughter, creative, energy', '#'],
    ['7845364-J6', 'concentrate | relax, energy, energy', '#'],
    ['7845364-J7', 'concentrate | laughter, creative, slow time', '#'],
    ['85413165-A1', 'tincture indica | hungery, hungery, relaxation', '#'],
    ['85413165-A2', 'tincture indica | laughter, calm, euphoria', '#'],
    ['85413165-A3', 'tincture indica | relaxation, spacey, euphoria', '#'],
    ['489465 - B1', 'tincture sativa | hungery, euphoria, euphoria', '#'],
    ['489465 - B2', 'tincture sativa | creative, relax, energy', '#'],
    ['84612313 - B1', 'tincture sativa | euphoria, hungery, spacey', '#'],
    ['84612313 - B2', 'tincture sativa | introspection, creative, vivid Colors', '#'],
    ['41418561', 'tincture sativa | euphoria, happy, happy', '#'],
    ['1849815', 'concentrate  shatter | creative, relax, happy', '#'],
    ['9416115', 'concentrate shatter | relaxation, energy, vivid Colors', '#'],
    ['87984156 - C1', 'concentrate shatter | laughter, vivid Colors, relax', '#'],
    ['87984156 - C2', 'concentrate shatter | creative, happy, relaxation', '#'],
    ['151601561 - C1', 'concentrate shatter | happy, calm, happy', '#']
  ]
  for p in products: 
    uid = p[0]
    desc = p[1]
    imgPath = p[2]
    sql = "insert into portlandProducts(uid, desc, img_path) values ('{}','{}','{}');".format(uid, desc, imgPath)
    cursor.execute(sql)
  conn.commit()



def insert_uid_product_image(): 
  products = [
    ["concentrate_shatter_100x_46.png",46],
    ["concentrate_shatter_100x_50.png",50],
    ["edibel_100x_29.png",27],
    ["edibel_100x_31.png",31],
    ["preroll_100x_30.png",30],
    ["preroll_indica_100x_27.png",27],
    ["preroll_sativa_100x_28.png",28],
    ["tincture_100x_26.png",26],
    ["tinture_sativa_100x_45.png",45]
  ]
  for p in products: 
    file_name = p[0]
    rowId = p[1]
    sql = "update portlandProducts set img_path = '{}' where rowId = {}".format(file_name, rowId)
    cursor.execute(sql)
  conn.commit()




def insert_portlandVendingMachine_step2(): 
  with open('portlandVendingMachines2.csv', 'r') as file:
    i = 0 
    isGood = True 
    reader = csv.DictReader(file, delimiter='|')
    for row in reader:
      if isGood == True:
        rowId = row["rowId"]
        storeId_fk = row["storeId_fk"]
        merchantId_fk = row["merchantId_fk"]
        machineId = row["machineId"]
        spoolId = row["spoolId"]
        instock = row["instock"]
        price = row["price"]
        uid = row["uid"]
        JSON = row["JSON"]
        sql="UPDATE portlandVendingMachine SET price={}, uid='{}', instock={}, JSON='{}' WHERE machineId='{}' and spoolId='{}';".format(price,uid, instock, JSON, machineId, spoolId)
        try:
          i += 1 
          if isGood == True:
            cursor.execute(sql)
            # print(sql)
          else: 
            print( " {} POISON on {}".format( i , row))
          conn.commit()
        except Exception as e:
          # conn.rollback()
          print('Error:', e)
          print(" {}   {} ".format(i, sql)) 
          isGood = False

    # finally:
    #     cyan("insert_portlandVendingMachine_step2() updated {} rows".format(i))


truncate_tables()
insert_merchants()
insert_stores()
insert_portlandVendingMachine_step1() 
insert_portlandVendingMachine_step2()
insert_uid_products()
insert_uid_product_image()
count_the_rows()
conn.close()

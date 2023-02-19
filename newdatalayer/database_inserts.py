import sqlite3

conn = sqlite3.connect("new_dispense.db")
cursor = conn.cursor()
tables = ["Item","Merchant", "Store", "vendingMachine", "Associate"]
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

def insert_into_item_table(): 

  products = [
    [1,13.07,42,0,'{"brand":"Estraweeda","cbd":30.49,"desc":"Relaxed, Euphoric, Sleepy, Hungry, Happy","farm":"","harvest":"21/05/20","name":"Indica_5","strain":"Estraweeda","thc":20.17,"type":"preroll","Wt_Num":5,"product":"preroll"}'],
    [0,7.20,13,0,'{"brand":"Estraweeda","cbd":32.86,"desc":"Happy, Relaxed, Uplifted, Euphoric, Sleepy","farm":"","harvest":"23/11/20","name":"Hybrid_15","strain":"Estraweeda","thc":10.08,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [0,30.42,61,0,'{"brand":"Red Flight","cbd":20.45,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"15/05/20","name":"Hybrid_5","strain":"Red Flight","thc":38.64,"type":"preroll","Wt_Num":5,"product":"preroll"}'],
    [0,86.00,84,0,'{"brand":"Estraweeda","cbd":16.07,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"02/02/19","name":"Hybrid_5","strain":"Estraweeda","thc":38.66,"type":"preroll","Wt_Num":5,"product":"preroll"}'],
    [0,77.81,28,0,'{"brand":"Estraweeda","cbd":36.29,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"23/04/20","name":"Hybrid_15","strain":"Estraweeda","thc":13.8,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [0,70.15,11,0,'{"brand":"Silky","cbd":39.87,"desc":"Relaxed, Sleepy, Euphoric, Happy, Uplifted","farm":"","harvest":"15/04/20","name":"Indica_10","strain":"Silky","thc":19.99,"type":"preroll","Wt_Num":10,"product":"preroll"}'],
    [1,68.33,72,0,'{"brand":"Silky","cbd":28.85,"desc":"Relaxed, Euphoric, Sleepy, Hungry, Happy","farm":"","harvest":"17/01/21","name":"Indica_10","strain":"Silky","thc":23.38,"type":"preroll","Wt_Num":10,"product":"preroll"}'],
    [1,43.99,94,0,'{"brand":"Red Flight","cbd":26.13,"desc":"Euphoric, Uplifted, Relaxed, Talkative, Happy","farm":"","harvest":"27/09/21","name":"Sativa_15","strain":"Red Flight","thc":11.79,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [1,74.80,58,0,'{"brand":"Silky","cbd":24.8,"desc":"Happy, Relaxed, Sleepy, Euphoric, Creative","farm":"","harvest":"21/09/21","name":"Indica_15","strain":"Silky","thc":26.28,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [0,85.11,17,0,'{"brand":"Estraweeda","cbd":39.3,"desc":"Happy, Relaxed, Sleepy, Euphoric, Creative","farm":"","harvest":"12/09/21","name":"Indica_10","strain":"Estraweeda","thc":34.48,"type":"preroll","Wt_Num":10,"product":"preroll"}'],
    [0,68.78,34,0,'{"brand":"Silky","cbd":15.06,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"02/04/20","name":"Sativa_15","strain":"Silky","thc":14.07,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [0,20.11,45,0,'{"brand":"Red Flight","cbd":24.35,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"23/07/21","name":"Sativa_20","strain":"Red Flight","thc":39.39,"type":"preroll","Wt_Num":20,"product":"preroll"}'],
    [0,29.33,78,0,'{"brand":"Estraweeda","cbd":18.73,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"19/04/21","name":"Sativa_20","strain":"Estraweeda","thc":10.78,"type":"preroll","Wt_Num":20,"product":"preroll"}'],
    [0,96.16,91,0,'{"brand":"Red Flight","cbd":19.57,"desc":"Happy, Relaxed, Sleepy, Euphoric, Creative","farm":"","harvest":"07/08/21","name":"Indica_10","strain":"Red Flight","thc":16.66,"type":"preroll","Wt_Num":10,"product":"preroll"}'],
    [0,29.20,8,0,'{"brand":"Estraweeda","cbd":21.03,"desc":"Euphoric, Uplifted, Relaxed, Talkative, Happy","farm":"","harvest":"10/01/20","name":"Sativa_5","strain":"Estraweeda","thc":19.63,"type":"preroll","Wt_Num":5,"product":"preroll"}'],
    [0,93.84,23,0,'{"brand":"Silky","cbd":20.67,"desc":"Relaxed, Creative, Uplifted, Euphoric, Hungry","farm":"","harvest":"18/11/21","name":"Hybrid_15","strain":"Silky","thc":30.65,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [0,43.39,59,0,'{"brand":"Silky","cbd":14.35,"desc":"Happy, Relaxed, Uplifted, Euphoric, Sleepy","farm":"","harvest":"05/05/19","name":"Hybrid_15","strain":"Silky","thc":36.07,"type":"preroll","Wt_Num":15,"product":"preroll"}'],
    [0,0.24,93,0,'{"brand":"Silky","cbd":10.26,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"11/07/20","name":"Sativa_20","strain":"Silky","thc":39.46,"type":"preroll","Wt_Num":20,"product":"preroll"}'],
    [1,78.66,79,0,'{"brand":"Estraweeda","cbd":25.95,"desc":"Relaxed, Sleepy, Euphoric, Happy, Uplifted","farm":"","harvest":"12/10/20","name":"Indica_5","strain":"Estraweeda","thc":31.94,"type":"preroll","Wt_Num":5,"product":"preroll"}'],
    [0,60.38,86,0,'{"brand":"Silky","cbd":33.96,"desc":"Hungry, Happy, Tingly, Uplifted, Creative","farm":"","harvest":"12/10/20","name":"Sativa_5","strain":"Silky","thc":38.04,"type":"preroll","Wt_Num":5,"product":"preroll"}'],
    [0,64.30,75,0,'{"brand":"Peanut","cbd":0.09,"desc":"indoor outdoor terpenes","farm":"Noble","harvest":"10/22/19","name":"Kellog","strain":"Peanut Butter Pie","thc":27.3,"type":"flower","Wt_Num":1.09,"product":"flower"}'],
    [1,62.76,88,0,'{"brand":"Sunset","cbd":0.7,"desc":"indoor outdoor terpenes","farm":"HighWinds","harvest":"11/05/19","name":"Kellog","strain":"Sunset Sherbert","thc":28.4,"type":"flower","Wt_Num":1.07,"product":"flower"}'],
    [1,87.07,82,0,'{"brand":"Headdog","cbd":0.07,"desc":"indoor outdoor terpenes","farm":"Heros of the Farm","harvest":"11/14/19","name":"Kellog","strain":"Headdog","thc":26.64,"type":"flower","Wt_Num":1.04,"product":"flower"}'],
    [0,42.85,67,0,'{"brand":"OG","cbd":0.09,"desc":"indoor outdoor terpenes","farm":"Makru Farms","harvest":"10/21/19","name":"Kellog","strain":"OG KB","thc":25.03,"type":"flower","Wt_Num":1.04,"product":"flower"}'],
    [0,76.24,42,0,'{"brand":"LostCause","cbd":0,"desc":"indoor outdoor terpenes","farm":"Trichome","harvest":"11/05/19","name":"Kellog","strain":"Lost Cause","thc":22.06,"type":"flower","Wt_Num":1.08,"product":"flower"}'],
    [0,92.04,44,0,'{"brand":"AB","cbd":0.09,"desc":"indoor outdoor terpenes","farm":"Makru Farms","harvest":"10/21/19","name":"Kellog","strain":"AB KB","thc":25.03,"type":"flower","Wt_Num":1.04,"product":"flower"}'],
    [0,71.43,81,0,'{"brand":"LostLake","cbd":0,"desc":"indoor outdoor terpenes","farm":"Trichome","harvest":"11/05/19","name":"Kellog","strain":"Lost Lake","thc":22.06,"type":"flower","Wt_Num":1.08,"product":"flower"}']
  ]

  for product in products:
    merchantId_fk = product[0]
    price = product[1]
    instock = product[2]
    deployed = product[3]
    json = product[4]

    sql = "insert into Item(merchantId_fk, price, instock, deployed, JSON) values ({}, {},{},{}, '{}');".format(
             merchantId_fk, price, instock, deployed, json
      )
    cursor.execute(sql)
  conn.commit() 
#         sql = "insert into Item(merchantId_fk, name, brand, JSON) values ({}, '{}','{}','{}');".format(
#             merchantId_fk, name, brand, json
#         )
#         cursor.execute(sql)
#         # print( sql )

#     conn.commit()





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


def insert_vending_machines(): 
    print("insert_vending_machines()")
    machines = []
    sqlfetch = "select storeId, merchantId_fk from Store;"; 
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        storeId_fk = x[0]
        merchantId_fk = x[1]
        fk = {
          "storeId_fk":storeId_fk,
          "merchantId_fk":merchantId_fk
        }
        machines.append(fk)


    vendingMachines = [
      # two machine to store 0 
      {
        "storeId_fk":machines[0]["storeId_fk"],
        "merchantId_fk":machines[0]["merchantId_fk"],
        "version":"v1_1",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',
      }, 
      {
        "storeId_fk":machines[0]["storeId_fk"],
        "merchantId_fk":machines[0]["merchantId_fk"],
        "version":"v1_2",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',



      }, 
      # one machine to store 1 
      {
        "storeId_fk":machines[1]["storeId_fk"],
        "merchantId_fk":machines[1]["merchantId_fk"],
        "version":"v1_3",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',


      }, 
      # one machine to store 2 
      {
        "storeId_fk":machines[2]["storeId_fk"],
        "merchantId_fk":machines[2]["merchantId_fk"],
        "version":"v1_1",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',


      }, 

    ] 

    for vm in vendingMachines:
        storeId_fk = vm['storeId_fk']
        merchantId_fk = vm['merchantId_fk']
        version = vm['version']
        averageMark = vm['averageMark']
        payload = vm['PAYLOAD']
        sql = "insert into vendingMachine(storeId_fk,merchantId_fk,version,averageMark, JSON) values ({},{},'{}',{}, '{}' );".format(
          storeId_fk, merchantId_fk, version, averageMark, payload
        )
        
        cursor.execute(sql)
    conn.commit()



def insert_associates():
    print("insert_associates()")
    merchants = []
    sqlfetch = "select merchantId from merchant"; 
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        merchantId = x[0]
        merchants.append(x[0])
    print("merchants")
    print( merchants)

    associates = [
      {
        "merchantId_fk":merchants[0],
        "name":"Adam"      
      }, 
      {
        "merchantId_fk":merchants[0],
        "name":"Becky"      
      }, 
      {
        "merchantId_fk":merchants[0],
        "name":"Charlie"      
      }, 
      {
        "merchantId_fk":merchants[1],
        "name":"Donna"      
      }, 
      {
        "merchantId_fk":merchants[1],
        "name":"Eric"      
      }, 
      {
        "merchantId_fk":merchants[1],
        "name":"Fredricka"      
      }, 
      {
        "merchantId_fk":merchants[1],
        "name":"Gage"      
      }, 
      {
        "merchantId_fk":merchants[1],
        "name":"Hillary"      
      }

    ]

    for associate in associates:
        merchantId_fk = associate["merchantId_fk"]
        name = associate["name"]
        sql = "insert into Associate(merchantId_fk, name) values ({},'{}');".format(merchantId_fk, name)
        
        cursor.execute(sql)
    conn.commit()







truncate_tables()
insert_into_item_table()
insert_merchants()
insert_stores()
insert_vending_machines()
insert_associates()
count_the_rows()
conn.close()

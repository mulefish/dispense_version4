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

def insert_flowers_into_Item_table():
    flower_names = [
        ["Peanut", "Kellog"],
        ["Sunset", "Kellog"],
        ["Headdog", "Kellog"],
        ["OG", "Kellog"],
        ["LostCause", "Kellog"],
        ["AB", "Kellog"],
        ["LostLake", "Kellog"],
    ]
    flowers = [
        '{"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12,"count":10,"product":"flower"}',
        '{"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11,"count":10,"product":"flower"}',
        '{"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8,"count":10,"product":"flower"}',
        '{"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10,"count":10,"product":"flower"}',
        '{"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9,"count":10,"product":"flower"}',
        '{"strain":"AB KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10,"count":11,"product":"flower"}',
        '{"strain":"Lost Lake","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9,"count":9,"product":"flower"}',
    ]

    print("insert_flowers_into_Item_table()")

    for i in range(len(flowers)):
        json = flowers[i]
        name = flower_names[i][0]
        brand = flower_names[i][1]

        sql = "insert into Item(name, brand, JSON) values ('{}','{}','{}');".format(
            name, brand, json
        )
        cursor.execute(sql)
        # print( sql )

    conn.commit()


def insert_prerolls_into_Item_table():

    preroll_names = [
        ["Estraweeda", "Indica_5"],
        ["Estraweeda", "Hybrid_15"],
        ["Red Flight", "Hybrid_5"],
        ["Estraweeda", "Hybrid_5"],
        ["Estraweeda", "Hybrid_15"],
        ["Silky", "Indica_10"],
        ["Silky", "Indica_10"],
        ["Red Flight", "Sativa_15"],
        ["Silky", "Indica_15"],
        ["Estraweeda", "Indica_10"],
        ["Silky", "Sativa_15"],
        ["Red Flight", "Sativa_20"],
        ["Estraweeda", "Sativa_20"],
        ["Red Flight", "Indica_10"],
        ["Estraweeda", "Sativa_5"],
        ["Silky", "Hybrid_15"],
        ["Silky", "Hybrid_15"],
        ["Silky", "Sativa_20"],
        ["Estraweeda", "Indica_5"],
        ["Silky", "Sativa_5"],
    ]

    prerolls = [
        '{"strain":"Estraweeda","type":"Indica","number_of_joints":5,"thc_percent":20.11,"cbd_percent":30.49,"harvest":"21/05/20","description":"Relaxed,Euphoric,Sleepy,Hungry,Happy","price":46.92,"store":1,"stock":5,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Hybrid","number_of_joints":15,"thc_percent":10.08,"cbd_percent":32.86,"harvest":"23/11/20","description":"Happy,Relaxed,Uplifted,Euphoric,Sleepy","price":17.92,"store":2,"stock":9,"product":"prerolls"}',
        '{"strain":"Red Flight","type":"Hybrid","number_of_joints":5,"thc_percent":38.64,"cbd_percent":20.45,"harvest":"15/05/20","description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","price":29.77,"store":2,"stock":9,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Hybrid","number_of_joints":5,"thc_percent":38.66,"cbd_percent":16.01,"harvest":"02/02/19","description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","price":47.35,"store":1,"stock":9,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Hybrid","number_of_joints":15,"thc_percent":13.8,"cbd_percent":36.29,"harvest":"23/04/20","description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","price":23.84,"store":1,"stock":9,"product":"prerolls"}',
        '{"strain":"Silky","type":"Indica","number_of_joints":10,"thc_percent":19.99,"cbd_percent":39.87,"harvest":"15/04/20","description":"Relaxed,Sleepy,Euphoric,Happy,Uplifted","price":19.93,"store":4,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Indica","number_of_joints":10,"thc_percent":23.32,"cbd_percent":28.85,"harvest":"17/01/21","description":"Relaxed,Euphoric,Sleepy,Hungry,Happy","price":33.63,"store":1,"stock":10,"product":"prerolls"}',
        '{"strain":"Red Flight","type":"Sativa","number_of_joints":15,"thc_percent":11.79,"cbd_percent":26.13,"harvest":"27/09/21","description":"Euphoric,Uplifted,Relaxed,Talkative,Happy","price":37.73,"store":4,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Indica","number_of_joints":15,"thc_percent":26.22,"cbd_percent":24.8,"harvest":"21/09/21","description":"Happy,Relaxed,Sleepy,Euphoric,Creative","price":49.36,"store":4,"stock":10,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Indica","number_of_joints":10,"thc_percent":34.42,"cbd_percent":39.3,"harvest":"12/09/21","description":"Happy,Relaxed,Sleepy,Euphoric,Creative","price":32.73,"store":4,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Sativa","number_of_joints":15,"thc_percent":14.01,"cbd_percent":15.06,"harvest":"02/04/20","description":"Hungry,Happy,Tingly,Uplifted,Creative","price":42.73,"store":2,"stock":10,"product":"prerolls"}',
        '{"strain":"Red Flight","type":"Sativa","number_of_joints":20,"thc_percent":39.39,"cbd_percent":24.35,"harvest":"23/07/21","description":"Hungry,Happy,Tingly,Uplifted,Creative","price":35.4,"store":4,"stock":10,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Sativa","number_of_joints":20,"thc_percent":10.78,"cbd_percent":18.73,"harvest":"19/04/21","description":"Hungry,Happy,Tingly,Uplifted,Creative","price":38.24,"store":2,"stock":10,"product":"prerolls"}',
        '{"strain":"Red Flight","type":"Indica","number_of_joints":10,"thc_percent":16.66,"cbd_percent":19.51,"harvest":"07/08/21","description":"Happy,Relaxed,Sleepy,Euphoric,Creative","price":19.84,"store":2,"stock":10,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Sativa","number_of_joints":5,"thc_percent":19.63,"cbd_percent":21.03,"harvest":"10/01/20","description":"Euphoric,Uplifted,Relaxed,Talkative,Happy","price":13.47,"store":1,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Hybrid","number_of_joints":15,"thc_percent":30.65,"cbd_percent":20.61,"harvest":"18/11/21","description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","price":32.68,"store":3,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Hybrid","number_of_joints":15,"thc_percent":36.07,"cbd_percent":14.35,"harvest":"05/05/19","description":"Happy,Relaxed,Uplifted,Euphoric,Sleepy","price":32.33,"store":1,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Sativa","number_of_joints":20,"thc_percent":39.46,"cbd_percent":10.26,"harvest":"11/07/20","description":"Hungry,Happy,Tingly,Uplifted,Creative","price":44.74,"store":2,"stock":10,"product":"prerolls"}',
        '{"strain":"Estraweeda","type":"Indica","number_of_joints":5,"thc_percent":31.94,"cbd_percent":25.95,"harvest":"12/10/20","description":"Relaxed,Sleepy,Euphoric,Happy,Uplifted","price":22.52,"store":1,"stock":10,"product":"prerolls"}',
        '{"strain":"Silky","type":"Sativa","number_of_joints":5,"thc_percent":38.04,"cbd_percent":33.96,"harvest":"12/10/20","description":"Hungry,Happy,Tingly,Uplifted,Creative","price":38.18,"store":1,"stock":10,"product":"prerolls"}',
    ]

    print("insert_prerolls_into_Item_table()")
    for i in range(len(prerolls)):
        json = prerolls[i]
        name = preroll_names[i][0]
        brand = preroll_names[i][1]

        sql = "insert into Item(name, brand, JSON) values ('{}','{}','{}');".format(
            name, brand, json
        )
        cursor.execute(sql)
        # print( sql )

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
        "averageMark":1
      }, 
      {
        "storeId_fk":machines[0]["storeId_fk"],
        "merchantId_fk":machines[0]["merchantId_fk"],
        "version":"v1_2",
        "averageMark":1
      }, 
      # one machine to store 1 
      {
        "storeId_fk":machines[1]["storeId_fk"],
        "merchantId_fk":machines[1]["merchantId_fk"],
        "version":"v1_3",
        "averageMark":1
      }, 
      # one machine to store 2 
      {
        "storeId_fk":machines[2]["storeId_fk"],
        "merchantId_fk":machines[2]["merchantId_fk"],
        "version":"v1_1",
        "averageMark":1
      }, 

    ]

    for vm in vendingMachines:
        storeId_fk = vm['storeId_fk']
        merchantId_fk = vm['merchantId_fk']
        version = vm['version']
        averageMark = vm['averageMark']
        sql = "insert into vendingMachine(storeId_fk,merchantId_fk,version,averageMark) values ({},{},'{}',{});".format(
          storeId_fk, merchantId_fk, version, averageMark
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
insert_flowers_into_Item_table()
insert_prerolls_into_Item_table()
insert_merchants()
insert_stores()
insert_vending_machines()
insert_associates()


count_the_rows()
conn.close()

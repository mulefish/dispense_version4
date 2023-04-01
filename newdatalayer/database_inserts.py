import sqlite3

conn = sqlite3.connect("new_dispense.db")
cursor = conn.cursor()
tables = ["Item","Merchant", "Store", "vendingMachine", "Associate", "Item2", "portlandVendingMachine", "portlandProducts"]
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


def insert_into_item2_table(): 

  items = [
    [1,13.07,42,-1,"Estraweeda",30.49,"Relaxed, Euphoric, Sleepy, Hungry, Happy","","21/05/20","Indica_5","Estraweeda",20.17,"preroll",-1,5,"preroll"],
[2,7.2,13,-1,"Estraweeda",32.86,"Happy, Relaxed, Uplifted, Euphoric, Sleepy","","23/11/20","Hybrid_15","Estraweeda",10.08,"preroll",-1,15,"preroll"],
[2,30.42,61,-1,"Red Flight",20.45,"Relaxed, Creative, Uplifted, Euphoric, Hungry","","15/05/20","Hybrid_5","Red Flight",38.64,"preroll",-1,5,"preroll"],
[1,86,84,-1,"Estraweeda",16.07,"Relaxed, Creative, Uplifted, Euphoric, Hungry","","2/2/19","Hybrid_5","Estraweeda",38.66,"preroll",-1,5,"preroll"],
[1,77.81,28,-1,"Estraweeda",36.29,"Relaxed, Creative, Uplifted, Euphoric, Hungry","","23/04/20","Hybrid_15","Estraweeda",13.8,"preroll",-1,15,"preroll"],
[2,70.15,11,-1,"Silky",39.87,"Relaxed, Sleepy, Euphoric, Happy, Uplifted","","15/04/20","Indica_10","Silky",19.99,"preroll",-1,10,"preroll"],
[2,68.33,72,-1,"Silky",28.85,"Relaxed, Euphoric, Sleepy, Hungry, Happy","","17/01/21","Indica_10","Silky",23.38,"preroll",-1,10,"preroll"],
[2,43.99,94,-1,"Red Flight",26.13,"Euphoric, Uplifted, Relaxed, Talkative, Happy","","27/09/21","Sativa_15","Red Flight",11.79,"preroll",-1,15,"preroll"],
[1,74.8,58,-1,"Silky",24.8,"Happy, Relaxed, Sleepy, Euphoric, Creative","","21/09/21","Indica_15","Silky",26.28,"preroll",-1,15,"preroll"],
[2,85.11,17,-1,"Estraweeda",39.3,"Happy, Relaxed, Sleepy, Euphoric, Creative","","12/9/21","Indica_10","Estraweeda",34.48,"preroll",-1,10,"preroll"],
[2,68.78,34,-1,"Silky",15.06,"Hungry, Happy, Tingly, Uplifted, Creative","","2/4/20","Sativa_15","Silky",14.07,"preroll",-1,15,"preroll"],
[2,20.11,45,-1,"Red Flight",24.35,"Hungry, Happy, Tingly, Uplifted, Creative","","23/07/21","Sativa_20","Red Flight",39.39,"preroll",-1,20,"preroll"],
[2,29.33,78,-1,"Estraweeda",18.73,"Hungry, Happy, Tingly, Uplifted, Creative","","19/04/21","Sativa_20","Estraweeda",10.78,"preroll",-1,20,"preroll"],
[2,96.16,91,-1,"Red Flight",19.57,"Happy, Relaxed, Sleepy, Euphoric, Creative","","7/8/21","Indica_10","Red Flight",16.66,"preroll",-1,10,"preroll"],
[2,29.2,8,-1,"Estraweeda",21.03,"Euphoric, Uplifted, Relaxed, Talkative, Happy","","10/1/20","Sativa_5","Estraweeda",19.63,"preroll",-1,5,"preroll"],
[1,93.84,23,-1,"Silky",20.67,"Relaxed, Creative, Uplifted, Euphoric, Hungry","","18/11/21","Hybrid_15","Silky",30.65,"preroll",-1,15,"preroll"],
[2,43.39,59,-1,"Silky",14.35,"Happy, Relaxed, Uplifted, Euphoric, Sleepy","","5/5/19","Hybrid_15","Silky",36.07,"preroll",-1,15,"preroll"],
[1,0.24,93,-1,"Silky",10.26,"Hungry, Happy, Tingly, Uplifted, Creative","","11/7/20","Sativa_20","Silky",39.46,"preroll",-1,20,"preroll"],
[1,78.66,79,-1,"Estraweeda",25.95,"Relaxed, Sleepy, Euphoric, Happy, Uplifted","","12/10/20","Indica_5","Estraweeda",31.94,"preroll",-1,5,"preroll"],
[1,60.38,86,-1,"Silky",33.96,"Hungry, Happy, Tingly, Uplifted, Creative","","12/10/20","Sativa_5","Silky",38.04,"preroll",-1,5,"preroll"],
[2,64.3,75,-1,"Peanut",0.09,"indoor outdoor terpenes","Noble","10/22/19","Kellog","Peanut Butt  er Pie",27.3,"flower",1.09,-1,"flower"],
[2,62.76,88,-1,"Sunset",0.7,"indoor outdoor terpenes","HighWinds","11/5/19","Kellog","Sunset Sherbert",28.4,"flower",1.07,-1,"flower"],
[1,87.07,82,-1,"Headdog",0.07,"indoor outdoor terpenes","Heros of the Farm","11/14/19","Kellog","Headdog",26.64,"flower",1.04,-1,"flower"],
[1,42.85,67,-1,"OG",0.09,"indoor outdoor terpenes","Makru Farms","10/21/19","Kellog","OG KB",25.03,"flower",1.04,-1,"flower"],
[1,76.24,42,-1,"LostCause",-1,"indoor outdoor terpenes","Trichome","11/5/19","Kellog","Lost Cause",22.06,"flower",1.08,-1,"flower"],
[2,92.04,44,-1,"AB",0.09,"indoor outdoor terpenes","Makru Farms","10/21/19","Kellog","AB KB",25.03,"flower",1.04,-1,"flower"],
[1,71.43,81,-1,"LostLake",-1,"indoor outdoor terpenes","Trichome","11/5/19","Kellog","Lost Lake",22.06,"flower",1.08,-1,"flower"],
]
  for item in items:
    merchantId_fk = item[0]
    price = item[1]
    instock = item[2]
    deployed = item[3]
    brand = item[4]
    cbd = item[5]
    desc = item[6]
    farm = item[7]
    harvest = item[8]
    name = item[9]
    strain = item[10]
    thc = item[11]
    thetype = item[12]
    weight = item[13]
    count = item[14]
    product = item[15]



    sql = "insert into Item2(merchantId_fk,price,instock,deployed,brand,cbd,desc,farm,harvest,name,strain,thc,type,weight,count,product) values ({},{},{},{},'{}',{},'{}','{}','{}','{}','{}',{},'{}',{},{},'{}')".format(merchantId_fk,price,instock,deployed,brand,cbd,desc,farm,harvest,name,strain,thc,thetype,weight,count,product)


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
        "vendingName": "Maggy",
        "version":"v1_1",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',
      }, 
      {
        "storeId_fk":machines[0]["storeId_fk"],
        "merchantId_fk":machines[0]["merchantId_fk"],
        "vendingName": "Shabone",
        "version":"v1_2",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',



      }, 
      # one machine to store 1 
      {
        "storeId_fk":machines[1]["storeId_fk"],
        "merchantId_fk":machines[1]["merchantId_fk"],
        "vendingName": "Eeboo",
        "version":"v1_3",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',


      }, 
      # one machine to store 2 
      {
        "storeId_fk":machines[2]["storeId_fk"],
        "merchantId_fk":machines[2]["merchantId_fk"],
        "vendingName": "Mr. C",
        "version":"v1_1",
        "averageMark":1,
        "PAYLOAD":'{  A0: {},  A1: {},A2: {},  A3: {},  A4: {},  A5: {},  A6: {},  A7: {},  B0: {},  B1: {},  B2: {},  B3: {},  B4: {},  B5: {},  B6: {},  B7: {},  C0: {},  C1: {},  C2: {},  C3: {},  C4: {},  C5: {},  C6: {},  C7: {},  D0: {},  D1: {},  D2: {},  D3: {},  D4: {},  D5: {},  D6: {},  D7: {},  E0: {},  E1: {},  E2: {},  E3: {},  E4: {},  E5: {},  E6: {},  E7: {}}',
      }, 

    ] 

    for vm in vendingMachines:
        storeId_fk = vm['storeId_fk']
        merchantId_fk = vm['merchantId_fk']
        vendingName = vm["vendingName"]
        version = vm['version']
        averageMark = vm['averageMark']
        payload = vm['PAYLOAD']
        sql = "insert into vendingMachine(storeId_fk,merchantId_fk,vendingName, version,averageMark, JSON) values ({},{},'{}','{}',{}, '{}' );".format(
          storeId_fk, merchantId_fk, vendingName, version, averageMark, payload
        )
        
        cursor.execute(sql)
    conn.commit()







#### 


def insert_portlandVendingMachine(): 
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
    ['15643151 - A1', 'Tincture Indica Highly | relaxation, energy, calm', '#'],
    ['15643151 - A2', 'Pre-roll Flower Indica | happy, relax, laughter', '#'],
    ['15643151 - A3', 'Pre-roll Flower Sativa | vivid Colors, spacey, relax', '#'],
    ['1545615-J5', 'Pre-roll Flower Hybrid | introspection, hungery, creative', '#'],
    ['1545615-J6', 'Pre-roll Flower Ruderalis | hungery, relaxation, energy', '#'],
    ['1545615-J7', 'Edibel THC | energy, energy, vivid Colors', '#'],
    ['54845613-J5', 'Edibel Gummies | introspection, spacey, relaxation', '#'],
    ['54845613-J6', 'Edibel Gummies | introspection, laughter, introspection', '#'],
    ['54845613-J7', 'Edibel Gummies | laughter, relaxation, energy', '#'],
    ['coke candy', 'concentrate crumble | laughter, creative, energy', '#'],
    ['7845364-J6', 'concentrate | relax, energy, energy', '#'],
    ['7845364-J7', 'concentrate | laughter, creative, slow time', '#'],
    ['85413165-A1', 'Tincture Indica | hungery, hungery, relaxation', '#'],
    ['85413165-A2', 'Tincture Indica | laughter, calm, euphoria', '#'],
    ['85413165-A3', 'Tincture Indica | relaxation, spacey, euphoria', '#'],
    ['489465 - B1', 'Tincture Sativa | hungery, euphoria, euphoria', '#'],
    ['489465 - B2', 'Tincture Sativa | creative, relax, energy', '#'],
    ['84612313 - B1', 'Tincture Sativa | euphoria, hungery, spacey', '#'],
    ['84612313 - B2', 'Tincture Sativa | introspection, creative, vivid Colors', '#'],
    ['41418561', 'Tincture Sativa | euphoria, happy, happy', '#'],
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



truncate_tables()
insert_into_item_table()
insert_merchants()
insert_stores()
insert_vending_machines()
insert_into_item2_table()
insert_portlandVendingMachine() 
insert_uid_products()
count_the_rows()
conn.close()

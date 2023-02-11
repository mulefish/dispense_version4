import sqlite3

conn = sqlite3.connect("new_dispense.db")
cursor = conn.cursor()


def truncate_tables():
    sql = "delete from Item"
    cursor.execute(sql)
    sql = "delete from Merchant"
    cursor.execute(sql)

    print("truncate_tables()")

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
            "phone": "217-367.3196",
            "bank_account_info": "TBD",
            "logo_location": "TBD",
        },
        {
            "name": "admin",
            "password": "topsecret",
            "billing_address": "1017 Lynn St., Urbana Il, 61801",
            "phone": "217-367.4449",
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


truncate_tables()
insert_flowers_into_Item_table()
insert_prerolls_into_Item_table()
insert_merchants()

conn.close()

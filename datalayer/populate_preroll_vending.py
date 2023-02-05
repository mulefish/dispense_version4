import sqlite3

conn = sqlite3.connect('dispense.db')

preroll_data = [
    {
        "vendingId": 1,
        "merchantId": 1,
        "storeId": 1,

        "brand": "Estraweeda",
        "type": "Indica",
        "strain": "Blue City Diesel",
        "number_of_joints": 10,
        "thc_percent": 19.30,
        "cbd_percent": 0.20,
        "harvest": "12/13/18",
        "description": "",
        "price": "25.00",
        "count":10,
        "product":"preroll"
    },
    {
        "vendingId": 1,
        "merchantId": 1,
        "storeId": 1,
        "brand": "Estraweeda",
        "type": "Sativa",
        "strain": "Ken Glue",
        "number_of_joints": 10,
        "thc_percent": 18.90,
        "cbd_percent": 0.03,
        "harvest": "08/08/18",
        "description": "",
        "price": "25.00",
        "count":10,
        "product":"preroll"

    },
        {
        "vendingId": 2,
        "merchantId": 1,
        "storeId": 1,
        "brand": "Estraweeda",
        "type": "Indica",
        "strain": "Blue City Diesel",
        "number_of_joints": 10,
        "thc_percent": 19.30,
        "cbd_percent": 0.20,
        "harvest": "12/13/18",
        "description": "",
        "price": "25.00",
        "count":10,
        "product":"preroll"

    },
    {
        "vendingId": 2,
        "merchantId": 1,
        "storeId": 1,
        "brand": "Estraweeda",
        "type": "Sativa",
        "strain": "Ken Glue",
        "number_of_joints": 10,
        "thc_percent": 18.90,
        "cbd_percent": 0.03,
        "harvest": "08/08/18",
        "description": "",
        "price": "25.00",
        "count":10,
        "product":"preroll"

    },
    #
        {
        "vendingId": 2,
        "merchantId": 1,
        "storeId": 1,
        "brand": "Estraweeda",
        "type": "Indica",
        "strain": "Blue City Diesel",
        "number_of_joints": 10,
        "thc_percent": 19.30,
        "cbd_percent": 0.20,
        "harvest": "12/13/18",
        "description": "",
        "price": "25.00",
        "count":10,
        "product":"preroll"

    },
    {
        "vendingId": 2,
        "merchantId": 1,
        "storeId": 1,
        "brand": "Estraweeda",
        "type": "Sativa",
        "strain": "Ken Glue",
        "number_of_joints": 10,
        "thc_percent": 18.90,
        "cbd_percent": 0.03,
        "harvest": "08/08/18",
        "description": "",
        "price": "25.00",
                "count":10,
        "product":"preroll"

    },
    
            {
        "vendingId": 3,
        "merchantId": 1,
        "storeId": 2,
        "brand": "Estraweeda",
        "type": "Indica",
        "strain": "Blue City Diesel",
        "number_of_joints": 10,
        "thc_percent": 19.30,
        "cbd_percent": 0.20,
        "harvest": "12/13/18",
        "description": "",
        "price": "25.00",
        "count":10,
                "product":"preroll"

    },
    {
        "vendingId": 3,
        "merchantId": 1,
        "storeId": 2,
        "brand": "Estraweeda",
        "type": "Sativa",
        "strain": "Ken Glue",
        "number_of_joints": 10,
        "thc_percent": 18.90,
        "cbd_percent": 0.03,
        "harvest": "08/08/18",
        "description": "",
        "price": "24.00",
        "count":9,
        "product":"preroll"

    },

]


if __name__ == "__main__":
    TABLE_NAME = "vending_prerolls"
    cursor = conn.cursor()

    table = """ CREATE TABLE vending_prerolls (
        vendingId INT,
        merchantId INT,
        storeId INT,
        brand VARCHAR(255),
        type VARCHAR(255),
        strain VARCHAR(255),
        number_of_joints INTEGER,
        thc_percent REAL,
        cbd_percent REAL,
        harvest VARCHAR(9),
        description VARCHAR(255),
        price REAL,
        count INT,
        product VARCHAR(20)

        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    cursor.execute(table)

    for x in preroll_data:
        sql = "INSERT INTO {} VALUES ({},{},{},'{}', '{}','{}', {}, {}, {},'{}','{}',{}, {}, '{}')".format(
        TABLE_NAME, x["vendingId"], x["merchantId"], x["storeId"], x["brand"], x["type"], x["strain"], x["number_of_joints"], x["thc_percent"], x["cbd_percent"], x["harvest"], x["description"], x["price"], x['count'], x['product'])
        print(sql)
        cursor.execute(sql)

    print("Created the table '{}' and inserted {} rows into it".format(
        TABLE_NAME, len(preroll_data)))
    conn.commit()
    conn.close()

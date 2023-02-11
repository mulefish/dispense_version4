import sys
sys.path.append('../')
from common import yellow, cyan, log, yellow, magenta, green
from populate_store_and_address import populate_store_and_address_data 
import sqlite3
import json
from convertObjToJson import o2j
from qr_code_maker import getQRCodeImage



def select_from_flower_table():

    conn = sqlite3.connect('dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM vending_flowers''')
    list_of_objs = cursor.fetchall()
    # print(list_of_objs)
    lookup = {}
    lookup["strain"]=3
    lookup["type"]=4
    lookup["farm"]=5
    lookup["weight_in_grams"]=6
    lookup["thc_percent"]=7
    lookup["cbd_percent"]=8
    lookup["harvest"]=9
    lookup["description"]=10
    lookup["price"]=11
    lookup["count"]=12
    lookup["product"]=13





    print("[")
    for item in list_of_objs:
        # print(item)
        x = '"strain":"{}","type":"{}","farm":"{}","weight_in_grams":{},"thc_percent":{},"cbd_percent":{},"harvest":"{}","description":"{}","price":{},"count":{},"product":"{}",'.format(item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13])
        print(x)
    


    conn.commit()
    conn.close()




def select_from_prerolls_table():

    conn = sqlite3.connect('dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM prerolls''')
    list_of_objs = cursor.fetchall()
    # print(list_of_objs)
    brand = 1 
    _type = 2 
    strain = 3
    number_of_joints = 4
    thc_percent = 5 
    cbd_percent = 6 
    harvest = 7
    description = 8 
    price = 9 
    store = 10
    stock = 11 



    print("[")
    for item in list_of_objs:
        # # print(item)
        # x = '"strain":"{}","type":"{}","number_of_joints":"{}","thc_percent":{},"cbd_percent":{},"harvest":"{}","description":"{}","price":{},"store":"{}","stock":{}'.format(
        #     item[brand],item[_type],item[strain],item[number_of_joints],item[thc_percent],item[cbd_percent],item[harvest],item[description],item[price],item[store],item[stock])

        x = '"strain":"{}","type":"{}", "number_of_joints":{},"thc_percent":{},"cbd_percent":{},"harvest":"{}","description":"{}","price":{},"store":{},"stock":{}'.format(
            item[brand],item[_type], item[number_of_joints], item[thc_percent], item[cbd_percent], item[harvest], item[description], item[price], item[store], item[stock]
            )
        print("{" + x + "},")

        # print(x)
        # print(item[4])


    conn.commit()
    conn.close()




def init(): 
    select_from_prerolls_table()

init()
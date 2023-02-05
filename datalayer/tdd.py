import sys
sys.path.append('../')
from common import yellow, cyan, log, yellow, magenta, green
from populate_store_and_address import populate_store_and_address_data 
import sqlite3
import json
from convertObjToJson import o2j
from qr_code_maker import getQRCodeImage

def verdict(a, b, msg=""):
    if a == b: 
        cyan("PASS {}".format(msg))
    else:
        yellow("FAIL {}".format(msg))


def check_the_shape_of_the_data():
    expected = [
        "id",
        "name",
        "street",
        "city",
        "state",
        "zip",
        "url",
        "img",
        "phone",
        "lat",
        "long"]
    isOk = True
    for item in populate_store_and_address_data:
        for expect in expected:
            if not expect in item: 
                yellow("Missing {}".format(expect))
                isOk = False
        if len( expected)  != len(item):
            yellow("Size is {} but ought to be {} ".format(len(item), len(expected)))
            isOk = False
    verdict(isOk, True, "check_the_shape_of_the_data")        

def select_one_store_record_and_examine_it():

    conn = sqlite3.connect('dispense.db')
    """
    {
        "name": "Barnside Moods",
        "street": "13122 SE Division St",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97211",
        "url": "example.com",
        "img": "static/leaf.png",
        "phone": "503.123.1234",
        "lat":45.538720,
        "long":-122.662000
    },
    """
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM stores limit 1''')
    list_of_just_one_row = cursor.fetchall()
    expected = ['unicode','unicode','unicode','unicode','unicode','unicode','unicode','unicode','float','float']
    isOk = True
    for row in list_of_just_one_row: 
        print( row )
    # for row in list_of_just_one_row:
    #     i = 0
    #     for col in row: 
    #         t = str(type(col))

    #         if expected[i] == 'unicode':
    #             # 'unicode' for python2.x and 'str' for python 3.x!
    #             # This curlycue is ugly - This is my sadface :(
    #             curlycue = False 
    #             if 'unicode' in t or 'str' in t: 
    #                 curlycue = True 
    #             if curlycue == False: 
    #                 yellow("Loop {}: type expected ('unicode' OR 'string') but got '{}'".format( i,  type(col)))
    #         else:
    #             if not expected[i] in t:
    #                 isOk = False 
    #                 yellow("-L oop {}: type expected '{}' but got '{}'".format( i,  expected[i], type(col)))
    #         # else:
    #         #     cyan("{}: type is '{}' and its value is '{}'".format( i, expected[i], col))
    #         i += 1
    conn.commit()
    conn.close()
    verdict(isOk, True, "select_one_store_record_and_examine_it")


def select_from_flower_table():

    conn = sqlite3.connect('dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM flowers''')
    list_of_objs = cursor.fetchall()
    conn.commit()
    conn.close()
    isOk = len(list_of_objs) > 0
    verdict(isOk, True, "select_from_flower_table: size is {}".format( len(list_of_objs)))

def select_from_prerolls_table():

    conn = sqlite3.connect('dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM prerolls''')
    list_of_objs = cursor.fetchall()
    conn.commit()
    conn.close()
    isOk = len(list_of_objs) > 1
    verdict(isOk, True, "select_from_prerolls_table: size is {}".format( len(list_of_objs)))




def convert_list_of_objs_to_json():
    obj1 = {
        "hello":"1"
    }
    obj2 = {
        "world":"2"
    }
    list_of_objs = []
    list_of_objs.append(obj1)
    list_of_objs.append(obj2)
    j = o2j(list_of_objs)
    expected = """[{"hello": "1"}, {"world": "2"}]"""
    isOk = expected == j
    verdict(isOk, True, "convert_list_of_objs_to_json")


def getQRCodeImage_test():
    isOk = False 
    try: 
        img = getQRCodeImage("dispense.com")
        img.save('test_artifact_ok_to_delete.png')
    except NameError:
        yellow("qr variable is not defined ")
    except:
        yellow("getQRCodeImage_test went awry") 
    finally:

        isOk = True
    
    verdict(isOk, True, "getQRCodeImage_test")

def test_logic_getMerchantStoreAndVendingInfo(): 
    magenta(" TODO! Test logic_getMerchantStoreAndVendingInfo")

def init(): 
    check_the_shape_of_the_data()
    select_one_store_record_and_examine_it()
    convert_list_of_objs_to_json()
    getQRCodeImage_test()
    select_from_flower_table()
    select_from_prerolls_table()
    test_logic_getMerchantStoreAndVendingInfo()

init()
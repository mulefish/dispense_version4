


import sqlite3
import os
import sys
rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

conn = sqlite3.connect("new_dispense.db")
cursor = conn.cursor()
from common import yellow, cyan, green, magenta

def upsert_into_portlandVendingMachine(listOfLists): 
    

    # machines = []
    # sqlfetch = "select storeId, merchantId_fk from Store;"; 
    # cursor.execute(sqlfetch)
    # row = cursor.fetchall()
    # for x in row:
    #     storeId_fk = x[0]
    #     merchantId_fk = x[1]
    #     fk = {
    #       "storeId_fk":storeId_fk,
    #       "merchantId_fk":merchantId_fk
    #     }
    #     machines.append(fk)
    # machineName = [
    #    "Jupiter", "WarmMoon", "PepsiCoke", "FlightyDirt"
    # ]
    # spoolIds = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']


    # index = 0 
    # for row in machines: 
    #   index += 1
    #   storeId_fk = row['storeId_fk']
    #   merchantId_fk = row['merchantId_fk']
    #   machineId = machineName[index]
    #   blankJson = {} 
    #   for spool in spoolIds: 
    #     # count is blank 
    #     # uid is blank 
    #     # json is empty
    #     sql = "insert into portlandVendingMachine(storeId_fk,merchantId_fk,machineId, spoolId, JSON) values ({},{},'{}','{}','{}' );".format(storeId_fk,merchantId_fk,machineId,spool, blankJson)
    #     print(sql)
    #     cursor.execute(sql)
    # conn.commit()


upsert_into_portlandVendingMachine() 
conn.close()

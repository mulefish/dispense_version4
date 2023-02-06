import sqlite3
conn = sqlite3.connect('new_dispense.db')
cursor = conn.cursor()

flower_names = [
    ["Peanut","Kellog"],
    ["Sunset","Kellog"],
    ["Headdog","Kellog"],
    ["OG","Kellog"],
    ["LostCause","Kellog"],
    ["AB","Kellog"],
    ["LostLake","Kellog"]
]
flowers = [
  '{"strain":"Peanut Butter Pie","type":"Indica","farm":"Noble","weight_in_grams":1.09,"thc_percent":27.3,"cbd_percent":0.09,"harvest":"10/22/19","description":"Indoor/outdoor terpenes","price":12,"count":10,"product":"flower"}',
  '{"strain":"Sunset Sherbert","type":"Hybrid","farm":"HighWinds","weight_in_grams":1.01,"thc_percent":28.4,"cbd_percent":0.1,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":11,"count":10,"product":"flower"}',
  '{"strain":"Headdog","type":"Hybrid","farm":"Heros of the Farm","weight_in_grams":1.04,"thc_percent":26.64,"cbd_percent":0.07,"harvest":"11/14/19","description":"Indoor/outdoor terpenes","price":8,"count":10,"product":"flower"}',
  '{"strain":"OG KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10,"count":10,"product":"flower"}',
  '{"strain":"Lost Cause","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9,"count":10,"product":"flower"}',
  '{"strain":"AB KB","type":"Indica","farm":"Makru Farms","weight_in_grams":1.04,"thc_percent":25.03,"cbd_percent":0.09,"harvest":"10/21/19","description":"Indoor/outdoor terpenes","price":10,"count":11,"product":"flower"}',
  '{"strain":"Lost Lake","type":"Sativa","farm":"Trichome","weight_in_grams":1.08,"thc_percent":22.06,"cbd_percent":0,"harvest":"11/05/19","description":"Indoor/outdoor terpenes","price":9,"count":9,"product":"flower"}'
]

for i in range(len(flowers)):
    json = flowers[i]
    name = flower_names[i][0]
    brand = flower_names[i][1]

    sql = "insert into Item(name, brand, JSON) values ('{}','{}','{}');".format(name, brand, json)
    cursor.execute(sql)
    print( sql )

conn.commit()
conn.close()
# for x in flowers:
#     sql = "INSERT INTO {} VALUES ({}, '{}','{}')".format(
#             TABLE_NAME, x["id"], x["username"], x["password"])
#         #print( sql )
#         cursor.execute(sql)

#     print("Created the table '{}' and inserted {} rows into it".format(
#         TABLE_NAME, len(populate_merchants_sql)))
#     conn.commit()
#     conn.close()

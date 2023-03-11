import csv


keys2 = ['Dispense ID', 
'Product UID', 
'in stock', 
' unit price ', 
'Product Type', 
'weight (g)', 
'Producer', 
'Strain', 
'Strain Classification', 
'Batch information', 
'Harvest Date', 
'Total Canabinoids', 
'% THC-A', 
'% Delta 9', 
'% CBD',
'Terpene profile + additional added data points -->']

keys = []
keys.append("Dispense ID") # 0
keys.append("Product UID ") 
keys.append("stock")
keys.append("price ")  
keys.append("product_type")
keys.append("weight") # 5 
keys.append("producer")
keys.append("strain")
keys.append("Strain Classification ") 
keys.append("Batch information  ")
keys.append("harvest") # 10 
keys.append("total canabinoids")  
keys.append("thc_a")
keys.append("delta_9")
keys.append("CBD")
keys.append("Terpene profile")


with open('products.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)


for i in range( len(keys2) ):
    print("  {} {}  ".format( i , keys2[i])) 

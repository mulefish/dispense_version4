
from flask import Flask, redirect, url_for, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from common import yellow, cyan, green, magenta # , getUsers
import sqlite3
import json
from datalayer.do_selects import do_select
from datalayer.do_inserts import do_insert
from flask import jsonify
# from datalayer.b import goat

app = Flask(__name__)
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.name = id
        self.password = password
users = {}
user_ids = {} 

@app.route('/login', methods=['GET', 'POST'])
def login():
    cyan("login")

    if not 'username' in request.form or 'password' not in request.form: 
        yellow("reject")
        return render_template('index_not_logged_in.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        yellow( "{}   {}".format(username, password))
        if username in users and password == users[username].password:
            login_user(users[username])
            return redirect(url_for('merchant'))
    return render_template('index_not_logged_in.html')


@app.route('/merchant')
@login_required
def merchant():
    cyan("merchant")
    username = current_user.name 
    merchantId= user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    sqlfetch = f"select * from stores where merchantId = {merchantId};"; 
    stores = do_select(sqlfetch)

    sqlfetch = f"select * from vending_machines where merchantId = {merchantId};"; 
    vending_machines = do_select(sqlfetch)

    sqlfetch = f"select * from vending_flowers where merchantId = {merchantId};"; 
    vending_flowers = do_select(sqlfetch)
    
    sqlfetch = f"select * from vending_prerolls where merchantId = {merchantId};"; 
    vending_prerolls = do_select(sqlfetch)

    return render_template('index_is_logged_in.html', vending_flowers=vending_flowers,  vending_prerolls=vending_prerolls, merchantName=username,vending_machines=vending_machines,  stores=stores, attempt=14, id=merchantId, username=username)

@app.route('/')
def lulu():
    cyan("index")
    return render_template('index_not_logged_in.html')



@app.route('/insert_vending', methods=['PUT'])
def insert_vending():
    cyan("insert_vending")
    x = request.get_json()
    green(x)
    TABLE_NAME= x['table']
    vendingId = x['newVendingId']
    merchantId = x['newVendingMerchantId']
    storeId = x['newVendingStoreId']
    version = x['newVendingVersion']

    if 'newVendingId' in x and 'newVendingMerchantId' in x and 'newVendingStoreId' in x and 'newVendingVersion' in x:
        insert = "INSERT INTO {} VALUES ({},{},{},'{}')".format(TABLE_NAME, vendingId, merchantId, storeId, version)
        do_insert(insert)
        obj = {"status":"ok"}
        return jsonify(obj)
    else:
        obj = {"status":"Missing parameters"}
        return jsonify( obj )

@app.route('/insert_flowers', methods=['PUT'])
def insert_flowers():
    cyan("insert_flower")
    x = request.get_json()
    green(x)
    TABLE_NAME= x['table']
    vendingId = x['vendingId']
    merchantId = x['merchantId']
    storeId = x['storeId']

    strain = x["strain"]
    type = x["type"]
    farm = x["farm"]
    weight_in_grams = x["weight_in_grams"]
    thc_percent = x["thc_percent"]
    cbd_percent = x["cbd_percent"]
    harvest = x["harvest"]
    description = x["description"]
    price = x["price"]
    count = x["count"]
    product = x["product"]

    if 'strain' in x and 'product' in x and 'type' in x:
        # insert = "INSERT INTO {} (strain, type, farm, weight_in_grams, thc_percent, cbd_percent,harvest,description,count, product) VALUES( {},{},{},'{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(TABLE_NAME, strain, type, farm, weight_in_grams, thc_percent, cbd_percent, harvest, description,count, product )
        insert = "INSERT INTO {} VALUES( {}, {}, {}, {},{},{},'{}', '{}', '{}', '{}', '{}', {}, '{}', '{}')".format(TABLE_NAME, vendingId,     merchantId    , storeId , strain, type, farm, weight_in_grams, thc_percent, cbd_percent, harvest, description,price, count, product )

        do_insert(insert)

        do_insert(insert)
        obj = {"status":"ok"}
        return jsonify(obj)
    else:
        obj = {"status":"Missing parameters"}
        return jsonify( obj )



@app.route('/get_inventory_by_merchant', methods=['POST'])
def get_inventory_by_merchant():
    cyan("get_inventory_by_merchant")
    x = request.get_json()
    if ("merchantId" in x ):
        merchantId = x["merchantId"]
        #
        sqlfetch = "select strain, type, farm, weight_in_grams, thc_percent, cbd_percent,harvest, description, price, count, product from vending_flowers  where merchantId={}".format(merchantId)
        flowers = do_select(sqlfetch)
        #
        sqlfetch = "select brand, type, strain, number_of_joints, thc_percent, cbd_percent, harvest, description, price, count, product from vending_prerolls where merchantId={}".format(merchantId)
        prerolls = do_select(sqlfetch)
        #
        sqlfetch = "select vendingId, merchantId, storeId, version from vending_machines where merchantId={}".format(merchantId)
        vending_machines = do_select(sqlfetch)
        #
        data = {} 
        data["flowers_columns"]=["strain", "type", "farm", "weight_in_grams", "thc_percent", "cbd_percent","harvest", "description", "price", "count", "product"]
        data["flowers"] = flowers 
        #
        data["prerolls_columns"]=["brand", "type", "strain", "number_of_joints", "thc_percent", "cbd_percent","harvest", "description", "price", "count", "product"]
        data["prerolls"] = prerolls
        #
        data["vending_machines_columns"] = ["vendingId", "merchantId", "storeId", "version"]
        data["vending_machines"] = vending_machines

        return jsonify(data)

    else:
        return "Missing parameter"


@app.route('/inventory_by_machine')
@login_required
def inventory_by_machine():
    username = current_user.name 
    merchantId= user_ids[username]
    cyan("inventory_by_machine username={} merchantId={}".format(username, merchantId))    

    return render_template('inventory_by_machine.html', username=username, merchant=merchantId )

@app.route('/get_vending_machine', methods=['POST'])
def get_vending_machine():
    cyan("get_vending_machine")

    obj = {
        "status":"Missing information"
    }
    if request.method == 'POST':
        x = request.get_json()
        if "storeId" in x and "merchantId" in x and "vendingId" in x:
            vendingId = x["vendingId"]
            storeId = x["storeId"]
            merchantId = x["merchantId"]
            print("v={} s={} m={}".format( vendingId, storeId, merchantId ))
            #query = "select * from vending_flowers where vendingId = {} and merchantId = {} and storeId = {}".format(vendingId, merchantId, storeId)
            query = "select * from vending_flowers where vendingId = {} and merchantId = {} and storeId = {}".format( vendingId, storeId, merchantId)

            obj["query"] = query
            obj["status"] = "OK"
            obj["data"] = do_select(query)
        else: 
            obj["status"] = "Missing parameter"
    else:
        obj["status"] = "Incorrect HTTP verb"

    return jsonify(obj)
    





@app.route('/logout')
def logout():
    cyan("logged out")
    logout_user()
    return render_template('index_not_logged_in.html')

@login_manager.user_loader
def load_user(user_id):
    cyan("load_user")
    return users.get(user_id)

def setUsers():
    green("setUsers using new_dispense.db")
    conn = sqlite3.connect('newdatalayer/new_dispense.db')
    cursor = conn.cursor()
    sqlfetch = "select merchantId, name, password from Merchant"; 
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        id = x[0]
        username = x[1]
        password = x[2]
        msg = f"{id} {username} {password}"
        print(msg)
        users[username] = User(username, password) 
        user_ids[username] = id
    conn.close()

if __name__ == '__main__':
    setUsers()

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True # REMOVE THIS ONCE IN PRODUCTION
    cyan("http://34.82.219.228:8080 with database at data/dispense.db")
    # cyan("http://localhost:4040 with database at data/dispense.db")

    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

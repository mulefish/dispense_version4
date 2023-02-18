
from flask import Flask, redirect, url_for, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from common import yellow, cyan, green, magenta
import sqlite3
import json
from newdatalayer.database_middle_layer import do_select, get_vending_machines_of_stores_for_a_merchant,get_inventory_for_a_merchant_as_json

from flask import jsonify


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
    merchantId = user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    # store info
    storeInfoFetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}"'
    stores = do_select(storeInfoFetch)
    # vending machines this merchant has 
    vendingMachines = get_vending_machines_of_stores_for_a_merchant(username)
    # inventory
    inventory = get_inventory_for_a_merchant_as_json(merchantId)
    print( inventory )
    return render_template('index_is_logged_in.html', stores=stores, vendingMachines=vendingMachines, inventory=inventory )


@app.route('/')
def lulu():
    cyan("index")
    return render_template('index_not_logged_in.html')


# getVendingMachine
@app.route('/get_vending_machine', methods=['POST'])
def get_vending_machine():
    obj = {
        "status":"Missing information"
    }
    x = request.get_json()
    if "vendingId" in x:


        vendingId = x["vendingId"]
        cyan("get_vending_machine for vendingId {}".format( vendingId))
        query = "select * from vendingMachine where vendingId = {}".format(vendingId)
        cyan(query)
        result = do_select(query)
        # print(result)
        obj["status"] = "OK"
        obj["data"] = result

    else: 
        cyan("get_vending_machine is missing a parameter")
        obj["status"] = "Missing parameter"


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

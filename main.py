
from flask import Flask, redirect, url_for, request, render_template, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from common import yellow, cyan, green, magenta
import sqlite3
import json
from newdatalayer.database_middle_layer import getAllProducts, get_entire_inventory_of_a_table, selectVendingMachines_ofStores_forGivenUser, selectStores_forGivenUser, updateSpools, getVendingMachine_fromMerchantIdAndMachineId, getStore_where_merchantIdAndStoreName, get_stores_for_user_and_storeName, line94, do_select, get_vending_machines_of_stores_for_a_merchant
# pip install qrcode
import qrcode

from flask import jsonify

# updatePortlandVendingMachine
app = Flask(__name__)
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.name = id
        self.password = password
users = {}
user_ids = {} 

# @app.route('/qrcode/<data>')
@app.route('/qrcode', methods=['GET', 'POST'])
def generate_qrcode():
    # create qr code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # select * from portlandVendingMachine where storeId_fk = 1 and machineId = "WarmMoon" and spoolId = "A1"; 
    itemToReach = {}
    itemToReach['storeId_fk']=1
    itemToReach['machineId']="WarmMoon"
    itemToReach['spoolId']="A1"



    qr.add_data(itemToReach)
    qr.make(fit=True)
    
    # generate qr code image
    img = qr.make_image(fill_color='black', back_color='white')

    # # save qr code image to a buffer
    # buffer = io.BytesIO()
    # img.save(buffer, format='PNG')
    # buffer.seek(0)

    # # send qr code image as a file
    # return send_file(buffer, mimetype='image/png')
    # save qr code image to a temporary file
    img_file = 'temp_qrcode.png'
    img.save(img_file)
    
    # send qr code image as a file
    return send_file(img_file, mimetype='image/png')

@app.route('/update', methods=['POST'])
@login_required 
def update():
    # cyan("update")
    username = current_user.name 
    merchantId = user_ids[username]
    data = request.get_json()

    storeId = data["storeId"]
    machineId = data["machineId"]
    spools = data["spools"]




    stores = getStore_where_merchantIdAndStoreName(merchantId, storeId) 
    spoolCount = getVendingMachine_fromMerchantIdAndMachineId(merchantId, machineId)

    #magenta("!! stores={} spoolCount = {} ".format( len(stores),spoolCount ))
    #magenta(data)

    yellow("update() username {} and merchantId {} storeId {}  machineId {} spoolCount {} ".format(username, merchantId, storeId, machineId, spoolCount))
    yellow(stores)

    result = {}
    if spoolCount > 0 and len(stores) == 1:

        # for row in data['spools']:
        #     mandatory = row['mandatory']
        #     optional = row['optional']
        #     spoolId = mandatory["spool"]

        #     # yellow("storeId={} merchandId={} spoolId={}".format( storeId, merchantId, spoolId )) 
        #     # magenta(mandatory )
        #     # green(optional)
        #     updateSpool(storeId, merchantId, spoolId,mandatory, optional )                
        receipt = updateSpools(storeId, merchantId, machineId, spools )  


        result= {
            "status":receipt["status"],
            "updated":receipt["rowsUpdated"],
            "storeId":storeId,
            "machineId":machineId,
            "storeCount":len(stores),
            "spoolCount":spoolCount,
            # "gotspools":spools
        }
    else:
        result= {
            "status":"NOPE",
            "storeId":storeId,
            "machineId":machineId,
            "storeCount":len(stores),
            "spoolCount":spoolCount,
            "gotspools":spools
        }


    return jsonify(result)


@app.route('/search', methods=['GET', 'POST'])
def search():
    cyan("search")
    return render_template('search.html')


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




@app.route('/upsertVendingMachine')
@login_required
def upsertVendingMachine():
    cyan("upsertVendingMachine upsertVendingMachine.html")
    username = current_user.name 
    merchantId = user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    storeInfoFetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}"'
    stores = do_select(storeInfoFetch)
    vendingMachines = get_vending_machines_of_stores_for_a_merchant(username)

    return render_template('upsertVendingMachine.html', stores=stores, vendingMachines=vendingMachines )



@app.route('/get_inventory', methods=['POST'])
@login_required
def get_inventory():

    data = request.get_json()
    storeid_fk = data["storeid_fk"]
    merchantId_fk = data["merchantId_fk"]
    machineId = data["machineId"]
    inventory = get_entire_inventory_of_a_table(storeid_fk, merchantId_fk, machineId)

    for product in inventory: 
        m = len(product["mandatory"])
        o = len(product["optional"])
        # print("mandatory={} optional={}".format(m, o ))
    cyan("get_inventory storeid_fk={} merchantId_fk={} machineId={} ".format( storeid_fk, merchantId_fk, machineId))

    return jsonify(inventory)



@app.route('/seeProducts')
def seeProducts():
    cyan("seeProducts.html")
    products = getAllProducts()
    return render_template('seeProducts.html', products=products )



@app.route('/merchant')
@login_required
def merchant():
    cyan("merchant merchant.html")
    username = current_user.name 
    merchantId = user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    stores = selectStores_forGivenUser(username)
    vendingMachines = selectVendingMachines_ofStores_forGivenUser(username)
    magenta(vendingMachines)

    return render_template('merchant.html', stores=stores, vendingMachines=vendingMachines )





@app.route('/bulk_insert')
@login_required
def bulk_insert():
    cyan("bulk_insert")
    username = current_user.name 
    merchantId = user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    # store info
    storeInfoFetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}"'
    stores = do_select(storeInfoFetch)
    # vending machines this merchant has 
    vendingMachines = get_vending_machines_of_stores_for_a_merchant(username)
    # inventory
    inventory = get_inventory_for_a_merchant_as_json(username)

    return render_template('bulk_insert.html', stores=stores, vendingMachines=vendingMachines, inventory=inventory )


@app.route('/fill_vending_machines')
@login_required
def fill_vending_machines():
    cyan("bulk_insert")
    username = current_user.name 
    merchantId = user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    # store info
    storeInfoFetch = f'select b.merchantId, a.storeId, a.name as storeName, a.address as storeAddress, b.name as merchantName, b.billing_address, b.phone from store a, merchant b where b.merchantId == a.merchantId_fk and b.name = "{username}"'
    stores = do_select(storeInfoFetch)
    vendingMachines = get_vending_machines_of_stores_for_a_merchant(username)
    # # inventory
    # # inventory = get_inventory_for_a_merchant_as_json(username)
    # inventory2 = line94(username)

    return render_template('fill_vending_machines.html', stores=stores, vendingMachines=vendingMachines, inventory2=inventory2 )



@app.route('/')
def lulu():
    cyan("index")
    return render_template('index_not_logged_in.html')





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

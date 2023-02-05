from flask import Flask, send_file
from flask import jsonify
from flask import render_template
from flask import request 
from helpers.pretty_print import yellow, cyan, log, green
import sqlite3
from helpers.qr_code_maker import getQRCodeImage
from io import BytesIO,StringIO
import base64
from helper import json_parse
#### Globals 
app = Flask(__name__)
stores = [] 


#### Endpoints

# @app.route('/handle_data', methods=['POST'])
# def handle_data():
#     cyan("handle_data")
#     projectpath = request.form['projectFilepath']
#     kittycat = request.form['kittycat']
#     green("projectpath: {}".format( projectpath) )
#     green("kittycat: {}".format( kittycat) )

#     # your code
#     # return a response
#     results = { 
#         "status":"status",
#         "projectpath":projectpath, 
#         "kittycat":kittycat
#     }

#     img = getQRCodeImage("dispensego.com")

#     return render_template('shopping_cart.html', results=results, the_qr=img)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    cyan("handle_data")
    cart_flowers = request.form['cart_flowers']
    cart_preroles = request.form['cart_preroles']

    conn = sqlite3.connect('data/dispense.db')
    cursor = conn.cursor()

    ary = json_parse(cart_flowers)
    for id in ary:
        sqlfetch = "SELECT stock from flowers where id={}".format(id)
        cursor.execute(sqlfetch)
        row = cursor.fetchall()
        stock_outter = row[0]
        stock = stock_outter[0]
        stock -= 1
        if stock  > 0:
            sqlupdate = "update flowers set stock = {} where ROWID = {}".format(stock, id)
            cursor.execute(sqlupdate)
            conn.commit()

    ary = json_parse(cart_preroles)
    for id in ary:

        sqlfetch = "SELECT stock from prerolls where id={}".format(id)
        cursor.execute(sqlfetch)
        row = cursor.fetchall()
        stock_outter = row[0]
        stock = stock_outter[0]
        stock -= 1
        if stock  > 0:
            sqlupdate = "update prerolls set stock = {} where ROWID = {}".format(stock, id)
            cursor.execute(sqlupdate)
            conn.commit()



    green("cart_flowers: {}".format( cart_flowers) )
    green("cart_preroles: {}".format( cart_preroles) )

    # return render_template('purchase.html',cart_flowers=cart_flowers ,  cart_preroles=cart_preroles) # , flowers_in_cart=flowers, prerolls_in_cart=prerolls)
    return admin()


@app.route('/purchase', methods=['POST'])
def purchase():
    cyan("purchase")
    cart_flowers = request.form['cart_flowers']
    cart_preroles = request.form['cart_preroles']
    green("cart_flowers: {}".format( cart_flowers) )
    green("cart_preroles: {}".format( cart_preroles) )

    return render_template('purchase.html',cart_flowers=cart_flowers ,  cart_preroles=cart_preroles) # , flowers_in_cart=flowers, prerolls_in_cart=prerolls)
    


@app.route('/about')
def about():
    cyan("about")
    endpoints = [
        {"name":"index", "path":"/"},
        {"name":"page", "path":"/page"},
        {"name":"map", "path":"/map"},
        {"name":"qr", "path":"/qr"},
        {"name":"json", "path":"/json"},
        {"name":"about", "path":"/about"},
        {"name":"search", "path":"/search"}
    ]
    return render_template('about.html', endpoints=endpoints)


@app.route('/flower/')
def flower_purchase():
    cyan("flower_purchase")

    json = request.json

    result = { 
        "status":"status",
        "json":json
    }
    return jsonify(result)


@app.route('/preroll')
def preroll_purchase():
    id = request.args.get('id')

    cyan("preroll_purchase for {}".format( id))

    conn = sqlite3.connect('data/dispense.db')
    cursor = conn.cursor()
    sqlfetch = "SELECT stock from prerolls where id={}".format(id)
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    stock_outter = row[0]
    stock = stock_outter[0]
    stock -= 1
    status = "successful"
    if stock  < 1:
        status = "already_empty"

    sqlupdate = "update prerolls set stock = {} where ROWID = {}".format(stock, id)
    cursor.execute(sqlupdate)
    conn.commit()

    result = { 
        "status":status,
        "id":id,
        "stock":stock,
        "sql":sqlfetch
    }

    return jsonify(result)


@app.route('/page')
def page():
    cyan("page")
    message = "Hello template"
    return render_template('page.html', message=message, message2="hello")

@app.route('/')
@app.route('/search')
def search():

    cyan("search")
    conn = sqlite3.connect('data/dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM flowers''')
    rows = cursor.fetchall()
    list_of_flowers = [] 
    for r in rows:

        names = ["Nothing", "Super Fresh", "Happy Market", "Shoal Farms", "Paper Jolt Cannabis"]
        obj = {
            "id": r[0],
            "strain": r[1],
            "type": r[2],
            "farm": r[3],
            "weight_in_grams": r[4],
            "thc_percent": r[5],
            "cbd_percent": r[6],
            "harvest": r[7],
            "description": r[8],
            "price":r[9],
            "store": names[r[10]],
            "stock": r[11]
        }
        list_of_flowers.append(obj)

    #######
    cursor.execute('''SELECT * FROM prerolls''')
    rows = cursor.fetchall()
    list_of_prerolls = [] 
    for r in rows:

        obj = {
            "id":r[0],
            "brand":r[1],
            "type":r[2],
            "strain":r[3],
            "number_of_joints":r[4],
            "thc_percent":r[5],
            "cbd_percent":r[6],
            "harvest":r[7],
            "description":r[8],
            "price":r[9],
            "store":names[r[10]],
            "stock": r[11]
        }
        list_of_prerolls.append(obj)


        # x = object2json(list_of_prerolls)

    return render_template('search.html', flowers=list_of_flowers, prerolls=list_of_prerolls)



@app.route('/admin')
def admin():

    cyan("admin")
    conn = sqlite3.connect('data/dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM flowers''')
    rows = cursor.fetchall()
    list_of_flowers = [] 
    names = ["Nothing", "Super Fresh", "Happy Market", "Shoal Farms", "Paper Jolt Cannabis"]

    for r in rows:

        obj = {
            "id": r[0],
            "strain": r[1],
            "type": r[2],
            "farm": r[3],
            "weight_in_grams": r[4],
            "thc_percent": r[5],
            "cbd_percent": r[6],
            "harvest": r[7],
            "description": r[8],
            "price":r[9],
            "store": names[r[10]],
            "stock": r[11]
        }
        list_of_flowers.append(obj)

    cursor.execute('''SELECT * FROM prerolls''')
    rows = cursor.fetchall()
    list_of_prerolls = [] 
    for r in rows:

        obj = {
            "id":r[0],
            "brand":r[1],
            "type":r[2],
            "strain":r[3],
            "number_of_joints":r[4],
            "thc_percent":r[5],
            "cbd_percent":r[6],
            "harvest":r[7],
            "description":r[8],
            "price":r[9],
            "store":r[10],
            "stock": r[11]
        }
        list_of_prerolls.append(obj)


    cursor.execute('''SELECT * FROM stores''')
    rows = cursor.fetchall()
    list_of_stores = [] 
    for r in rows:
        obj = {
            "id": r[0],
            "name": r[1],
            "street": r[2],
            "city": r[3],
            "state": r[4],
            "zip": r[5],
            "url": r[6],
            "img": r[7],
            "phone": r[8],
            "lat":r[9],
            "long":r[10],

        }
        list_of_stores.append(obj)


    data = {
        'flowers':list_of_flowers,
        'prerolls':list_of_prerolls,
        'stores':list_of_stores
    }



    return render_template('admin.html', data=data)





@app.route('/map')
def map():
    cyan("map")
    message = "Hello template"
    return render_template('map.html', message=message, message2="hello")


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/qr')
def serve_img():
    #img = Image.new('RGB', ...)
    img = getQRCodeImage("dispensego.com")
    return serve_pil_image(img)


@app.route('/json')
def json(): 
    cyan('send pre-loaded object')
    return render_template('loop.html', payload=stores)
# 
def pre_load(): 
    conn = sqlite3.connect('data/dispense.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM stores''')
    rows = cursor.fetchall()
    list_of_objs = [] 
    for r in rows:
        obj = {
            "name": r[0],
            "street": r[1],
            "city": r[2],
            "state": r[3],
            "zip": r[4],
            "url": r[5],
            "img": r[6],
            "phone": r[7],
            "lat":r[8],
            "long":r[9]
        }
        list_of_objs.append(obj)

    global stores
    stores = list_of_objs

    cyan("pre_load Ready!")
 



if __name__ == '__main__':
    #pre_load()
    cyan("http://34.83.236.108:8080 with database at data/dispense.db")
    #app.run(host='0.0.0.0', port=8080)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    # app.run(host='0.0.0.0', port=8080)
    # flask run --host=0.0.0.0 --port=80 


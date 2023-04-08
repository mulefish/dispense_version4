from PIL import Image
import sqlite3

def updateDB(name, rowId):
    april
    databasePathAndName='../database/april.db'
    conn = sqlite3.connect(databasePathAndName)
    cursor = conn.cursor()
    try:
        sql = "update portlandProducts set img_path = '{}' where rowId = {}".format(name, rowId)
        print(sql)
        cursor.execute(sql)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print('Error:', e)

    finally:
        conn.close()

def resizeImg():
    name = input("Enter the picture name: ")
    rowId = input("Enter the row: ")

    img = Image.open(name)
    width, height = img.size
    smaller_dim = min(width, height)

    resized_img = img.resize((smaller_dim, smaller_dim))
    resized_img = resized_img.resize((100, 100))

    newName = "../static/images/{}".format(name) 
    print("Wrote to {}".format(newName ))
    resized_img.save(newName)

    updateDB(name, rowId)

resizeImg()


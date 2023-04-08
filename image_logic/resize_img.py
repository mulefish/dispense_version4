from PIL import Image

def resizeImg(origImage, newName):

    img = Image.open(origImage)
    width, height = img.size
    smaller_dim = min(width, height)

    resized_img = img.resize((smaller_dim, smaller_dim))
    resized_img = resized_img.resize((100, 100))

    newName = "../static/images/{}".format(newName) 
    print("Wrote to {}".format(newName ))
    resized_img.save(newName)



### Assumption: first filename points to a file right here in this directory. The second is what it will be renamed to ( and moved ) 

orig = [
["concentrate_shatter_100x_46.png","concentrate_shatter_100x_46.png"], 
["preroll_sativa_100x_28.png","preroll_sativa_100x_28.png"],
["tinture_sativa_100x_45.png","tinture_sativa_100x_45.png"]
]

for o in orig: 
    resizeImg(o[0], o[1])
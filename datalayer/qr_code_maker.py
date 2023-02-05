# import pyqrcode
# import png
# from pyqrcode import QRCode

import qrcode

def getQRCodeImage(urlToEncode):  

    # Link for website
    input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"#Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    #img.save('qrcode001.png')
    return img


# def getQRCodeImage(urlToEncode):  
#     #urlToEncode = "dispense.com"
#     url = pyqrcode.create(urlToEncode)
  
#     # Create and save the svg file naming "myqr.svg"
#     #url.svg("myqr.svg", scale = 8)
  
#     # Create and save the png file naming "myqr.png"
#     #url.png('myqr.png', scale = 6)

#     return url



if __name__ == "__main__":


    #qr = getQRCodeImage("dispense.com")
    #qr.png('test_qr_code.png', scale = 6)
    img = getQRCodeImage("dispense.com")
    img.save('tdd2.png')



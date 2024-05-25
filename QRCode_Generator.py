import qrcode

def generate_qr(text):

    qr = qrcode.QRCode(
        version =1,
        error_correction = qrcode.constants.ERROR_COrrect_L,
        box_size=10,
        border=4,
        )

    qr.add_data(text)
    qr.made(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

#generate_qr("https://www.google.com")
url = input("enter the url")
generate_qr(url)

import qrcode

def create_qr(data):
    img = qrcode.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save("qr_output/qr.png")
    print(data)
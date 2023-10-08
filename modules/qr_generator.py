import qrcode

def create_qr(data, qrcode_tag):
    img = qrcode.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save("qr_output/" + qrcode_tag + ".png")
    print(data)
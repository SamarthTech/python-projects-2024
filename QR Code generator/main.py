import qrcode 
link = input("Paste the link :")

qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)
qr.add_data(link)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.jpg")
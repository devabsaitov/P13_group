# import barcode
# from barcode.writer import ImageWriter
#
# # Generate a barcode image
# barcode_value = "123456789101"  # Replace with your desired barcode value
# barcode_image = barcode.get_barcode_class('ean13')
# barcode_image = barcode_image(barcode_value, writer=ImageWriter())
#
# # Save the barcode image
# barcode_filename = 'barcode.png'  # Replace with your desired filename
# barcode_image.save(barcode_filename)
#
#
#
#
# import qrcode
#
# # Generate a QR code
# data = "https://t.me/absaitovD"  # Replace with your desired data (URL, text, etc.)
# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# qr.add_data(data)
# qr.make(fit=True)
#
# # Create an image from the QR code
# qr_image = qr.make_image(fill_color="black", back_color="white")
#
# # Save the QR code image
# qr_filename = 'qrcode.png'  # Replace with your desired filename
# qr_image.save(qr_filename)


import redis


db = redis.Redis(host = "localhost" , port = 6379,decode_responses=True)

# db.set("1" , "Ikki")
print(db.get("1"))



# print(db.get("1").decode("utf-8"))



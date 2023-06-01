
# with open("lesson.txt" , "r") as f:
#     f.read()
# from fileinput import filename
#
#
# class FileManager:
#     def __init__(self, filename , mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename , self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with FileManager("lesson.txt" , "r") as m:
#     print(m.read())

import qrcode
# pip install qrcode

# Generate a QR code
data = ""  # Replace with your desired data (URL, text, etc.)
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="green", back_color="white")

# Save the QR code image
qr_filename = 'qrcode.png'  # Replace with your desired filename
qr_image.save(qr_filename)








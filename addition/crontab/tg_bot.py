from PyPDF2 import PdfReader
import os


with open("python-task.pdf", 'rb') as f:
    pdf = PdfReader(f)
    if not os.path.exists("images"):
        os.mkdir("images")
    for p in pdf.pages:
        for i in p.images:
            with open(i.name , 'wb') as f:
                f.write(i.data)



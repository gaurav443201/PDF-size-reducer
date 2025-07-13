from PyPDF2 import PdfReader, PdfWriter


name= input("name of the pdf:")
reader = PdfReader(name) # put name here
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open("out.pdf", "wb") as f:
    writer.write(f)

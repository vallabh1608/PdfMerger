from PyPDF2 import *

reader=PdfReader("merged.pdf")
total_pages=len(reader.pages)
writer=PdfWriter()

r=reader.pages[0].rotate(90)
writer.add_page(r)

for page_number in range(1,total_pages):
    page=reader.pages[page_number]
    writer.add_page(page)
with open("output_file.pdf","wb") as output_file:
    writer.write(output_file)
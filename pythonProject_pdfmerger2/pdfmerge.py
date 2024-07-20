
from PyPDF2 import *

pdffiles=["1.pdf","2.pdf","3.pdf"]
merger=PdfMerger()

for pdf in pdffiles:
    pdffile=open(pdf,'rb')
    reader = PdfReader(pdffile)
    merger.append(reader)
pdffile.close()
merger.write('merged.pdf')




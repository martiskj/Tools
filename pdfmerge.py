#!/usr/bin/python
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if len(sys.argv) < 4 and (sys.argv[1] != '-h' and sys.argv[1] != '--help'):
	sys.exit("Not enough input arguments!")

if sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '-help':
	print("pdfmerge.py [firstPdf.pdf] [SecondPdf.pdf] [Outputname]")
	print("Note that Outputname should not include '.pdf' extension")
	sys.exit()

#pdf1 = PdfFileReader(file("page1.pdf", "rb"))
pdf1 = PdfFileReader(file(sys.argv[1], "rb"))
pdf2 = PdfFileReader(file(sys.argv[2], "rb"))
outputName = sys.argv[3]
writer = PdfFileWriter()

for page in range(0, pdf1.getNumPages()):
	writer.addPage(pdf1.getPage(page))

for page in range(0, pdf2.getNumPages()):
	writer.addPage(pdf2.getPage(page))

output = file(outputName+".pdf", "wb")
writer.write(output)
output.close()

print("The pdfs were succesfully merged!")
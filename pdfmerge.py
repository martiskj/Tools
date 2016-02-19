#!/usr/bin/python
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if "-h" in sys.argv or "--help" in sys.argv:
	print("Usage: pdfmerge.py [FILE 1] [FILE 2] ... [FILE N] [OUTPUTNAME]")
	print("\tMerges 'FILE 1' through 'FILE N' into 'OUTPUTNAME.pdf'")
	print("\tNote that 'OUTPUTNAME' should not include '.pdf' extension")
	print("\n -h, --help\t Give this help list")
	sys.exit()
elif len(sys.argv) < 4:
	sys.exit("Error: Not enough input arguments!")

outputName = sys.argv[-1]
writer = PdfFileWriter()
for inputPDF in sys.argv[1:-1]:
	currentPDF = PdfFileReader(file(inputPDF, "rb"))
	for page in range(0, currentPDF.getNumPages()):
		writer.addPage(currentPDF.getPage(page))

output = file(outputName+".pdf", "wb")
writer.write(output)
output.close()

print("The PDFs were succesfully merged!")
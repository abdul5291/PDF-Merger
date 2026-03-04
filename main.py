from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs = []
n = int(input("Enter the number of PDF files you want to merge: "))

for i in range(0,n):
  pdfs.append(input("Enter the path of PDF file " + str(i+1) + ": "))

for pdf in pdfs:
  merger.append(pdf)

merger.write("merged.pdf")
merger.close()
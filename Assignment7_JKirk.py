import os, pathlib
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

""" 
Estabilsh file path (variable or function)
"""
# mac path
# pdf_path = '/Users/birdsmini/Documents/PCC/CIS 112/Code/Assignments/07/From_pythonlearn_ch8.pdf'
# windows path
# pdf_path = 'C:/Users/Jaybi/Desktop/PCC/CIS 112/Code/Assignments/07/CIS112_Assignment7_ExtractPdfPages/From_pythonlearn_ch8.pdf'


# import path via cwd
fileName = 'From_pythonlearn_ch8.pdf'
pdf_path = os.path.join(pathlib.Path.cwd(), fileName)
print("\n\n" + pdf_path)


""" 
Estabilsh input variable (variable or function)
"""
input_pdf = PdfFileReader('C:/Users/Jaybi/Desktop/PCC/CIS 112/Code/Assignments/07/CIS112_Assignment7_ExtractPdfPages/From_pythonlearn_ch8.pdf')
""" 
Estabilsh output variable (variable or function)
"""
output_pdf = PdfFileWriter()
""" 
Use `for in` loop to get pages from input file and add them to output file
"""
def getPages(n1, n2):
    for pageN in range (n1, n2):
        page = input_pdf.getPage(pageN)
        output_pdf.addPage(page)
""" 
Create new file useing output variable
"""
def getName(name):
    pdfStr = ".pdf"
    return name + pdfStr
name = getName("new")


# function to read and add pages to output_pdf
getPages(1, 4)

# completes output of file
with Path (name).open(mode="wb") as outputFile:
    output_pdf.write(outputFile)





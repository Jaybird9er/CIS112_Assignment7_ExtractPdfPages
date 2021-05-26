from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

""" 
Estabilsh file path (variable or function)
"""
pdf_path = '/Users/birdsmini/Documents/PCC/CIS 112/Code/Assignments/07/From_pythonlearn_ch8.pdf'
""" 
Estabilsh input variable (variable or function)
"""
input_pdf = PdfFileReader(pdf_path)
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

with Path (name).open(mode="wb") as outputFile:
    output_pdf.write(outputFile)

getPages(1, 4)



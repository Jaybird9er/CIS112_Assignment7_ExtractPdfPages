""" 
Description: 
 - the program asks for user's input to extract pages from a given PDF
 - the extracted pages are used to generate a new PDF

Author: Jamey Kirk
Date: 05.28.2021
Assignment: 07
Class: CIS 112
"""

import os, pathlib
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# global variables
pageBounds = True
firstPage = 0
lastPage = 0

output_pdf = PdfFileWriter()

# functions
""" 
`for in` loop gets pages from input file and adds them to output file
"""
def getPages(n1, n2):
    for pageN in range (n1, n2):
        page = input_pdf.getPage(pageN)
        output_pdf.addPage(page)

""" 
after pages have been added to file, a new file is created with the user's file name
"""
def outputPDF():
    with Path (userFileName).open(mode="wb") as outputFile:
        output_pdf.write(outputFile)

""" 
main program
"""

fileName =  input("Please enter a file name: ")
pdf_path = os.path.join(pathlib.Path.cwd(), fileName)
input_pdf = PdfFileReader(pdf_path)

while (pageBounds): 
    pageBounds = False   
    firstPage = int(input("Please enter the beginning page number to extract: ")) - 1
    lastPage = int(input("Please enter the ending page number to extract: "))
    # add 1 to firstPage to confirm lastPage isn't larger
    if (firstPage + 1 > lastPage):
        print("Your beginning and ending page numbers are not correct.")
        pageBounds = True
    elif (lastPage > input_pdf.getNumPages()):
        print("Your ending index is out of range, please enter correct ending page.")
        pageBounds = True

# user has successfully entered details and create file
userFileName = input("Please enter output file name: ")

# function to read and add pages to output_pdf
getPages(firstPage, lastPage)

# completes output of file
outputPDF()

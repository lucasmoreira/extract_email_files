import textract
import re
import os
import csv
import PyPDF3
import time
import pdftotext

directory = os.fsencode("/Users/lucasgomes/Desktop/arquivos") #path to files
regex = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\.*" #identify emails

all_text = []
bad_files = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
            
    try: #check for PDF files
        pdf_file = open("arquivos/"+filename , "rb")
        pdf_file = pdftotext.PDF(pdf_file)

        for i in range(j): #for every page of the PDF
            text = pdf_file[j].decode("UTF-8")
            text = text.replace("\n"," ").replace(" @","@").replace("@ ","@")
            all_text.append(text)

    except Exception as error: #if file is not a PDF .. 
        text = textract.process("arquivos/"+filename).decode("UTF-8")
        text = text.replace("\n"," ").replace(" @","@").replace("@ ","@")
        all_text.append(str(text))

    if len(re.findall(regex, str(text)))<1: #if there are no instances found, then try textract (for PDF cases)

        text = textract.process("arquivos/"+filename).decode("UTF-8")
        text = text.replace("\n"," ").replace(" @","@").replace("@ ","@")

        if len(re.findall(regex, str(text)))<1:
            print("\n ************ERRO*************")
            print(text)
            print("Check file: "+ filename +"\n")
            bad_files.append(filename)


text = " ".join(all_text)
text = re.findall(regex, text.lower())
text = [[x] for x in text]
bad_files = [["Check files:"+x] for x in bad_files]
export = text + bad_files
print(export)

# writing the data into the file
file = open('export.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(export)
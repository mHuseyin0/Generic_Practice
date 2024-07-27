# Copyright (c) 2022, YKRCL
# All rights reserved.

from urllib import request
from pypdf import PdfMerger
import os, glob


while True:
    selected_exam = input("İndirmek istediğiniz sınav [Final:f , Midterm-1: m, Midterm-2: m2]: ")
    if selected_exam in ["f", "m", "m2"]:
        break
    else:
        print("Seçeneklerden bir cevap seçiniz!")





pdf_general_link = f"http://www.fen.bilkent.edu.tr/~otekman/math101/[TERM][YEAR]/[EXAM]q[NUMBER].pdf"
merger = PdfMerger()
os.makedirs(os.path.dirname("math/"), exist_ok=True)
file_index = 0
for year in range(21, 12,-1):
    for term in ["f", "s"]:
        for question in range(1, 6, 1):
            try:
                specific_link = pdf_general_link.replace("[YEAR]", str(year)).replace("[TERM]", term).replace("[EXAM]", selected_exam).replace("[NUMBER]", str(question))
                print("Downloading", specific_link)
                request.urlretrieve(specific_link, "math/file_"+str(file_index)+".pdf")
                merger.append("math/file_"+str(file_index)+".pdf")
                file_index += 1
            except:
                if selected_exam == "m":
                    try:    
                        specific_link = pdf_general_link.replace("[YEAR]", str(year)).replace("[TERM]", term).replace("[EXAM]", "m1").replace("[NUMBER]", str(question))
                        print("Downloading", specific_link)
                        request.urlretrieve(specific_link, "math/file_"+str(file_index)+".pdf")
                        merger.append("math/file_"+str(file_index)+".pdf")
                        file_index += 1
                    except:
                        pass

merger.write(selected_exam+"_result.pdf")
merger.close()
for filename in glob.glob("math/file_*"):
    os.remove(filename) 

import glob
import os
from docx import Document
from docx.shared import Pt

# Folder Path
path = "D:/ScarlettBooks/fictionbooks"
# outpath = "D:/ScarlettBooks/outbooks"

# Change the directory
os.chdir(path)

with open("D:/ScarlettBooks/outbooks/books.txt", encoding="utf8") as f:
    data = f.read()

# Read text File
for file in os.listdir():
    # Check whether file is in text format or not
    file_path = f"{path}/{file}"
    with open(file_path, encoding="utf8") as fin:
        data1 = fin.read()

    data += data1

with open("D:/ScarlettBooks/outbooks/books.txt", 'w', encoding="utf8") as fp:
    fp.write(data)

    #     infile = f"{file}.txt"
    #     outfile = f"{outpath}/{file}.txt"
    #     delete_list = ["Provided by LoyalBooks.com"]
    #     with open(outfile, "w+") as fout:
    #         for line in fin:
    #             for word in delete_list:
    #                 line = line.replace(word, "POWERED BY JESSCARLETT")
    #             fout.write(line)
    # fout.close()
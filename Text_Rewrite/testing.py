import glob
import os
from docx import Document
from docx.shared import Pt

# Folder Path
path = "D:/ScarlettBooks/booktest"
outpath = "D:/ScarlettBooks/outbooks"

# Change the directory
os.chdir(path)

# Read text File
for file in os.listdir():
    # Check whether file is in text format or not
    file_path = f"{path}/{file}"
    with open(file_path, 'r') as fin:
        infile = f"{file}.txt"
        outfile = f"{outpath}/{file}.txt"
        delete_list = ["Provided by LoyalBooks.com"]
        with open(outfile, "w+") as fout:
            for line in fin:
                for word in delete_list:
                    line = line.replace(word, "POWERED BY JESSCARLETT")
                fout.write(line)
    fout.close()

# os.chdir(outpath)
# for f in glob.glob('*.txt'):
#     new_name = f.replace(".txt", "")
#     os.rename(f, new_name)
doc = Document()
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(12)
for f in glob.glob('D:/ScarlettBooks/outbooks/*.txt'):
    with open(f, 'r', encoding='utf-8') as openfile:
        line = openfile.read()
        doc.add_paragraph(line)
        doc.save(f + ".docx")

os.chdir(outpath)
for f in glob.glob('D:/ScarlettBooks/outbooks/*.docx'):
    new_name = f.replace(".txt", "")
    os.rename(f, new_name)
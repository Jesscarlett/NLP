import json

# the file to be converted to
# json format
filename = 'D://ScarlettBooks//Children-Stories//Oxford-English-Dictionary.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(filename, encoding="utf-8") as fh:
    for line in fh:
        # reads each line and trims of extra the spaces
        # and gives only the valid words
        try:
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip()
        except ValueError:
            pass

# creating json file
# the JSON file is named as test1
out_file = open("D://ScarlettBooks//Children-Stories//Oxford-English-Dictionary.json", "w")
json.dump(dict1, out_file, indent=1, sort_keys=False)
out_file.close()
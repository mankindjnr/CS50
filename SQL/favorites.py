# thios code will open the csv file and reads from it and returns output

import csv

# open the file inread mode and the reader tells python to analyze the file
with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file) # returns a dictionary
    scratch, python, C = 0, 0, 0
    for row in reader: #line by line - checks for rows in every row while increasing itself to move to the next row
        favorite = row["language"] # use a key to output data
        if favorite == "Scratch":
            scratch +=1
        elif favorite == "C":
            C += 1
        elif favorite == "Python":
            python += 1

print(f"scratch: {scratch}")
print(f"c: {c}")
print(f"python: {python}")

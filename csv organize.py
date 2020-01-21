# This is a program that takes the input .csv file and creates a new .csv file with all the necessary attached data
import csv
import os

# Open the specific file system that contains the training data
import string
from dataclasses import field
from typing import TextIO, Dict, Any

os.chdir("C:/Users/adenm_x26zerm/Downloads/data-science-bowl-2019")
install_id = set()
title = set()
install = dict()
with open('train_test.csv') as train_file:
    csv_reader: object = csv.reader(train_file, delimiter=',')
    for row in csv_reader:
        install_id.add(row[1])
        title.add(row[2])
        install_idDict = dict.fromkeys(install_id, 0)
        if install.get(row[1], "No") == "No":
            install.setdefault(row[1], [0, 0, 0, 0, 0, 0, 0, 0, 0])
        title_dict = dict.fromkeys(title, 0)
        i = 0
        for x in install_idDict:
            install_idDict[x] = i
            i = i+1
        i = 0
        for x in title_dict:
            title_dict[x] = i
            i = i + 1
        install[row[1]][0] = install[row[1]][0] + 1
        install[row[1]][2] = install[row[1]][2] + 1
        install[row[1]][4] = install[row[1]][4] + 1
        install[row[1]][6] = install[row[1]][6] + 1
        install[row[1]][1] = install[row[1]][1] + title_dict[row[2]]
        install[row[1]][3] = install[row[1]][3] + float(row[3])
        install[row[1]][5] = install[row[1]][5] + float(row[4])
        install[row[1]][7] = install[row[1]][7] + float(row[5])
        row[0] = ''
        row[1] = install_idDict[row[1]]
        row[2] = title_dict[row[2]]
        print(row, file=open('train.csv', 'a'))
print(install_idDict, file=open("rings.txt", 'w'))
for x in install:
    #Get the list to print with the ID
    a = install_idDict[x]
    row = str(a) + ", " + str(install[x][1]/install[x][0]) + ", " + str(install[x][3]/install[x][2]) + ", " \
          + str(install[x][5]/install[x][4]) + ", " + str(install[x][7]/install[x][6])
    print(row, file=open('avgtest.csv', 'a'))


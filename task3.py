import os
import re

freq = {}
amount = 0
with open("_itartass1.xhtml", "r", encoding = "utf-8") as file1, \
     open("_itartass2.xhtml", "r", encoding = "utf-8") as file2, \
     open("_itartass3.xhtml", "r", encoding = "utf-8") as file3, \
     open("_itartass4.xhtml", "r", encoding = "utf-8") as file4, \
     open("_itartass5.xhtml", "r", encoding = "utf-8") as file5, \
     open("_rbk2.xhtml", "r", encoding = "utf-8") as file6, \
     open("_rbk3.xhtml", "r", encoding = "utf-8") as file7, \
     open("_rbk4.xhtml", "r", encoding = "utf-8") as file8, \
     open("_rbk6.xhtml", "r", encoding = "utf-8") as file9, \
     open("_rbk7.xhtml", "r", encoding = "utf-8") as file10, \
     open("_rian1.xhtml", "r", encoding = "utf-8") as file11, \
     open("_rian2.xhtml", "r", encoding = "utf-8") as file12, \
     open("_rian3.xhtml", "r", encoding = "utf-8") as file13, \
     open("_rian5.xhtml", "r", encoding = "utf-8") as file14, \
     open("everything.xhtml", "w", encoding = "utf-8") as ready_file:
    ready_file.write(file1.read())
    ready_file.write(file2.read())
    ready_file.write(file3.read())
    ready_file.write(file4.read())
    ready_file.write(file5.read())
    ready_file.write(file6.read())
    ready_file.write(file7.read())
    ready_file.write(file8.read())
    ready_file.write(file9.read())
    ready_file.write(file10.read())
    ready_file.write(file11.read())
    ready_file.write(file12.read())
    ready_file.write(file13.read())
    ready_file.write(file14.read())

f = open('ress.txt', 'a', encoding = 'utf-8')
with open("everything.xhtml", "r", encoding = "utf-8") as file:
    for line in file.readlines():
        if ',gen"' in line:
            f.write(line)


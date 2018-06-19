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

def get_data(file_name):
    with open("everything.xhtml", encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text


def pos_freq(text):
    pos = re.findall(r'\b[А-ЯЁA-Z]{2,}\b', text)
    pos_freq_d = {p: pos.count(p) for p in pos}
    return pos_freq_d

def dict_to_file(freq_dict):
    with open('pos_freq.csv', 'w') as f:
        f.write("POS \t Frequency\n")
        for p in freq_dict:
            f.write(p + '\t' + ' ' + str(freq_dict[p]) + '\n')
    print('Done.')


if __name__ == '__main__':
    raw = get_data("corpus-xml-example.xml")
    freq = pos_freq(raw)
    dict_to_file(freq)

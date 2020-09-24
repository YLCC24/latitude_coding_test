#!/usr/bin/python

import json
import csv

file = open('spec.json')
data = json.load(file)
file.close()

lista = data['ColumnNames']
listb = data['Offsets']
columns = tuple(map(tuple, zip(lista, list(map(int, listb)))))
with open('sample_file_load.txt', 'w', encoding='cp1252') as file:
    file.write(''.join([(field_name).ljust(width) for field_name, width in columns]))
    
def parse(x,l):
    address = 0
    for len in l:
        yield x[address:address + len]
        address += len

with open("sample_file_load.txt") as file:
    for line in file:
       with open('sample_csv.csv', 'w', encoding='utf-8') as csv_file:
          writer = csv.writer(csv_file, delimiter=',')
          writer.writerow(list(parse(line, list(map(int, listb)))))

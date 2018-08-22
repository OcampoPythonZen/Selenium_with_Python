#!/usr/bin/env python
# -- coding: utf-8 --
# -- coding: latin-1 --
import csv
import random

path="/home/eocampo/Escritorio/porque_pregunta_6.csv"
file=open(path,newline='')
reader=csv.reader(file)
data=[row for row in reader]
reader = csv.reader(data[0], delimiter=',')

newRandomList=[]
for row in reader:
    newRandomList.append(row)

finalString=random.choice(newRandomList)

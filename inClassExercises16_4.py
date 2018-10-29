#! /usr/bin/python3

f = open('atis.ex','r')

lines = f.readlines()

prepositions = []

for eachLine in lines:
    line = eachLine.split()
    for eachElement in line:
        if eachElement.endswith('/IN'):
            print(eachElement[:-3])
#! /usr/bin/python3

limit = input('Please give me a number: ')

table = []

for number in range(1, int(limit) + 1):
    temp = []
    for secondNumber in range(1, int(limit) + 1):
        temp.append(str(secondNumber + number))
    table.append(temp)

for eachLine in table:
    print("\t".join(eachLine))
#! /usr/bin/python3

limit = input('Please give me a number: ')

for number in range(1, int(limit) + 1):
    for secondNumber in range(1, int(limit) + 1):
        print(secondNumber + number, end='\t')
    print("")

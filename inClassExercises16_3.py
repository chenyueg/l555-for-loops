#! /usr/bin/python3

f = open('blonde.txt','r')

sentences =f.readlines()

print(sentences)

for eachSentence in sentences:
    sentence = eachSentence.split()
    for i in range(len(sentence)-1):
        print(sentence[i],sentence[i+1])
#! /usr/bin/python3

# Open and read in the file line by line

f = open('atis.ex', 'r')

lines = f.readlines()

np = []

sentenceNumber = 0

for eachLine in lines:

    # Print the sentence number

    if eachLine.strip() == "( END_OF_TEXT_UNIT )":
        sentenceNumber += 1
        if (sentenceNumber % 2) == 1:
            print("sentence " + str(sentenceNumber // 2))

    # Print the noun phrases in each sentence

    if "(NP" in eachLine:
        wordsInALine = eachLine.split()
        if len(wordsInALine) > 1:
            for eachWord in wordsInALine:
                wordAndTag = eachWord.split("/")
                if len(wordAndTag) == 2:
                    print(wordAndTag[0], end=" ")
            print("")
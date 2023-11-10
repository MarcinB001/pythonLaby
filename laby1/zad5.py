import re

def deleteWords(filePath, word):
    file = open(filePath, "r").read()
    file = re.sub(word, "", file)
    print(file)

def replaceWords(filePath, word, newWord):
    file = open(filePath, "r").read()
    file = re.sub(word, newWord, file)
    print(file)

path = "kopernik.txt"

deleteWords(path,"Nicolaus")
print("-----------------------------")
replaceWords(path, "Nicolaus", "Mikolaj")

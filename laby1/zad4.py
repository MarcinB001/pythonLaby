
def replace(filePath, word, newWord):
    file = open(filePath,"r")
    for line in file:
        if word in line:
                line = line.replace(word,newWord)
        print(line)



path = "kopernik.txt"


replace(path, "Nicolaus", "Mikolaj")

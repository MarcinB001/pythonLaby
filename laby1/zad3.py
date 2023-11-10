
def delete(filePath,word):
    file = open(filePath,"r")
    for line in file:
        if word in line:
                line = line.replace(word,"")
        print(line)



path = "kopernik.txt"


delete(path, "Nicolaus")

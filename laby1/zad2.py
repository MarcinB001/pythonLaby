import os

def printfiles(path):
    for x in os.listdir(path):
        if os.path.isfile(os.path.join(path, x)):
            print(x)
        else:
            printfiles(os.path.join(path, x))


printfiles("C:/dev")

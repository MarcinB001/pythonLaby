import os

devPath = "C:/dev"

i = 0

for x in os.listdir(devPath):
    if os.path.isfile(os.path.join(devPath, x)):
        i += 1

print(i)


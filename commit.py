import os

for i in range(10):
    # print(str(i) + ".txt")
    name = open(str(i) + ".txt", "w+")
    os.system("git add *")
    os.system("git commit -m \"hey\"")
    os.system("git push")

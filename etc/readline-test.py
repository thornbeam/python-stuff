import os, shutil
curDir = os.path.dirname(__file__)

tmpFile = open(curDir + "/test.csv", "r")
data = tmpFile.readlines()
tmpFile.close()

def readLines(data):
    if not os.path.exists(curDir + "/result"):
        os.mkdir(curDir + "/result")

    index = 0
    keys = []

    for line in data:
        line = line.strip("\n")

        if index == 0:
            for key in line.split(";"):
                keys.append(key)

            index += 1

        else:
            values = line.split(";")

            for i in range(len(values)):
                if values[i] == "":
                    values[i] = None

            assert len(keys) == len(values)

            for i in range(len(keys)):
                print(keys[i] + ":", values[i])

# model: save values!

readLines(data)

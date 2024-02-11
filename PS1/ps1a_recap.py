import time, os

def load_cows(filename):
    curDir = os.path.dirname(__file__)
    file = open(curDir + "/" + filename, "r")
    lines = file.readlines()
    cows = {}
    for line in lines:
        cow = line.strip().split(",")
        cows[cow[0]] = int(cow[1])
    return cows

cows = load_cows("ps1_cow_data_3.txt")
print(cows)

def greedy_cow_transport(cows, limit=10):
    """
    cows: dictionary
    """
    cows_sorted = sorted(cows.items(), key=lambda x:x[1], reverse=True)

    transports = []

    while len(cows_sorted) != 0:

        cows_sorted_copy = cows_sorted.copy()
        cows_transported = []
        restSpace = limit

        for cow in cows_sorted_copy:
            if cow[1] <= restSpace:
                cows_transported.append(cow)
                restSpace -= cow[1]
                cows_sorted.remove(cow)
                
        transports.append(cows_transported)

    return transports
                
print(greedy_cow_transport(cows))

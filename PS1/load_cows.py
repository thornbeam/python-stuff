import os

def load_cows(filename):
    """
    Read the contents of the given file. Assumes the file contents contain data in the form of comma-separated cow name, weight pairs, and return a dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    curDir = os.path.dirname(__file__)
    file = open(curDir + "/" + filename, "r")
    lines = file.readlines()
    cows = {}
    for line in lines:
        line = line.strip().split(",")
        cows[line[0]] = int(line[1])
    return cows
        
# cows = load_cows("ps1_cow_data.txt")
# print(cows)

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
        
cows = load_cows("ps1_cow_data.txt")
print(cows)


def brute_force_cow_transport(cows, avail):

    # create a list of cows 
    cows_list = []
    for item in cows.items():
        cows_list.append(item)

    trips = []

    def brute_force(cows_list, avail):
        """
        Returns list of trips
        """

        if len(cows_list) == 0 or avail == 0:
            trip = []

        elif cows_list[0][1] > avail:
            trip = brute_force(cows_list[1:], avail)

        else:
            nextCow = cows_list[0]

            trip = brute_force(cows_list[1:], avail - nextCow[1])
            trip.append(nextCow)

        trips.append(trip)

        transported = []
        for trip in trips:
            transported += trip

        for cow in transported:
            cows_list.remove(cow)

        if len(cows_list) == 0:
            return trips

        else:
            brute_force(cows_list, avail)

    return brute_force(cows_list, avail)

# print(brute_force_cow_transport(cows, 10))

# difference between yield and return 

def printResult_yield(S):
    """
    S a string
    """
    for i in S:
        if i == "e":
            yield i

test = printResult_yield("Test_printResult_yield")

print("How many 'e' in S:")
ans = 0
for i in test:
    print(i)
    ans += 1
print(ans, "times")

def printResult_return(S):
    for i in S:
        if i == "e":
            return i

print(printResult_return("Test_printResult_return"))

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)


from random import random
test = random()
print(test)
test *= 100
print(test)
test = round(test + 0.5)
print(test)
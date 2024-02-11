from ps1_partition import get_partitions
import time, os

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

def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to minimize the number of spaceship trips needed to transport all the cows. The returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    #1. As long as the current trip can fit another cow, add the largest cow that will fit to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows 

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows transported on a particular trip and overall list containing all the trips
    """

    cows_sorted = sorted(cows.items(), key=lambda x:x[1], reverse = True)
    # sorted list of cows with weights
    print("cows_sorted:", cows_sorted)

    cows_main = []
    # list of cow's transports

    cows_transported = {}
    # dictionary of cows already transported

    while len(cows_sorted) != 0:

        cows_sub = []
        restSpace = limit
        # list of cows at a transport
        cows_sorted_copy = cows_sorted.copy()

        for cow in cows_sorted_copy:
            # e.g., ("Betsy", 9)
            
            if cow[1] <= restSpace:
                # the cow's weight is smaller than limit
                cows_sub.append(cow)
                print("cows_sub", cows_sub)

                restSpace -= cow[1]
                print(restSpace)
                cows_sorted.remove(cow)
                print(cows_sorted, "\n")

        cows_main.append(cows_sub)
    print(cows_main, "\n")
    return cows_main

# greedy_cow_transport(cows)


def gen_subsets(cows_list):

    if len(cows_list) == 0:
        subs = [[]]

    else:
        latest = cows_list[-1]
        subs = gen_subsets(cows_list[:-1])
        tmp = []
        for element in subs:
            new_element = element + [latest]
            tmp.append(new_element)
        subs += tmp

    return subs

cows_list = []
for element in cows.items():
    cows_list.append(element)

cows_subsets = gen_subsets(cows_list)
print(cows_subsets)
print(len(cows_subsets))

print("------------")

def brute_force_cow_transport_test(cows, avail):
    """
    LEGACY: doesn't return the desired result!
    """

    # create a list of cows 
    cows_list = []
    for item in cows.items():
        cows_list.append(item)

    trips = []

    def generate_trip(cows_list, avail):

        if len(cows_list) == 0 or avail == 0:
            trip = []

        elif cows_list[0][1] > avail:
            trip = generate_trip(cows_list[1:], avail)

        else:
            nextCow = cows_list[0]

            trip = generate_trip(cows_list[1:], avail - nextCow[1])
            trip.append(nextCow)

        return trip


    def generate_trips(cows_list, avail):
        
        trips.append(generate_trip(cows_list, avail))

        transported = []
        for trip in trips:
            transported += trip

        for cow in transported:
            if cow in cows_list:
                cows_list.remove(cow)

        if len(cows_list) == 0:
            return trips

        else:
            return generate_trips(cows_list, avail)

    return generate_trips(cows_list, avail)


print(brute_force_cow_transport_test(cows, 10))

# use get_partitions

def listToDict(Dict):
    result = []
    for i in Dict.items():
        result.append(i)
    return result

cows_list = listToDict(cows)
print("cows_list:", cows_list)

def get_subsets(L, toPrint=False):

    if len(L) == 0:
        subs = [[]]

    else:
        last = L[-1]
        subs = gen_subsets(L[:-1])
        tmp = []
        for element in subs:
            # element is a list
            new_element = element + [last]
            tmp.append(new_element)

            if toPrint:
                print("element:", element)
                print("new_element:", new_element)
                print("tmp:", tmp)

        subs += tmp

    return subs

print("\n--- printing data with cows_list ---\n")
partitions = []
for partition in get_partitions(cows_list):
    partitions.append(partition)

print("     length of cows_list:", len(cows_list))
print("     length of partitions from cows_list:", len(partitions))
print("     length of powerset of cows_list:", len(gen_subsets(cows_list)))

print("\n--- printing data with testList[1, 2, 3, 4, 5] ---\n")
testList = [1, 2, 3, 4, 5]
partitions = []
for partition in get_partitions(testList):
    partitions.append(partition)
print("     length of testList[1, 2, 3, 4, 5]:", len(testList))
print("     length of partitions from testList [1, 2, 3, 4, 5]:", len(partitions))

print("     length of powerset of testList [1, 2, 3, 4, 5]:", len(get_subsets(testList)))

print("\n--- printing data with testList[1, 2, 3] ---\n")

print("     get_partitions:\n")
for partition in get_partitions([1, 2, 3]):
    print("         ", partition)

print("\n     gen_subsets:\n")
for subset in gen_subsets([1, 2, 3]):
    print("         ", subset)

print("\n--- printing data with testList[1, 2, 3, 4] ---\n")

print("     get_partitions:\n")
for partition in get_partitions([1, 2, 3, 4]):
    print("         ", partition)

def brute_force_cow_transport_with_partitions(cows, limit):
    """
    cows a dictionary of cows
    limit maximal weight for each single transport
    """

    cowsName_list = []
    for cow in cows.keys():
        cowsName_list.append(cow)

    all_partitions = get_partitions(cowsName_list)
    partitions_inLimit = []

    for setTrips in all_partitions:
        # setTrips e.g. [[2, 3], [1]]
        inLimit = True
        for singleTrip in setTrips:
            # trip e.g. [2, 3] or ['maggie', 'herman']
            totalWeight = 0
            for cowsName in singleTrip:
                totalWeight += cows[cowsName]
            if totalWeight > limit:
                inLimit = False
                break

        if inLimit:
            partitions_inLimit.append(setTrips)

    partitions_inLimit.sort(key=len)

    minLen = len(partitions_inLimit[0])
    partitions_final = []

    for partition in partitions_inLimit:
        if len(partition) == minLen:
            partitions_final.append(partition)
        else:
            break

    return partitions_final

transports_final = brute_force_cow_transport_with_partitions(cows, 10)
print(transports_final)
for t in transports_final:
    print(len(t))

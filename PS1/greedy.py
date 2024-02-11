from load_cows import load_cows
import time

def greedy_cow_transport(cows, limit=10, toPrint=False):
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
    if toPrint:
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
                restSpace -= cow[1]
                cows_sorted.remove(cow)

        cows_main.append(cows_sub)
        if toPrint:
            print("cows_main in while:", cows_main, "\n")

    return cows_main

cows = load_cows("ps1_cow_data.txt")

start = time.time()
print(greedy_cow_transport(cows, 10, False))
end = time.time()
print("time of algorithm:", end - start)

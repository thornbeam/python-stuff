from ps1_partition import get_partitions
from load_cows import load_cows
import time

cows = load_cows("ps1_cow_data.txt")

def brute_force_cow_transport_with_partitions(cows, limit, check=False):
    """
    cows a dictionary of cows
    limit maximal weight for each single transport
    """

    cowsName_list = []
    for cow in cows.keys():
        cowsName_list.append(cow)

    partitions_inLimit = []

    for setTrips in get_partitions(cowsName_list):
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
        else:
            continue

    partitions_inLimit.sort(key=len)
    if check:
        print("length of partitions_inLimit:", len(partitions_inLimit))

    minLen = len(partitions_inLimit[0])
    partitions_final = []

    for partition in partitions_inLimit:
        if len(partition) == minLen:
            partitions_final.append(partition)
        else:
            break

    return partitions_final

def test_brute_force(cows, limit, check=True):
    result = brute_force_cow_transport_with_partitions(cows, limit, check)
    print("length of partitions_final:", len(result))
    i = 0
    for partition in result:
        i += 1
        print("length of {}. partition:".format(i), len(partition))
start = time.time()
test_brute_force(cows, 10)
end = time.time()
print("time of algorithm:", end - start)

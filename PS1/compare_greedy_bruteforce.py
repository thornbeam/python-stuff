import time
from load_cows import load_cows
from brute_force import brute_force_cow_transport_with_partitions
from greedy import greedy_cow_transport

start = time.time()
cows = load_cows("ps1_cow_data.txt")
end = time.time()
print("time for load_cows:", end - start)

start = time.time()
brute_force = brute_force_cow_transport_with_partitions(cows, 10)
end = time.time()
time_bruteforce = end - start
print("time for brute_force:", time_bruteforce)

start = time.time()
greedy = greedy_cow_transport(cows, 10)
end = time.time()
time_greedy = end - start
print("time for greedy:", time_greedy)

if time_greedy == time_bruteforce:
    print("same")
elif time_greedy < time_bruteforce:
    print("greedy faster")
else:
    print("brute force faster")

"""
--------------------
--------------------
Partitions Generator
--------------------
--------------------

Takes as input a list
Returns a generator that contains all the possible partitions of this list from 0-partitions to n-partitions (n is the length of the list):
    means for [1,2,3]:
        returns
            [[1, 2, 3]]
            [[2, 3], [1]]
            [[1, 3], [2]]
            [[3], [1, 2]]
            [[3], [2], [1]]
"""

def partitions(set_):
    if not set_:
        # what is with 'if not set_'?
        yield []
        return
        # what does this return do?
    for i in range(2**len(set_)//2):
        # why the range of 2 ** len(set_) // 2?
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            # mean of [1&1]
            i >>= 1
            # mean of >>
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

def first_n(n):
    """
    Build and return a list
    """
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1

    return nums

sum_of_first_n = sum(first_n(1000000))
print(sum_of_first_n)
# It builds the full list in memory. So, we resort to the generator pattern.

testList = [1, 2, 3]
testIterList = iter(testList)
while True:
    item = next(testIterList, "end")
    if item == "end":
        break
    print(item)

testIterList = iter(testList)
print("1.", next(testIterList))
print("2.", next(testIterList))
print("3.", next(testIterList))
# print("4.", next(testIterList))

class first_n(object):

    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()


def get_subsets(L, toPrint=False):

    if len(L) == 0:
        subs = [[]]

    else:
        last = L[-1]
        subs = get_subsets(L[:-1])
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

def gen_list(n):
    """
    n an integer for length of generated list
    """
    result = []
    for i in range(n):
        result.append(i)
    return result

if __name__ == "__main__":
    for n in range(7):
        result = gen_list(n)
        print("powerset of", str(result) + ":")
        print(get_subsets(result))

import itertools
k = 1
lst1 = list()
lst2 = list()
for m in range(1,6):
    if(k == 5):
        break

    lst1.append(3*k - 2)
    lst1.append(3*k - 1)
    lst1.append(3 * k)
    lst2.append(3*m - 2)
    lst2.append(3*m - 1)
    lst2.append(3*m)
    somelists = [lst1, lst2]
    for element in itertools.product(*somelists):
        print(element)
    lst1.pop()
    lst1.pop()
    lst1.pop()
    lst2.pop()
    lst2.pop()
    lst2.pop()
    k = k + 1
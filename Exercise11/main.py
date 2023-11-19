# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import operator


def most_frequent(lst):
    counter = 0
    num = lst[0]

    for i in lst:
        curr_frequency = lst.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


if __name__ == '__main__':
    lst= ["a", "a", "b", "c"]
    print(most_frequent(lst))

    dict1 = {"a,b": 0.4, "b,c": 0.5, "a,c": 0.3}

    # maxdiagnoser = max(dict1.iteritems(), key=operator.itemgetter(1))[0]
    maxdiagnoser = max(dict1.items(), key=operator.itemgetter(1))[0]
    print(maxdiagnoser)
import random


def quicksort(iterable):
    if len(iterable) <= 1:
        return iterable

    pivot = iterable.pop()
    lesser, greater, same = [], [], [pivot]

    for item in iterable:
        if item < pivot:
            lesser.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            greater.append(item)

    return quicksort(lesser) + same + quicksort(greater)


if __name__ == '__main__':
    array = [random.randint(0, 50) for i in xrange(50)]
    print quicksort(array)

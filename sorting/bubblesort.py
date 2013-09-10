import random


def bubblesort(iterable):
    limit = len(iterable)

    for i in xrange(len(iterable)):
        for j in xrange(1, limit):
            if iterable[j - 1] > iterable[j]:
                iterable[j], iterable[j - 1] = iterable[j - 1], iterable[j]
        limit -= 1

    return iterable


if __name__ == '__main__':
    array = [random.randint(0, 50) for i in xrange(5)]

    print bubblesort(array)

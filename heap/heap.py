import datetime
import random
import math


class Heap(object):

    def __init__(self, iterable=None):
        self.items = []

        if iterable:
            self._build_heap(iterable)

    def _build_heap(self, iterable):
        for item in list(iterable):
            self.add(item)

    def _balance_up(self, index):
        if index == 0:
            return

        parent = int(math.floor((index - 1) / 2))
        if self.items[parent] < self.items[index]:
            self.items[parent], self.items[index] = self.items[index], self.items[parent]
            self._balance_up(parent)

    def _balance_down(self, index=0):
        if index >= len(self.items):
            return

        last_index = len(self.items) - 1
        left, right = (index * 2) + 1, (index * 2) + 2

        largest = index

        if left <= last_index and self.items[left] > self.items[index]:
            largest = left

        if right <= last_index and self.items[right] > self.items[largest]:
            largest = right

        if index is not largest:
            self.items[largest], self.items[index] = self.items[index], self.items[largest]
            self._balance_down(largest)

    def add(self, value):
        self.items.append(value)
        self._balance_up(len(self.items) - 1)

    def pop(self):
        last_index = len(self.items) - 1
        self.items[0], self.items[last_index] = self.items[last_index], self.items[0]

        item = self.items.pop()

        self._balance_down()

        return item

    def is_empty(self):
        return len(self.items) == 0


def heapsort(iterable):
    heap = Heap(iterable)
    return [heap.pop() for i in xrange(len(heap.items))]


if __name__ == '__main__':
    array = [random.randint(0, 50) for r in xrange(10)]

    start = datetime.datetime.now()
    heapsort(array)
    print datetime.datetime.now() - start

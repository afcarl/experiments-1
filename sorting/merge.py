def mergesort(iterable):
    if len(iterable) <= 1:
        return iterable

    pivot = len(iterable) / 2

    left = mergesort(iterable[pivot:])
    right = mergesort(iterable[:pivot])
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


if __name__ == '__main__':
    print mergesort([5, 4, 1, 8, 7, 2, 6])

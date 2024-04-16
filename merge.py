from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()

def mergesort(b, moves=0, comparisons=0):
    n = len(b)
    if n < 2:
        return b, moves, comparisons
    else:
        mid = n // 2
        left = b[:mid]
        right = b[mid:]

        left, moves, comparisons = mergesort(left, moves, comparisons)
        right, moves, comparisons = mergesort(right, moves, comparisons)

        i = j = k = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                b[k] = left[i]
                i += 1
            else:
                b[k] = right[j]
                j += 1
            k += 1
            moves += 1

        while i < len(left):
            b[k] = left[i]
            i += 1
            k += 1
            moves += 1

        while j < len(right):
            b[k] = right[j]
            j += 1
            k += 1
            moves += 1

    return b, moves, comparisons

sorted_a, moves, comparisons = mergesort(b)
print('Sorted array is:', sorted_a)
print('Jumlah perpindahan data:', moves)
print('Jumlah perbandingan data:', comparisons)

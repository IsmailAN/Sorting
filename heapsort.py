from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()

def heapify(b, n, i, comparisons, moves):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        comparisons += 1
        if b[i] < b[l]:
            largest = l

    if r < n:
        comparisons += 1
        if b[largest] < b[r]:
            largest = r

    if largest != i:
        moves += 1
        b[i], b[largest] = b[largest], b[i]
        moves, comparisons = heapify(b, n, largest, comparisons, moves)

    return moves, comparisons

def heapSort(b):
    n = len(b)
    moves = 0
    comparisons = 0

    for i in range(n // 2, -1, -1):
        moves, comparisons = heapify(b, n, i, comparisons, moves)

    for i in range(n - 1, 0, -1):
        b[i], b[0] = b[0], b[i]
        moves, comparisons = heapify(b, i, 0, comparisons, moves)

    return b, moves, comparisons

sorted_arr, moves, comparisons = heapSort(b)
end = timeit.default_timer()
print('Sorted array is: ',b)
print("Jumlah perpindahan data:", moves)
print("Jumlah perbandingan data:", comparisons)
print("waktu : ",end - start)
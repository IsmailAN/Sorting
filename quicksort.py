from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()


def quicksort(b):
    if len(b) <= 1:
        return b, 0, 0
    else:
        pivot = b[0]
        less_than_pivot = [x for x in b[1:] if x <= pivot]
        greater_than_pivot = [x for x in b[1:] if x > pivot]
        sorted_less, moves_less, comps_less = quicksort(less_than_pivot)
        sorted_greater, moves_greater, comps_greater = quicksort(greater_than_pivot)
        moves = len(less_than_pivot) + len(greater_than_pivot) + moves_less + moves_greater
        comparisons = len(b) - 1 + comps_less + comps_greater
        return sorted_less + [pivot] + sorted_greater, moves, comparisons
    
# Contoh penggunaan
sorted_b, moves, comparisons = quicksort(b)
end = timeit.default_timer()
print("Sorted bay:", sorted_b)
print("Total perpindahan data:", moves)
print("Total perbandingan data:", comparisons)
print("waktu :",end-start)

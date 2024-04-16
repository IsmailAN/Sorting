from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()


def countingSortAlgo(b, position, counts):
    n = len(b)
    result = [0] * n
    count = [0] * 10  
    for j in range(0, n):
        counts['comparison'] += 1
        element = b[j] // position
        count[element % 10] += 1  # Calculating the cumulative count
    for j in range(1, 10):
        count[j] += count[j - 1]  # Sorting the elements
    i = n - 1
    while i >= 0:
        element = b[i] // position
        result[count[element % 10] - 1] = b[i]
        count[element % 10] -= 1
        i -= 1
    for j in range(0, n):
        b[j] = result[j]
        counts['move'] += 1


def radixSortAlgo(b, counts):  # Acquiring the largest element in the bay
    maximum = max(b)  # Using counting sort to sort digit by digit
    position = 1
    while maximum // position > 0:
        countingSortAlgo(b, position, counts)
        position *= 10


counts = {'comparison': 0, 'move': 0}
radixSortAlgo(b, counts)
print("Sorted bay:", b)
print("Total perpindahan data:", counts['move'])
print("Total perbandingan data:", counts['comparison'])

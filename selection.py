from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()

def selection():
    move = 0
    comparison = 0
    for i in range(len(b)):
        min_idx = i
        for j in range(i+1, len(b)):
            comparison += 1
            if b[j] < b[min_idx]:
                min_idx = j
        print("min_idx = ",min_idx)
        if min_idx != i:
            b[i], b[min_idx] = b[min_idx], b[i]
            move += 1
    print(b)
    print(f"Total perpindahan data: {move}")
    print(f"Total perbandingan data: {comparison}")

selection()
end = timeit.default_timer()
print("waktu : ",end - start)
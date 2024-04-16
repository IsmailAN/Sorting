from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()

def insertion():
    move = 0
    comparison = 0
    for i in range(1, len(b)):
        nilai = b[i]
        j = i - 1
        while j >= 0 and nilai < b[j]:
            comparison += 1
            b[j + 1] = b[j]
            j = j - 1
            move += 1
        b[j + 1] = nilai
    print(b)
    print(f"Total perpindahan data: {move}")
    print(f"Total perbandingan data: {comparison}")

insertion()
end = timeit.default_timer()
print("waktu : ",end - start)

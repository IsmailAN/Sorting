from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()

def bubblesort(b):
    move = 0
    comparison = 0
    for j in range(len(b)-1): #model biasa
        for i in range(len(b)-1-j):
            comparison += 1
            if b[i]>b[i+1]:
                b[i],b[i+1]=b[i+1],b[i]
                move +=1
    print(b)
    print(f"Total perpindahan data: {move}")
    print(f"Total perbandingan data: {comparison}")
 
bubblesort(b)
end = timeit.default_timer()

print("waktu : ",end - start)
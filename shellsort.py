from random import randint
import timeit

start = timeit.default_timer()
a = []
for i in range(1500):
    a.append(randint(1,100))

b = a.copy()

def shellSort(b):
    swaps = 0
    comparisons = 0
    gap=len(b)//2
    
    
    while gap>0:
        j=gap
        while j<len(b):
            i=j-gap 
            
            while i>=0:
                comparisons += 1
                if b[i+gap]>b[i]:
                    break
                else:
                    b[i+gap],b[i]=b[i],b[i+gap]
                    swaps += 1

                i=i-gap
            j+=1
        gap=gap//2

    return swaps, comparisons

swaps, comparisons = shellSort(b)
print("sorted array",b)
print("Jumlah perpindahan data:", swaps)
print("Jumlah perbandingan data:", comparisons)

stop = timeit.default_timer()
print('Time: ', stop - start)

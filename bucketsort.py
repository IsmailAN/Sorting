import random
import time

def bucket_sort(arr):
    start_time = time.time()
    n = len(arr)
    bucket_size = 10
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / bucket_size

    # Create buckets
    buckets = [[] for _ in range(bucket_size)]

    # Add elements into buckets
    comparisons = 0
    moves = 0
    for num in arr:
        index = int((num - min_value) / bucket_range)
        comparisons += 1
        if index != bucket_size:
            moves += 1
            buckets[index].append(num)
        else:
            moves += 1
            buckets[bucket_size - 1].append(num)

    # Sort individual buckets
    for i in range(bucket_size):
        buckets[i].sort()

    # Concatenate buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    end_time = time.time()
    return sorted_arr, end_time - start_time, comparisons, moves

# Generate a random list of 100,000 numbers
arr = [random.randint(1, 100) for _ in range(1500)]

# Perform bucket sort
sorted_arr, execution_time, comparisons, moves = bucket_sort(arr)

# Print execution time, comparisons, and moves
print(f"Execution time: {sorted_arr} seconds")
print(f"Execution time: {execution_time} seconds")
print(f"Jumlah perbandingan data: {comparisons}")
print(f"Jumlah perpindahan data: {moves}")

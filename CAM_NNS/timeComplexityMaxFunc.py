import random
import timeit
import matplotlib.pyplot as plt

''' This code simply test max functions time complexity with problem size,  N  which is O(N) '''


def find_max(arr):
    return max(arr)

# Define a range of array sizes (N) for testing
array_sizes = [10, 50, 100, 500, 1000, 2000, 4000, 5000,  6000, 10000, 15000, 20000,  25000, 30000, 35000, 40000]

# Generate a random array for each size
random_arrays = [[random.uniform(0,1) for _ in range(size)] for size in array_sizes]

# Measure execution time for each array size
execution_times = []

for arr in random_arrays:
    time_taken = timeit.timeit(lambda: find_max(arr), number=10)
    execution_times.append(time_taken*1e6)

# Plot the time complexity curve
plt.plot(array_sizes, execution_times, marker='o')
plt.xlabel('Array Size (N)')
plt.ylabel('Execution Time (us)')
plt.title('Time Complexity of max() Function')
plt.show()

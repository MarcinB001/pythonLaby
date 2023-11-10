import multiprocessing
import random


def parallel_sort(arr, processes):
    if len(arr) <= 1:
        return arr

    split_size = len(arr) // processes

    small_arrays = [arr[i:i + split_size] for i in range(0, len(arr), split_size)]

    with multiprocessing.Pool(processes) as pool:
        sorted_small_arrays = pool.map(sorted, small_arrays)

    return sorted(sum(sorted_small_arrays, []))


if __name__ == '__main__':
    n = random.sample(range(0, 1000), 50)
    print(n)

    print(parallel_sort(n, 10))

from zad2 import parallel_sort
import random
import datetime

import matplotlib.pyplot as plt


if __name__ == '__main__':
    sizes = [1000, 10000, 100000, 1000000]
    x = [1, 2, 4, 8]

    for size in sizes:
        n = random.sample(range(0, 10000000), size)

        times = []
        for i in x:
            start = datetime.datetime.now()
            parallel_sort(n, i)
            times.append(datetime.datetime.now() - start)

        for i in range(len(x)):
            print(f"Czas dla {size} elementów przy {x[i]} procesach: {times[i]}")

        plt.plot(x, [time.total_seconds() for time in times], marker='o', label=f"{size} elementów")

    plt.title('Czas sortowania w zależności od liczby procesów')
    plt.xlabel('Liczba procesów')
    plt.ylabel('Czas')
    plt.legend(title='Rozmiar tablicy')
    plt.show()
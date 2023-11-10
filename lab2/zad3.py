from zad2 import parallel_sort
import random
import datetime

import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = random.sample(range(0, 10000000), 10000000)  # tabblica 10 000 000 liczb
    # print(n)

    x = [1, 2, 4, 8]

    times = []
    for i in x:
        start = datetime.datetime.now()
        parallel_sort(n, i)
        times.append(datetime.datetime.now() - start)

    for i in range(len(x)):
        print("Czas przy " + x[i].__str__() + " procesach: " + times[i].__str__())

    plt.plot(x, [time.total_seconds() for time in times], marker='o')
    plt.title('Czas sortowania w zależności od liczby procesów')
    plt.xlabel('Liczba procesów')
    plt.ylabel('Czas')

    plt.show()
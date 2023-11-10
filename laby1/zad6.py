import random


def bubble_sort(numbers):
    n = len(numbers)

    while n > 1:
        change = False
        for l in range(0, n - 1):
            if numbers[l] > numbers[l + 1]:
                numbers[l], numbers[l + 1] = numbers[l + 1], numbers[l]
                change = True

        n -= 1
        if change == False: break

    return numbers


def instertion_sort(numbers):
    for i in range(1, len(numbers)):
        temp = numbers[i];
        j = i - 1;
        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = temp
    return numbers


n = random.sample(range(0, 100), 10)
print(n)

print("bubble_sort:")
print(bubble_sort(n.copy()))

print("instertion_sort:")
print(instertion_sort(n.copy()))

print("python sort:")
print(sorted(n))

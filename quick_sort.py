import random as r
import sys

def quick_sort(lst, p, r):
    if p < r:
        index = partition(lst, p, r)

        quick_sort(lst, p, index - 1)
        quick_sort(lst, index + 1, r)


def partition(lst, p , r):
    pivot = lst[r]
    i = p - 1
    print(p)
    for j in range(p, r):
        if lst[j] <= pivot:
            i += 1
            a = lst[i]
            b = lst[j]
            lst[i] = b
            lst[j] = a
        print(lst)
    a = lst[i + 1]
    b = lst[r]
    lst[i + 1] = b
    lst [r] = a
    return i + 1

def main():
    if len(sys.argv) < 4:
        print("usage: quick_sort.py <length of rand number list> <lower bound for rand numbers> "
              "<upper bound for random numbers>")
        return

    numbers = [r.randint(int(sys.argv[2]), int(sys.argv[3])) for _ in range(int(sys.argv[1]))]
    print(numbers)
    quick_sort(numbers, 0, len(numbers) - 1)
    print(numbers)

if __name__ == '__main__':
    main()
import random as r
import sys


def merge_sort(lst):
    """
    sorts numbers in ascending order
    :param lst: list to sort
    :return: sorted list
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """
    helper function to merge 2 lists in sorted order
    :param left: left list
    :param right: right list
    :return: merged list
    """
    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    while left:
        merged.append(left[0])
        left = left[1:]
    while right:
        merged.append(right[0])
        right = right[1:]

    return merged


def main():
    if len(sys.argv) < 4:
        print("usage: merge_sort.py <length of rand number list> <lower bound for rand numbers> "
              "<upper bound for random numbers>")
        return

    numbers = [r.randint(int(sys.argv[2]), int(sys.argv[3])) for _ in range(int(sys.argv[1]))]
    print(numbers)
    merged = merge_sort(numbers)
    print(merged)


if __name__ == '__main__':
    main()

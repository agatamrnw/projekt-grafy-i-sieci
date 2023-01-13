import random
import time


def menu():
    try:
        print("Would you like to input data or import from a file? Or you would like data to be auto completed [k/f/a]")
        choice = input()
        if choice == "k":
            key_board(0)
        elif choice == 'a':
            autocomplete()
        elif choice == 'f':
            readfile()
        else:
            print("Wrong! Try again [k/f/a]")
            menu()
    except:
        print("Wrong! Try again[k/f/a]")
        menu()


def key_board(i):
    try:

        print("Input numbers:")
        while i < 1000:
            data.append(int(input()))
            i += 1
    except:
        print("The last input wasn't a number!")
        key_board(i)


def autocomplete():
    for i in range(0, 1000000):
        data.append(random.randint(-10000, 10000))


def readfile():
    try:
        print("Enter name of the file:")
        name = input()
        f = open(name)

        try:
            while f.readline():
                data.append(int(f.readline()))
            f.close()
        except:
            print("An error has occurred!")
            menu()

    except:
        print("Wrong name! Try for example name.txt")
        readfile()


def partition_random(a, left_index, right_index):
    pivot = a[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[left_index], a[i - 1] = a[i - 1], a[left_index]
    return i - 1


def quicksort_random(a, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        a[pivot], a[left] = (a[left], a[pivot])  # switches the pivot with the left most bound
        pivot_index = partition_random(a, left, right)
        quicksort_random(a, left, pivot_index)  # recursive quicksort to the left of the pivot point
        quicksort_random(a, pivot_index + 1, right)


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


# function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quicksort(array, low, pi - 1)

        quicksort(array, pi + 1, high)


def mergesort(array):
    if len(array) > 1:

        r = len(array) // 2
        lo = array[:r]
        m = array[r:]

    # Sort the two halves
        mergesort(lo)
        mergesort(m)

        i = j = k = 0

    # Until we reach either end of either L or M, pick larger among
    # elements L and M and place them in the correct position at A[p..r]
        while i < len(lo) and j < len(m):
            if lo[i] < m[j]:
                array[k] = lo[i]
                i += 1
            else:
                array[k] = m[j]
                j += 1
            k += 1

    # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
        while i < len(lo):
            array[k] = lo[i]
            i += 1
            k += 1

        while j < len(m):
            array[k] = m[j]
            j += 1
            k += 1


data = []
menu()

try:
    print("Unsorted Array")
    print(data)

    data1 = data
    data2 = data

    size = len(data)

    start1 = time.time()
    quicksort(data, 0, size - 1)
    end1 = time.time()
    total1 = end1-start1

    print('Sorted data:')
    print(data)

    start2 = time.time()
    quicksort_random(data1, 0, size - 1)
    end2 = time.time()
    total2 = end2 - start2

    start3 = time.time()
    mergesort(data2)
    end3 = time.time()
    total3 = end3-start3

    print("Quicksort with median pivot {0} s".format(total1))
    print("Quicksort with random pivot {0} s".format(total2))
    print("Mergesort {0} s".format(total3))

    if total1 < total2 and total1 < total3:
        print("Quicksort with median pivot is the most effective")
    elif total2 < total1 and total2 < total3:
        print("Quicksort with random pivot is the most effective")
    elif total3 < total1 and total3 < total2:
        print("Mergesort is the most effective")
    elif total1 == total2 and total2 == total3:
        print("All algorithms have the same efficiency")
    elif total1 == total2:
        print("Both quicksort algorithms have the same efficiency")
    elif total1 == total1:
        print("Quicksort with median pivot and mergesort have the same efficiency")
    elif total2 == total3:
        print("Quicksort with random pivot and mergesort have the same efficiency")
except:
    print('Something has fucked up :c')

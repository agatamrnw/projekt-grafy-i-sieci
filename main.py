import random


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


def menu():
    try:
        print("Would you like to input data or import from a file? [k/f]")
        chose = input()
        if chose == "k":
            key_board(0)
    except:
        print("Wrong! Try again[k/f]")
        menu()


data = []


def key_board(i):
    try:

        print("Input numbers:")
        while i < 12:
            data.append(int(input()))
            i += 1
    except:
        print("The last input wasn't a number!")
        key_board(i)



menu()

try:
    print("Unsorted Array")
    print(data)

    size = len(data)

    quicksort(data, 0, size - 1)

    print('QuickSort:')
    print(data)

except:
    print('Something has fucked up :c')


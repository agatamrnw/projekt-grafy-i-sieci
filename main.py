import random
import time
from tkinter import *


root = Tk()
j = 0
data = []
root['bg'] = '#FFF4F4'
root.title('Compare three sorting algorithms')
root.geometry('608x320')
root.resizable(width=False, height=False)
photo = PhotoImage(file='snake.png')
root.iconphoto(False, photo)
l1 = Label(root, text="Would you like to input data or load from file?", font=("Montserrat", 16),
           bg='#FFF2F2', foreground='#241414')

l1.grid(column=0, row=0, columnspan=3, padx=80, pady=60)
# l1.pack()
l2 = Label(text="Input numbers please:", font=("Montserrat", 16),
           bg='#FFF2F2', foreground='#241414')
btn1 = Button(root, text='Keyboard', bg='#D0ADA7', foreground='#241414', command=lambda: key(),
              activebackground='#FFC8AF')
btn1.grid(column=0, row=1, columnspan=1, padx=96, pady=0)
btn2 = Button(root, text='Autocomplete', bg='#D0ADA7', foreground='#241414', command=lambda: autocomplete(),
              activebackground='#FFC8AF')
btn2.grid(column=1, row=1, columnspan=1, padx=0, pady=0)
btn3 = Button(root, text='Load from file', bg='#D0ADA7', foreground='#241414', command=lambda: file(),
              activebackground='#FFC8AF')
btn3.grid(column=2, row=1, columnspan=1, padx=96, pady=0)
l5 = Label(text="Input file's name:", font=("Montserrat", 16),
           bg='#FFF2F2', foreground='#241414')
key_check = Entry(root)
file_check = Entry(root)
btn4 = Button(text='Submit', bg='#D0ADA7', foreground='#241414', command=lambda: key_valid(),
              activebackground='#FFC8AF')
btn5 = Button(text='Submit', bg='#D0ADA7', foreground='#241414', command=lambda: file_valid(),
              activebackground='#FFC8AF')
l6 = Label(text="Invalid file's name:", font=("Montserrat", 16),
           bg='#FFF2F2', foreground='#241414')
l7 = Label(text="Invalid data:", font=("Montserrat", 16),
           bg='#FFF2F2', foreground='#241414')


def key():
    l1.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    l2.grid(column=0, row=0, columnspan=3, padx=80, pady=60)
    key_check.grid(row=1, column=1)
    btn4.grid(row=1, column=2)


def key_valid():

    global j
    if key_check.get().isdigit() or (key_check.get()[1:].isdigit() and key_check.get()[0] == '-'):

        key_board()
    else:
        key_check.delete(0, 'end')

        l4 = Label(text="Invalid input", font=("Montserrat", 16),
                   bg='#FFF2F2', foreground='#241414')
        l4.grid(column=0, row=2)
        l4.destroy()


def key_board():
    global j
    if j < 10:
        data.append(int(key_check.get()))
        key_check.delete(0, 'end')
        j += 1
    else:
        key_check.delete(0, 'end')
        sort()


def file():
    l1.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    l5.grid(column=0, row=0, columnspan=3, padx=80, pady=60)
    file_check.grid(row=1, column=1)
    btn5.grid(row=1, column=2)


def file_valid():
    try:
        name = file_check.get()
        file_check.delete(0, 'end')
        f = open(name)
        readfile(f)
    except:
        l6.grid(row=3, column=0)
        valid_flag = False


def autocomplete():
    for i in range(0, 1000000):
        data.append(random.randint(-10000000000, 1000000000))
    sort()


def readfile(n):
    try:
        while n.readline():
            data.append(int(n.readline()))
        n.close()
        sort()
    except:
        l7.grid(row=3, column=0)


def sort():
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    l7.destroy()
    data1 = data
    data2 = data
    file_check.destroy()
    size = len(data)
    btn5.destroy()
    start1 = time.time()
    quicksort(data, 0, size - 1)
    end1 = time.time()
    total1 = end1 - start1

    start2 = time.time()
    quicksort_random(data1, 0, size - 1)
    end2 = time.time()
    total2 = end2 - start2

    start3 = time.time()
    mergesort(data2)
    end3 = time.time()
    total3 = end3 - start3
    result(total1, total2, total3)


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


def result(t1, t2, t3):
    l1.destroy()
    l2.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    l5.destroy()
    l6.destroy()
    btn5.destroy()
    btn4.destroy()
    key_check.destroy()
    qm = "Quicksort with median pivot {0} s".format(t1)
    qr = "Quicksort with random pivot {0} s".format(t2)
    m = "Mergesort {0} s".format(t3)
    lqm = Label(root, text=qm, font=("Montserrat", 12),
                bg='#FFF2F2', foreground='#241414', justify='center')
    lqm.grid(column=3, row=1, columnspan=3, sticky='e')
    lqr = Label(root, text=qr, font=("Montserrat", 12),
                bg='#FFF2F2', foreground='#241414', justify='center')
    lqr.grid(column=3, row=2, columnspan=3, sticky='e')
    lm = Label(root, text=m, font=("Montserrat", 12),
               bg='#FFF2F2', foreground='#241414', justify='center')
    lm.grid(column=3, row=3, columnspan=3, sticky='e')
    if t1 < t2 and t1 < t3:
        lbl = Label(root, text="Quicksort with median pivot\n is the most effective", font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')

    elif t2 < t1 and t2 < t3:
        lbl = Label(root, text="Quicksort with random pivot \nis the most effective", font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')

    elif t3 < t1 and t3 < t2:
        lbl = Label(root, text="Mergesort is the most effective", font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')

    elif t1 == t2 and t2 == t3:
        lbl = Label(root, text="All algorithms have the same efficiency",
                    font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')

    elif t1 == t2:
        lbl = Label(root, text="Both quicksort algorithms have the same efficiency",
                    font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')

    elif t1 == t3:

        lbl = Label(root, text="Quicksort with median pivot\n and mergesort have the same efficiency",
                    font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')
    elif t2 == t3:
        lbl = Label(root, text="Quicksort with random pivot \n and mergesort have the same efficiency",
                    font=("Montserrat", 16),
                    bg='#FFF2F2', foreground='#241414', justify='center')
        lbl.grid(column=3, row=0, columnspan=3, padx=80, pady=60, sticky='e')


root.mainloop()
print(data)



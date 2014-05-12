# -*- coding: utf-8 -*-
__author__ = 'boqingfu'


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


def insert_sort(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array


def select_sort(array):
    for i in range(len(array) - 1):
        index = i
        for j in range(i, len(array)):
            if array[j] < array[index]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array


def ins_for_shell(l, n, step):
    for i in range(0, n, step):
        for j in range(i, 0, -step):
            if l[j] < l[j - step]:
                l[j], l[j - step] = l[j - step], l[j]
            else:
                break
    return l


def shell_sort(l):
    i = len(l) / 2
    while i > 2:
        for j in range(i):
            ins_for_shell(l, len(l) - j, i)
        i = i / 2
    ins_for_shell(l, len(l), 1)
    return l


def quick_sort(l):
    return l if len(l) <= 1 else quick_sort([x for x in l[1:] if x < l[0]]) + [l[0]] + quick_sort(
        [x for x in l[1:] if x >= l[0]])


def merge_sort(alist):
    # print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    # print("Merging ", alist)


def heap_adjust(data, s, m):
    if 2 * s > m:
        return
    temp = s - 1
    if data[2 * s - 1] > data[temp]:
        temp = 2 * s - 1
    if 2 * s <= m - 1 and data[2 * s] > data[temp]:
        temp = 2 * s
    if temp <> s - 1:
        data[s - 1], data[temp] = data[temp], data[s - 1]
        heap_adjust(data, temp + 1, m)


def heap_sort(data):
    m = len(data) / 2
    for i in range(m, 0, -1):
        heap_adjust(data, i, len(data))
    data[0], data[-1] = data[-1], data[0]
    for n in range(len(data) - 1, 1, -1):
        heap_adjust(data, 1, n)
        data[0], data[n - 1] = data[n - 1], data[0]


if __name__ == "__main__":
    arr = [20, 4, 10, 5, 7, 12]
    print "bubble_sort"
    print bubble_sort(arr)
    print "*" * 22

    arr = [20, 4, 10, 5, 7, 12]
    print "insert_sort"
    print insert_sort(arr)
    print "*" * 22

    arr = [20, 4, 10, 5, 7, 12]
    print "select_sort"
    print select_sort(arr)
    print "*" * 22

    arr = [20, 4, 10, 5, 7, 12]
    print "shell_sort"
    print shell_sort(arr)
    print "*" * 22

    arr = [20, 4, 10, 5, 7, 12]
    print "quick_sort"
    print quick_sort(arr)
    print "*" * 22

    arr = [20, 4, 10, 5, 7, 12]
    print "merge_sort"
    merge_sort(arr)
    print arr
    print "*" * 22

    arr = [20, 4, 10, 5, 7, 12]
    print "heap_sort"
    heap_sort(arr)
    print arr
    print "*" * 22


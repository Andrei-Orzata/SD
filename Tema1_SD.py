from timeit import default_timer as timer
from random import randint, choice
from math import log, floor


def BubbleSort(X):
    global start, time_limit
    for i in range(len(X)):
        if timer() - start < time_limit:
            for j in range(0, len(X) - 1 - i):
                if X[j] > X[j + 1]:
                    X[j], X[j + 1] = X[j + 1], X[j]
        else:
            return []
    return X


def CountSort(X):
    MAX = max(X)
    if max(X) > 999999:
        print("Not enough memory!")
        return []
    else:
        List = []
        final = []
        for i in range(MAX + 1):
            List.append(0)
        for nr in X:
            List[nr] += 1
        for i in range(MAX + 1):
            for j in range(List[i]):
                final.append(i)
        return final


def Interclasare(st, dr):
    i = j = 0
    final = []
    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            final.append(st[i])
            i = i + 1
        else:
            final.append(dr[j])
            j += 1
    final.extend(dr[j:])
    final.extend(st[i:])
    return final


def MergeSort(X):
    if len(X) <= 1:
        return X
    else:
        return Interclasare(MergeSort(X[len(X) // 2:]), MergeSort(X[:len(X) // 2]))


def first(X):
    return X[0]


def middle(X):
    return X[len(X) // 2]


def Median_pivot(X):
    if len(X) <= 5:
        return sorted(X)[len(X) // 2]
    sublists = [sorted(X[i:i + 5]) for i in range(0, len(X), 5)]
    median = [sl[len(sl) // 2] for sl in sublists]
    return Median_pivot(median)


def QuickSort(X, start, end, f_pivot=Median_pivot):
    i = start
    j = end
    pivot = f_pivot(X[start:end])
    while i <= j:
        while i < end and X[i] < pivot:
            i = i + 1
        while X[j] > pivot and j >= start:
            j = j - 1
        if i <= j:
            X[i], X[j] = X[j], X[i]
            i = i + 1
            j = j - 1
    if i < end:
        QuickSort(X, i, end)
    if j > start:
        QuickSort(X, start, j)
    return X


def RadixSort(X):
    base = 10
    placement = 1
    lenght = floor(log(max(X), base)) + 1
    for i in range(lenght):
        buckets = [[] for ind in range(base)]
        for i in X:
            tmp = i // placement
            buckets[tmp % base].append(i)
        k = 0
        for ind in range(base):
            for i in buckets[ind]:
                X[k] = i
                k += 1
        placement *= base
    return X


def isSorted(X):
    for i in range(len(X) - 1):
        if X[i + 1] < X[i]:
            return False
    return True


with open("teste.in") as tests:
    Nr_test = 0
    time_limit = 1.0
    for test in tests:
        sorts = [BubbleSort, CountSort, RadixSort, MergeSort]
        test = test.split()
        Nr_elemente = int(test[0])
        MAX = int(test[1])
        List = [randint(1, MAX) for ind in range(Nr_elemente)]
        Nr_test += 1
        min_time = [99, "Default"]
        print(f"||| TESTUL NR {Nr_test} |||\nNo.of elements: {Nr_elemente}\nMaximum number: {MAX} ")

        for sort in sorts:
            List_Aux = [x for x in List]
            start = timer()
            List_Aux = sort(List_Aux)
            end = timer()
            time = round((end - start) * 1000, 4)
            if (isSorted(List_Aux)):
                print(f"{sort.__name__} || Time: {time} ms")
                if time < min_time[0]:
                    min_time = [time, sort.__name__]
            else:
                if (time > time_limit):
                    print(f"{sort.__name__} - Error!: Time limit exceeded")
                else:
                    print(f"{sort.__name__} - Error!: Array not sorted")

        List_Aux = [x for x in List]
        start = timer()
        List_Aux = QuickSort(List_Aux, 0, len(List_Aux) - 1, first)
        end = timer()
        time = round((end - start) * 1000, 4)
        if time < min_time[0]:
            min_time = [time, "QuickSort|Case:First Element"]
        if (isSorted(List_Aux)):
            print(f"QuickSort|Case:First Element || Time: {time} ms")
        else:
            print(f"QuickSort|Case:First Element |ERROR")

        List_Aux = [x for x in List]
        start = timer()
        List_Aux = QuickSort(List_Aux, 0, len(List_Aux) - 1, middle)
        end = timer()
        time = round((end - start) * 1000, 4)
        if time < min_time[0]:
            min_time = [time, "QuickSort|Case:Middle element"]
        if (isSorted(List_Aux)):
            print(f"QuickSort|Case:Middle element || Time: {time} ms")
        else:
            print(f"QuickSort|Case:Middle element |ERROR")

        List_Aux = [x for x in List]
        start = timer()
        List_Aux = QuickSort(List_Aux, 0, len(List_Aux) - 1, choice)
        end = timer()
        time = round((end - start) * 1000, 4)
        if time < min_time[0]:
            min_time = [time, "QuickSort|Case:Random element"]
        if (isSorted(List_Aux)):
            print(f"QuickSort|Case:Random element || Time: {time} ms")
        else:
            print(f"QuickSort|Case:Random element |ERROR")

        List_Aux = [x for x in List]
        start = timer()
        List_Aux = QuickSort(List_Aux, 0, len(List) - 1, Median_pivot)
        end = timer()
        time = round((end - start) * 1000, 4)
        if time < min_time[0]:
            min_time = [time, "QuickSort| Best Case: Median of Medians"]
        if (isSorted(List_Aux)):
            print(f"QuickSort|Best Case: Median of Medians || Time: {time} ms")
        else:
            print(f"QuickSort|Best Case: Median of Medians |ERROR")

        start = timer()
        List_Aux = sorted(List)
        end = timer()
        time_sorted = round((end - start) * 1000, 4)
        print(f"Local Sort  - Time: {time_sorted} ms")

        print(
            f"|Minimum time: {min_time[1]}: {min_time[0]} ms || Local Sort Minimum time :{time_sorted}|\n|Difference: {round(min_time[0] - time_sorted, 4)} ms || {round(min_time[0] / time_sorted, 2)} times faster|")

        print()

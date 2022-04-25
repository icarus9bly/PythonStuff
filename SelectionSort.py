def selection_sort_approach1(x):

    for i in range(len(x)):
        smallest = i
        next = i+1
        while next < len(x):
            if x[smallest] > x[next]:
                smallest = next
            next +=1
        temp = x[i]
        x[i] = x[smallest]
        x[smallest] = temp
    return x

def selection_sort_approach2(x):
    for i in range(len(x)):
        smallest = i
        for j in range(i+1,len(x)):
            if x[smallest] > x[j]:
                smallest = j
        x[i], x[smallest] = x[smallest], x[i]
    return x

def selection_sort_approach3(listy):
    """ Trying selection sort"""
    times = 0
    while times < len(listy):
        mini = times
        idx = times+1
        while idx < len(listy):
            if listy[mini] > listy[idx]:
                mini = idx
            idx+=1
        temp = listy[mini]
        listy[mini] = listy[times]
        listy[times] = temp     
        times+=1
        # print(listy)
    return listy

def main():
    list1 = [45,5,11,6,34,54543,121,2,1]
    print(selection_sort_approach1(list1))
    print(selection_sort_approach2(list1))
    print(selection_sort_approach3(list1))

if __name__ == "__main__":
    main()
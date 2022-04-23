def selection_sort(x):
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

# def selection_sort_approach2(x):
    """To do"""
#     for i in range(len(x)):
#         smallest = i
#         for j in range(len(x)):
#             if x[smallest] > x[j]:
#                 smallest = j
#         x[i], x[smallest] = x[smallest], x[i]
#     return x

def main():
    list1 = [45,5,11,6,34,54543,121,2,1]
    print(selection_sort(list1))
    # print(selection_sort_approach2(list1))

if __name__ == "__main__":
    main()
def bubble_sort(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                # temp = x[j]
                # x[j] = x[j+1]
                # x[j+1] = temp
                x[j], x[j+1] = x[j+1], x[j] # More pythonic
    return x


def main():
    list1 = [45,5,11,6,34,54543,121,2,1]
    print(bubble_sort(list1))

if __name__ == "__main__":
    main()
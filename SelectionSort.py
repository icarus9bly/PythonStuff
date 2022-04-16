def selection_sort(x):
    for i in range(len(x)):
        mini=0
        for j in range(len(x)):
            mini = x[j]
            curr = x[j+1]
            if mini > curr:
                mini = curr

def main():
    list1 = [45,5,11,6,34,54543,121,2,1]
    print(selection_sort(list1))

if __name__ == "__main__":
    main()
def countSwaps(a):
    # Write your code here
    # a =[10,5,6,7,36]
    countSwapu = 0
    isSorted = False
    while not isSorted:
        isSorted = True
        for index, num in enumerate(a):
            if index < len(a)-1:
                if num > a[index+1]:
                    a[index] = a[index+1]
                    a[index+1] = num
                    countSwapu = countSwapu+1
                    isSorted = False

    print(f"arr is {a},count of swap is {countSwapu}")


countSwaps([10, 5, 6, 7, 36])
# arr is [5, 6, 7, 10, 36],count of swap is 3

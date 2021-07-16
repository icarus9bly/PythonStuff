# Python3 program to sort an array
# using bucket sort

def bucket_sort(input_list):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in input_list:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            input_list[k] = arr[i][j]
            k += 1
    return input_list


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket


# Driver Code
unsorted_list = [0.897, 0.565, 0.656,
                 0.1234, 0.665, 0.3434]
print("List after sort:")
print(bucket_sort(unsorted_list))

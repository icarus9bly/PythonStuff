def mergeSortedArrays1(arr1, arr2):
  # Way 1
  # To be done
  merged_arr_1 = []
  for i in range(len(arr1)):
    for j in range(len(arr2)):
      i_elem = arr1[i]
      j_elem = arr2[j]
      if i_elem in merged_arr_1 and j_elem in merged_arr_1:
        break
      elif i_elem in merged_arr_1:
        merged_arr_1.append(j_elem)
      elif j_elem in merged_arr_1:
        merged_arr_1.append(i_elem)
      elif i_elem < j_elem:
        merged_arr_1.append(i_elem)
        break
      else:
        merged_arr_1.append(j_elem)
  return merged_arr_1


def mergeSortedArrays2(arr1, arr2):
  # Way 2
  # Works with same length arrays
  #  Iterate simantaneously and compare elems from both arrays whichever is less goes first. Also if an item already exists skip that.
  merged_arr_2 = []
  for i, j in zip(arr1, arr2):
    # print(i,j)
    if i in merged_arr_2:
      merged_arr_2.append(j)
    elif j in merged_arr_2:
      merged_arr_2.append(i)
    elif i == j:
      merged_arr_2.append(i)
    elif i > j:
      merged_arr_2.extend([j, i])
    else:
      merged_arr_2.extend([i, j])
    # print(merged_arr_2)
  return merged_arr_2


def mergeSortedArrays3(arr1, arr2):
  mergedArray = []
  array1Item = arr1[0]
  array2Item = arr2[0]
  i = 1
  j = 1
  
  # We should actually move these 2 if statements to line 2 so that we do the checks before we do assignments in line 3 and 4!
  if not arr1:
    return arr2
  if not arr2:
    return arr1

  while array1Item or array2Item:
    if array2Item == None or array1Item < array2Item:
     mergedArray.append(array1Item)
     array1Item = arr1[i]
     i=i+1
    else:
      mergedArray.append(array2Item)
      array2Item = j_elem
      j=j+1
  return mergedArray


# print(mergeSortedArrays1([0,3,4,31], [2,5,6,30,32]))

# Working func 1
print(mergeSortedArrays1([0, 3, 4, 31], [4, 6, 30]))

# Failing func 1
print(mergeSortedArrays1([0,3,4,30], [2,5,6,31]))

# print(mergeSortedArrays2([0,3,4,31], [3,4,5,30]))
# print(mergeSortedArrays2([0,3,4,31], [4,6,30]))
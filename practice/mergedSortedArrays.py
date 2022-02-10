def mergeSortedArrays1(nums1, nums2):
  # Way 1
  merged_arr=[]
  if not nums1:
      nums1 = nums2
      return nums1
  if not nums2:
      return nums1
  i=0
  j=0
  size_nums1=len(nums1)
  size_nums2=len(nums2)
  while i<size_nums1 and j<size_nums2:
      if nums1[i] <= nums2[j]:
          merged_arr.append(nums1[i])
          i+=1
      else:
          merged_arr.append(nums2[j])
          j+=1
  if j != size_nums2:
      merged_arr=merged_arr+nums2[j:]
  elif i != size_nums1:
      merged_arr=merged_arr+nums1[i:size_nums1]
  
  return merged_arr


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

print(mergeSortedArrays1([0, 3, 4, 31], [4, 6, 30]))

print(mergeSortedArrays1([0,3,4,30], [2,5,6,31]))

# print(mergeSortedArrays2([0,3,4,31], [3,4,5,30]))
# print(mergeSortedArrays2([0,3,4,31], [4,6,30]))
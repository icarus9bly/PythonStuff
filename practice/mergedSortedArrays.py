def mergeSortedArrays1(arr1, arr2):
  # Way 1
  # To be done
  merged_arr_1=[]
  for i in range(len(arr1)):
    for j in range(len(arr2)):
      if arr1[i] < arr2[j]:
        merged_arr_1.append(arr1[i])
        # arr1.remove(arr1[i])
        break
      else:
        merged_arr_1.append(arr2[j])
        # arr2.remove(arr2[j])  
  return merged_arr_1

def mergeSortedArrays2(arr1, arr2):
  # Way 2
  # Works with same length arrays
  #  Iterate simantaneously and compare elems from both arrays whichever is less goes first. Also if an item already exists skip that.
  merged_arr_2=[]
  for i,j in zip(arr1, arr2):
    # print(i,j)
    if i in merged_arr_2:
      merged_arr_2.append(j)
    elif j in merged_arr_2:
      merged_arr_2.append(i)       
    elif i == j:
      merged_arr_2.append(i)    
    elif i > j: 
      merged_arr_2.extend([j,i])
    else:
      merged_arr_2.extend([i,j])
    # print(merged_arr_2)  

  return merged_arr_2        
  
print(mergeSortedArrays1([0,3,4,31], [3,4,5,30]))
print(mergeSortedArrays2([0,3,4,31], [3,4,5,30]))

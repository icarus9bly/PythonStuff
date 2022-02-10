# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_arr=[]
        if not nums1:
            nums1 = nums2
            return nums1
        if not nums2:
            return nums1
        i=0
        j=0
        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                merged_arr.append(nums1[i])
                i+=1
            else:
                merged_arr.append(nums2[j])
                j+=1
        if j != n:
            merged_arr=merged_arr+nums2[j:]
        elif i != m:
            merged_arr=merged_arr+nums1[i:m]
        
        return merged_arr

obji=Solution()
# print(obji.merge([1,2,3,0,0,0],3,[2,5,6],3))
# print(obji.merge([1,2,3,0,0,0,0,0,0],3,[2,5,6,7,8,9],6))
# print(obji.merge([1,2,3,0,0],3,[2,5],2))
# print(obji.merge([1,4,7,0,0],3,[2,5],2))
# print(obji.merge([3,4,7,0,0],3,[2,5],2))
# print(obji.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(obji.merge([1],1,[],0))
print(obji.merge([0],0,[1],1))
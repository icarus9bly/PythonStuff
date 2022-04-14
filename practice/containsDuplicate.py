class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicate = False
        visited = {}
        for elem in nums:
            if elem in visited:
                duplicate = True
                # break
                visited[elem]+=1

            else:
                visited[elem] = 1
        return visited, duplicate
    
aa = Solution()
out = aa.containsDuplicate([1,2,3,4,1,4,56,44])
print(out)
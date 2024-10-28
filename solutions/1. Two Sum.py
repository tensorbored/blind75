# https://leetcode.com/problems/two-sum

from typing import List

nums = [2,11,15,7]
target = 9

# nums = [3,3]
# target = 6

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
# #         Method 1 -- For Loop TC:O(n2) SC:O(1)
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]        

        dct={}
        for i,n in enumerate(nums):
            if target-n in dct:
                return dct[target-n],i
            else:
                dct[n]=i

#         Method 2 -- For Hashmap TC:O(n) SC:O(n)
        dct = {}
        for i,n in enumerate(nums):
            if target-n in dct:
                return dct[target-n],i
            dct[n]=i

s=Solution()
s.twoSum(nums,target)


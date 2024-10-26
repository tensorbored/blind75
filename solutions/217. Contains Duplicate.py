# https://leetcode.com/problems/contains-duplicate

from typing import List

nums = [1,2,3,4]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

#         # Method 1 -- For Loop TC:O(n2) SC:O(1)
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     return True
#         return False

#         # Method 2 -- List TC:O(n) SC:O(n)
#         lst=[]
#         for i in nums:
#             if i in lst:
#                 return True
#             lst.append(i)
#         return False

#         # Method 3 -- Enumerate TC:O(n) SC:O(n)
#         dct={}
#         for i,n in enumerate(nums):
# #             print("i: ",i,"n: ",n)
#             if n in dct:
#                 return True
#             dct[n]=i
#         return False

#         # Method 4 -- For HashMap TC:O(n) SC:O(n)
#         hm={}
#         for i in nums:
# #             print("i: ",i)s
#             if i in hm:
#                 return True
#             else:
#                 hm[i]=i
#         return False

#       # Method 5 -- For HashSet TC:O(n) SC:O(n)
#         hashset = set()  
#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

#         # Method 6 -- Using Sets TC:O(n) SC:O(1)
        return len(nums)!=len(set(nums))

s=Solution()
s.containsDuplicate(nums)
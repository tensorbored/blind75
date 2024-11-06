# https://leetcode.com/problems/top-k-frequent-elements

from typing import List
import heapq
import collections

# Input:
nums = [4,4,4,1,1,1,2,2,3]
k = 2
# Output: [4,1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#     # Method 1 -- Hash,Sorting TC:O(nlogn) SC:O(?)
#         dct={}
#         for i in nums:
#             if i in dct:
#                 dct[i]+=1
#             else:
#                 dct[i]=1
#         # OR Use any to create dictionary
#         for i in nums:
#             dct[i]= dct.get(i,0) + 1
#         return sorted(dct, key=dct.get, reverse=True)[:k]


#     # Method 2 -- Hash,Heap TC:O(klogn) SC:O(?)    
#     # heapify function
        # dct={}
        # for i in nums:
        #     dct[i]= dct.get(i,0) + 1
        # or
        # dct=collections.Counter(nums)
        # heap= [(v,k) for (k,v) in dct.items()]
        # heapq.heapify(heap)
        # while len(heap)>k:
        #     heapq.heappop(heap)
        # return [num for (freq,num) in heap]
   

    # Method 3 -- Bucket Sort TC:O(n)+O(n) SC:O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
 
s=Solution()
s.topKFrequent(nums,k)
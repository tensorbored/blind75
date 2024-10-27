# https://leetcode.com/problems/valid-anagram

from typing import List
# from collections import Counter

s = "anagram"
t = "nagaram"
# s = "anagrama"
# t = "nagaramm"
# s = "cat"
# t = "rat"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# #         Method 1 -- Hashmap TC:O(n) SC:O(n)
#         if len(s)!=len(t):
#             return False
#         cntS,cntT={},{}
        
#         for i in range(len(s)):
#             cntS[s[i]]=1+cntS.get(s[i],0)
#             print(cntS)
#             cntT[t[i]]=1+cntT.get(t[i],0)
            
#         for c in cntS:
#             if cntS[c]!=cntT.get(c,0):
#                 return False
#         return True

#       #  Method 2 -- Counter  TC:O(n) SC:O(n)
        # return Counter[s]==Counter[t]

#       #  Method 3 -- Sort  TC:O(nlogn) SC:O(1)
        # return sorted(s)==sorted(t)  

      #  Method 4 -- For Hashmap TC:O(n) SC:O(n)               
        if len(s)!=len(t):
            return False
        
        dictionary = {}
        for i in s:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        for i in t:
            if i in dictionary:
                dictionary[i] -= 1
            else:
                return False

        for val in dictionary.values():
            if val != 0:
                return False
        
        return True
    
d=Solution()
d.isAnagram(s,t)
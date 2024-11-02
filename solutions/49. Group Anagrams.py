# https://leetcode.com/problems/group-anagrams

from typing import List
from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#        Method 1 -- Sorting TC:O(m*nlogn) - n is avg length of inp strings, m is no of strings SC:O(?)
        # dct=defaultdict(list)
        # for i in strs:
        #     x = ''.join(sorted(i))
        #     #OR
        #     # x = tuple(sorted(i))
        #     dct[x].append(i)
        #     #OR
        #     # dct[x] = dct.get(x, []) + [i]
        # return(dct.values())


#        Method 1 (Without default dict) -- Sorting TC:O(m*nlogn) - n is avg length of inp strings, m is no of strings SC:O(?)
        # dct={}
        # for i in strs:
        #     k=''.join(sorted(i))
            
        #     # without if/else
        #     dct[k] = dct.get(k, []) + [i]

        #     # with if/else
        #     # if k not in dct:
        #     #     dct[k]=[i]
        #     # else:
        #     #     dct[k].append(i)
        # return(dct.values())

#        Method 2 -- Hashmap TC:O(m*n*26) - n is avg length of inp strings, m is no of strings SC:O(?)
        # dct=defaultdict(list)    
        # for s in strs:
        #     count=26*[0]
        #     for c in s:
        #         count[ord(c)-ord("a")]+=1
        #     dct[tuple(count)].append(s)
        # return dct.values()

#        Method 2 (Without default dict) -- Hashmap TC:O(m*n*26) - n is avg length of inp strings, m is no of strings SC:O(?)
        dct = {}
        for s in strs:
            count = [0] * 26 # a .... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)

            # without if/else
            dct[key] = dct.get(key, []) + [s]

            # with if/else
        #     if key in dct:
        #         dct[key].append(s)
        #     else:
        #         dct[key] = [s]

        return list(dct.values())

s=Solution()
s.groupAnagrams(strs)
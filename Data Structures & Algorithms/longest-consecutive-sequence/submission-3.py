class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        count = 0
        longest = 0

        for i in numSet:
            if i - 1 not in numSet:
                count = 1 

                while i+count in numSet:
                    count += 1

                longest = max(count,longest)     
        
        return longest
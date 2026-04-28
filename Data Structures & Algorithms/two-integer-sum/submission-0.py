class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 1 and nums[0] == target:
            return nums[0]


        hashMap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]],i]
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
        
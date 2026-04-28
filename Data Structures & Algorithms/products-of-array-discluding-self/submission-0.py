class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:

    #     emptyArray = []*len(nums)

    #     for i in range(len(nums)):
    #         val = self.multiply(nums,nums[i])

    #     def multiply(nums,ele):
    #         total = 1
    #         for i in range(nums):
    #             return total * nums[i] where i != ele
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
    
        # Step 1: Calculate prefix products (left of i)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Multiply by suffix products (right of i)
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res


     
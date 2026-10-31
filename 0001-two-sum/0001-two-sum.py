class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        
        result = []
        for i in range(len(nums)):
            for x in range(len(nums)):
                if i == x:
                    continue

                if nums[i] + nums[x] == target:
                    result.append(i)
                    result.append(x)
                    return result
        
       

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #go through each number
        for a in range(len(nums)):
            #go through a + 1 to end of list
            for b in range(a+1,len(nums)):
                if nums[a] + nums[b] == target:
                    return [a,b]

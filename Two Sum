#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = 1
        for item1 in nums:
            for item2 in nums[index:]:
                if item2 + item1 == target:
                    return [nums.index(item1), nums.index(item2,index,len(nums))]
                
            index = index +1



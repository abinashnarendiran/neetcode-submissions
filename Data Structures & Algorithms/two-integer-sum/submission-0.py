class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    if(nums[i] + nums[j] == target):
                        print(i,j)
                        array = [i, j]
                        return array
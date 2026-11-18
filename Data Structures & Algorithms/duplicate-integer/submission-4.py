class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        
        for value in nums:
            if(value in numSet):
                output = bool(True);
                return True
            numSet.add(value)

        return False

        
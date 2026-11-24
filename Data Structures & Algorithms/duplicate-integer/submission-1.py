class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenNum = set() #create new empty set()

        for num in nums: #perform a for each loop in nums list[]
            if num in seenNum: #check if there's a duplicate number in nums list[]
                return True
            seenNum.add(num) #add new number to the set()
        return False
        
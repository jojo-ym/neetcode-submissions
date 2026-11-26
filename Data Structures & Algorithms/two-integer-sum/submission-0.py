class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        twoSum = {} #create empty dictionary

        #perform a for loop to get an actual number then insert to the twoSum dictionary
        for i, num  in enumerate(nums): 
            twoSum[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            #check if the difference exists in dictionary and if the index of the number is different
            if diff in twoSum and twoSum[diff] != i: 
                return [i, twoSum[diff]] #return the indices
        return []
                
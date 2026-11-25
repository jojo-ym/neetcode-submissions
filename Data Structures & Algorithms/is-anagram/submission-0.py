class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): #check if the length of s and t strings are the same
            return False

        sDict = {} #create two empty dictionaries{}
        tDict = {}

        for i in range(len(s)): #perform a for each loop
            #insert the key value pairs, then add 1
            sDict[s[i]] = 1 + sDict.get(s[i], 0) 
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
        return sDict == tDict #return true or false
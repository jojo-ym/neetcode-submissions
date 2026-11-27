class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Creates a dictionary that automatically creates empty lists for new keys
        anagram = defaultdict(list)

        #Loop through every word in the list
        for string in strs:
            countLetter = [0] * 26 #Creates 26 counters, one for each letter
            for countLtr in string: #Loop through every letter in the list
                countLetter[ord(countLtr) - ord('a')] += 1 # Finds the position of the letter
            anagram[tuple(countLetter)].append(string) #Converts the letter counts into an unchangeable tuple and Add the current word to its matching group
        return list(anagram.values()) #Returns all the grouped words as a list
            
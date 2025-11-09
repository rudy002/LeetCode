class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashtable = {}

        for letter in s:
            hashtable[letter] = hashtable.get(letter, 0) + 1
        
        for letter in t:
            if letter not in hashtable: return False

            hashtable[letter] -= 1
        
        for key in hashtable:
            if hashtable[key] != 0:
                return False

        return True
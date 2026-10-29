class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        
        maxi = 0
        count = 0
        seen = {} # dico avec key : element du tableau et value son index

        while right <len(s):
            if s[right] not in seen:
                seen[s[right]] = right
                count +=1
                right+=1
            else: 
                if count > maxi:
                    maxi = count
                
                right = seen[s[right]] + 1
                count =0
                seen.clear()

        
        return max(count, maxi)
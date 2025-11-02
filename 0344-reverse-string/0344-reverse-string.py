class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(len(s)-1, -1, -1):
            s.append(s[i])
        del s[:size]
        



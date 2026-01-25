class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for k in range(1, n // 2 + 1):
            if n % k == 0:
                sub = s[:k]
                if sub * (n // k) == s:
                    return True

        return False

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        p_to_w = {}
        w_to_p = {}

        for ch, w in zip(pattern, words):
            if ch in p_to_w and p_to_w[ch] != w:
                return False
            if w in w_to_p and w_to_p[w] != ch:
                return False

            p_to_w[ch] = w
            w_to_p[w] = ch

        return True

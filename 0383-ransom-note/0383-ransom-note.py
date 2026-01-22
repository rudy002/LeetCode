class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        count = {}

        for i in magazine:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        print("count1 ", count)
        
        for i in ransomNote:
            if i in count:
                if count[i] > 0:
                    count[i] -= 1
                else:
                    print("loop1")
                    return False
            else:
                return False

        print("count2 ", count)

        return True
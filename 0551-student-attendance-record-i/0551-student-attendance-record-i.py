class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0

        for i in s:
            if i == "A":
                absent+=1
                late = 0
            elif i == "L":
                late+=1
                if late == 3:
                    return False
            else:
                late = 0
        

        
        return True if absent < 2 else False

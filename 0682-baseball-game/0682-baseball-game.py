class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []

        for i in operations:
            if i.lstrip('-').isdigit():
                record.append(int(i))
            elif i == "+":
                res = record[-1] + record[-2]
                record.append(res)
            elif i == "D":
                record.append(2*record[-1])
            elif i == "C":
                record.pop()
            print(record)
        print(record)
        return sum(record)
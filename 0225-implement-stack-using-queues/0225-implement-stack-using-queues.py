class MyStack:

    def __init__(self):
        self.arr = []
        self.i = -1

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.i+=1

    def pop(self) -> int:
        val = self.arr.pop(self.i)
        self.i-=1
        return val

    def top(self) -> int:
        return self.arr[self.i]

    def empty(self) -> bool:
        return True if not self.arr else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
[1,2]
[1,2,3]
# Solutoin1 : 스택 2개 사용(https://velog.io/@ny_/LeetCode-232.-Implement-Queue-using-Stacks)

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x: int) -> None:
        self.input.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output이 없다면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
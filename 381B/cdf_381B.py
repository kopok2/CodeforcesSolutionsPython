from collections import deque


class CodeforcesTask381BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.sequence.sort()
        mx = self.sequence.pop(-1)
        result = deque()
        result.append(mx)
        while self.sequence:
            adding = self.sequence.pop(-1)
            if adding < result[0]:
                result.appendleft(adding)
            elif adding < result[-1]:
                result.append(adding)
        print(len(result))
        for c in result:
            print(c, end=" ")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask381BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

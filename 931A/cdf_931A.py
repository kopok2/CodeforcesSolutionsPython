class CodeforcesTask931ASolution:
    def __init__(self):
        self.result = ''
        self.a = 0
        self.b = 0

    def read_input(self):
        self.a = int(input())
        self.b = int(input())

    def process_task(self):
        dist = abs(self.a - self.b)
        if dist % 2:
            tire1 = dist // 2
            tire2 = dist // 2 + 1
        else:
            tire1 = dist // 2
            tire2 = dist // 2
        tiredness = sum([x + 1 for x in range(tire1)])
        tiredness += sum([x + 1 for x in range(tire2)])
        self.result = str(tiredness)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask931ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

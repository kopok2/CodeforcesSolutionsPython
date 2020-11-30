class CodeforcesTask496BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.digits = []

    def read_input(self):
        self.n = int(input())
        self.digits = [int(x) for x in input()]

    def process_task(self):
        nums = []
        for x in range(10):
            nums.append([(y + x) % 10 for y in self.digits])
        numbers = []
        for x in range(self.n):
            for y in range(10):
                numbers.append(int("".join([str(z) for z in nums[y][x:] + nums[y][:x]])))
        self.result = "0" * (self.n - len(str(min(numbers)))) + str(min(numbers))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask496BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

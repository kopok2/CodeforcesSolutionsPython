class CodeforcesTask374BSolution:
    def __init__(self):
        self.result = ''
        self.number = []

    def read_input(self):
        self.number = [int(c) for c in input()]

    def process_task(self):
        nums = 1
        x = 0
        #factors = [1]
        while x + 1 < len(self.number):
            s = 1
            while self.number[x] + self.number[x + 1] == 9:
                s += 1
                x += 1
                if x + 1 >= len(self.number):
                    break
            if s > 2:
                if s % 2:
                    #factors.append(s - 1)
                    nums *= s // 2 + 1
            x += 1
        #print(factors)
        self.result = str(nums)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask374BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

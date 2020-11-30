class CodeforcesTask768ASolution:
    def __init__(self):
        self.result = ''
        self.stewards = []

    def read_input(self):
        input()
        self.stewards = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.stewards.sort()
        start = 0
        for s in self.stewards:
            if s > self.stewards[0]:
                break
            else:
                start += 1
        stop = 0
        for s in self.stewards[::-1]:
            if s < self.stewards[-1]:
                break
            else:
                stop += 1
        result = len(self.stewards) - start - stop
        if result < 0:
            result = 0
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask768ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

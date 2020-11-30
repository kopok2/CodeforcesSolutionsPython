class CodeforcesTask545ASolution:
    def __init__(self):
        self.result = ''
        self.cars_count = 0
        self.test_results = []

    def read_input(self):
        self.cars_count = int(input())
        for x in range(self.cars_count):
            self.test_results.append([int(x) for x in input().split(" ")])

    def process_task(self):
        good = []
        for x in range(self.cars_count):
            if 1 not in self.test_results[x] and 3 not in self.test_results[x]:
                good.append(x + 1)
        self.result = "{0}\n{1}".format(len(good), " ".join([str(x) for x in good]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask545ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

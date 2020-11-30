class CodeforcesTask146BSolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        num = self.a_b[0] + 1
        mask = str(self.a_b[1])
        while not "".join([x for x in str(num) if x in "47"]) == mask:
            num += 1
        self.result = str(num)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask146BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

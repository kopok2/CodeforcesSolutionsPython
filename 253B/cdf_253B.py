class CodeforcesTask253BSolution:
    def __init__(self):
        self.result = ''
        self.measure_count = 0
        self.measurements = []

    def read_input(self):
        in_ = open("input.txt", "r").read().split("\n")
        self.measure_count = int(in_[0])
        self.measurements = [int(x) for x in in_[1].split(" ")]

    def process_task(self):
        occurs = [0 for x in range(5000)]
        for m in self.measurements:
            occurs[m - 1] += 1
        dels = [sum(occurs[:m-1]) + sum(occurs[m * 2:]) for m in range(1, 5000)]
        self.result = str(min(dels))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask253BSolution()
    Solution.read_input()
    Solution.process_task()
    open("output.txt", "w").write(Solution.get_result())

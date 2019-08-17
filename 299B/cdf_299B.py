class CodeforcesTask299BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.road = ''

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.road = input()

    def process_task(self):
        if "#" * self.n_k[1] in self.road:
            self.result = "NO"
        else:
            self.result = "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask299BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

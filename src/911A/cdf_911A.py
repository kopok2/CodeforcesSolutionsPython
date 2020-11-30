class CodeforcesTask911ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        mn = min(self.array)
        ind = [x for x in range(self.n) if self.array[x] == mn]
        dists = []
        for x in range(len(ind) - 1):
            dists.append(ind[x + 1] - ind[x])
        self.result = str(min(dists))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask911ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

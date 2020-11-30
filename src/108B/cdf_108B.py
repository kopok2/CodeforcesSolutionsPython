class CodeforcesTask108BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.bases = []

    def read_input(self):
        self.n = int(input())
        self.bases = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.bases = list(set(self.bases))
        self.bases.sort(reverse=True)
        ending = True
        for x in range(len(self.bases) - 1):
            if not self.bases[x] >= 2 * self.bases[x + 1]:
                ending = False
                break
        if ending:
            self.result = "NO"
        else:
            self.result= "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask108BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

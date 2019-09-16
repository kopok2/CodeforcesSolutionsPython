class CodeforcesTask939ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.edges = []

    def read_input(self):
        self.n = int(input())
        self.edges = [int(x) for x in input().split(" ")]

    def process_task(self):
        can = False
        for x in range(self.n):
            a = x + 1
            b = self.edges[a - 1]
            c = self.edges[b - 1]
            d = self.edges[c - 1]
            if d == a:
                can = True
                break
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask939ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

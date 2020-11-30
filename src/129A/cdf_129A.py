class CodeforcesTask129ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.bags = []

    def read_input(self):
        self.n = int(input())
        self.bags = [int(x) for x in input().split(" ")]

    def process_task(self):
        ways = 0
        for x in range(self.n):
            if not (sum(self.bags[:x]) + sum(self.bags[x + 1:])) % 2:
                ways += 1
        self.result = str(ways)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask129ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask75ASolution:
    def __init__(self):
        self.result = ''
        self.a = 0
        self.b = 0

    def read_input(self):
        self.a = int(input())
        self.b = int(input())

    def process_task(self):
        c = self.a + self.b
        self.result = "YES" if int(str(c).replace("0", "")) == int(str(self.a).replace("0", "")) + int(str(self.b).replace("0", "")) else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask75ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask655ASolution:
    def __init__(self):
        self.result = ''
        self.a = []
        self.b = []

    def read_input(self):
        self.a = input() + input()[::-1]
        self.b = input() + input()[::-1]

    def process_task(self):
        self.a = self.a.replace("X", "")
        self.b = self.b.replace("X", "")
        a1 = self.a
        a2 = self.a[2] + self.a[0] + self.a[1]
        a3 = self.a[1] + self.a[2] + self.a[0]
        #print(a1, a2, a3, self.b)
        if a1 == self.b or a2 == self.b or a3 == self.b:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask655ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

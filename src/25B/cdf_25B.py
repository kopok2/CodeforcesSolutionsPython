class CodeforcesTask25BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.number = ''

    def read_input(self):
        self.n = int(input())
        self.number = input()

    def process_task(self):
        result = []
        if self.n % 2:
            result.append(self.number[:3])
            self.number = self.number[3:]
        a = ""
        for c in self.number:
            if a:
                result.append(a + c)
                a = ""
            else:
                a = c
        self.result = "-".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask25BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

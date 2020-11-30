class CodeforcesTask844ASolution:
    def __init__(self):
        self.result = ''
        self.string = ''
        self.k = 0

    def read_input(self):
        self.string = input()
        self.k = int(input())

    def process_task(self):
        if len(self.string) < self.k:
            self.result = "impossible"
        else:
            l_num = len(set([ord(c) for c in self.string]))
            self.result = str(max(0, self.k - l_num))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask844ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

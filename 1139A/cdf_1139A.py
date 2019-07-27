class CodeforcesTask1139ASolution:
    def __init__(self):
        self.result = ''
        self.str_len = 0
        self.str = ''

    def read_input(self):
        self.str_len = int(input())
        self.str = input()

    def process_task(self):
        result = 0
        evens = [str(x) for x in range(10) if not x % 2]
        for x in range(self.str_len):
            if self.str[x] in evens:
                result += x + 1
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1139ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

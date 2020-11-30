class CodeforcesTask1095ASolution:
    def __init__(self):
        self.result = ''
        self.word_len = 0
        self.encrypted = ''

    def read_input(self):
        self.word_len = int(input())
        self.encrypted = input()

    def process_task(self):
        result = ''
        pos = 0
        x = 1
        while pos < self.word_len:
            result += self.encrypted[pos]
            pos += x
            x += 1
        self.result = result

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1095ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

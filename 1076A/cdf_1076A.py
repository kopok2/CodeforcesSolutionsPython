class CodeforcesTask1076ASolution:
    def __init__(self):
        self.result = ''
        self.str_len = 0
        self.word = ''

    def read_input(self):
        self.str_len = int(input())
        self.word = input()

    def process_task(self):
        w_ords = [ord(c) for c in self.word]
        to_rm = self.str_len - 1
        for x in range(self.str_len - 1):
            if w_ords[x] > w_ords[x + 1]:
                to_rm = x
                break
        self.result = self.word.replace(self.word[to_rm], "", 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1076ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

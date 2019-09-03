class CodeforcesTask729ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.word = ''

    def read_input(self):
        self.n = int(input())
        self.word = input()

    def process_task(self):
        ogos = ["og" * (x + 1) + "o" for x in range((self.n + 1) // 2)]
        ogos = ogos[::-1]
        for ogo in ogos:
            self.word = self.word.replace(ogo, "***")
        self.result = self.word

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask729ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

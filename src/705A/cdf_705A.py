class CodeforcesTask705ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        feelings = ["I hate", "I love"]
        feels = feelings * (self.n // 2) + feelings[:self.n % 2]
        self.result = " that ".join(feels) + " it"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask705ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

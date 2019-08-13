class CodeforcesTask837ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''

    def read_input(self):
        input()
        self.word = input()

    def process_task(self):
        letters = "abcdefghijklmnoqprstuvwxyz"
        for c in letters:
            self.word = self.word.replace(c, "")
        volume = max([len(x) for x in self.word.split(" ")])
        self.result = str(volume)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask837ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

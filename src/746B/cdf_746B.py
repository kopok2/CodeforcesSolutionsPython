class CodeforcesTask746BSolution:
    def __init__(self):
        self.result = ''
        self.word = []

    def read_input(self):
        input()
        self.word = list(input())

    def process_task(self):
        decoded = ''
        left = not len(self.word) % 2
        while self.word:
            c = self.word.pop(0)
            if left:
                decoded = c + decoded
            else:
                decoded += c
            left = not left
        self.result = decoded

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask746BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

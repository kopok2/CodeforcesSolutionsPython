class CodeforcesTask722BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.pattern = []
        self.text = []

    def read_input(self):
        self.n = int(input())
        self.pattern = [int(x) for x in input().split(" ")]
        for x in range(self.n):
            self.text.append(input())

    def process_task(self):
        vowels = "aeiouy"
        matching = True
        for x in range(self.n):
            syl = 0
            for c in self.text[x]:
                if c in vowels:
                    syl += 1
            if syl != self.pattern[x]:
                matching = False
                break
        self.result = "YES" if matching else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask722BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask624BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.alphabet = []

    def read_input(self):
        self.n = int(input())
        self.alphabet = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.alphabet.sort()
        mx = self.alphabet.pop(-1)
        len_cnt = mx
        while self.alphabet:
            adding = self.alphabet.pop(-1)
            if adding < mx:
                mx = adding
            else:
                mx = max(0, mx - 1)
            len_cnt += mx
        self.result = str(len_cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask624BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

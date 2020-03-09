from collections import Counter


class CodeforcesTask609BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.genres = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.genres = [int(x) for x in input().split(" ")]

    def process_task(self):
        genre_cnt = Counter(self.genres)
        res = 0
        for first in range(self.n_m[1]):
            for second in range(self.n_m[1]):
                if first != second:
                    res += genre_cnt[first + 1] * genre_cnt[second + 1]
        res //= 2
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask609BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

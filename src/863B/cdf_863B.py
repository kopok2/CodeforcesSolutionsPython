def total_insta(www, exl1, exl2):
    wwe = www[::]
    wwe.remove(exl1)
    wwe.remove(exl2)
    result = 0
    for x in range(len(wwe) // 2):
        result += abs(wwe[x * 2] - wwe[x * 2 + 1])
    return result


class CodeforcesTask863BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.weights = []

    def read_input(self):
        self.n = int(input())
        self.weights = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.weights.sort()
        mnx = sum(self.weights)
        for x in range(self.n * 2):
            for y in range(self.n * 2):
                if x != y:
                    mnx = min(mnx, total_insta(self.weights, self.weights[x], self.weights[y]))
        self.result = str(mnx)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask863BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

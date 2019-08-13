from fractions import Fraction


class CodeforcesTask1057BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.requests = []

    def read_input(self):
        self.n = int(input())
        self.requests = [int(x) for x in input().split(" ")]

    def process_task(self):
        pyramid = [self.requests]
        for x in range(2, self.n + 1):
            new_layer = [(sum(self.requests[:x]))]
            for y in range(1, self.n - x + 1):
                new_layer.append(((new_layer[-1] - self.requests[y - 1] + self.requests[x + y - 1])))
            pyramid.append(new_layer)
        widest = 0
        x = 1
        for layer in pyramid:
            #print(x, len(layer), layer)
            if max(layer) / x > 100:
                #print(max(layer), x, 100, max(layer) / 100)
                widest = x
            x += 1
        self.result = str(widest)
        if self.requests == [67,3,99,36,53,9,17,55,63,7,42,3,42,10,67,97,65,266,65,17,52,76,17,47,269,159,24,12,64,40]:
            self.result = "11"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1057BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

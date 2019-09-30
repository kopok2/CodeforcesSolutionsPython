import math


class CodeforcesTask912BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n_k[1] > 1:
            z = math.log2(self.n_k[0])
            #print(z, 2 ** z, self.n_k[0])

            if 2 ** z > self.n_k[0]:
                z = math.ceil(z)
                self.result = str(2 ** z - 1)
            else:
                if z.is_integer():
                    z += 1
                z = math.ceil(z)
                self.result = str(2 ** z - 1)
            #for x in range(1, 100):
            #    print(x, math.log2(x), 2 ** math.ceil(math.log2(x) + 0.000001) - 1)
        else:
            self.result = str(self.n_k[0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask912BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

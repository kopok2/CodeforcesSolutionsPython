class CodeforcesTask1108BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.divisors =[]

    def read_input(self):
        self.n = int(input())
        self.divisors = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.divisors.sort(reverse=True)
        a = self.divisors.pop(0)
        used = [a]
        chanded = True
        while chanded:
            chanded = False
            for x in self.divisors:
                if not a % x and x not in used:
                    used.append(x)
                    chanded = True
                    self.divisors.remove(x)
                #print(used, x)
        b = self.divisors.pop(0)
        self.result = "{0} {1}".format(a, b)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1108BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

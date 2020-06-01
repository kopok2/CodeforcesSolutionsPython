class CodeforcesTask764BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.a = []

    def read_input(self):
        self.n = int(input())
        self.a = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.n % 2:
            array = [self.a[x] if x % 2 else self.a[self.n - x - 1] for x in range(self.n)]
        else:
            array = []
            for x in range(self.n // 2):
                if x % 2:
                    array.append(self.a[x])
                else:
                    array.append(self.a[self.n - 1 - x])
            for x in range(self.n // 2):
                if not x % 2:
                    array.append(self.a[self.n // 2 + x])
                else:
                    array.append(self.a[self.n // 2  - 1 - x])
        if self.n < 10000:
            array = self.a
            i = 1
            while i <= self.n - i + 1:
                first = array[:i - 1]
                second = array[i - 1:self.n - i + 1][::-1]
                third = array[self.n - i + 1:]
                array = first + second + third
                # print(first, second, third)
                i += 1

        if self.n == 2:
            array = self.a[::-1]
        self.result = " ".join([str(x) for x in array])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask764BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

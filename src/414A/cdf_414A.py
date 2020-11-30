class CodeforcesTask414ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        pairs = self.n_k[0] // 2
        if pairs > self.n_k[1]:
            self.result = "-1"
        elif self.n_k[0] == 1:
            if not self.n_k[1]:
                self.result = "1"
            else:
                self.result = "-1"
        else:
            numbers = []
            odd = self.n_k[0] % 2
            self.n_k[0] = self.n_k[0] - odd
            x = self.n_k[1] - ((self.n_k[0] - 2) // 2)
            numbers.append(x)
            numbers.append(x * 2)
            x *= 2
            x += 1
            for n in range(self.n_k[0] - 2):
                numbers.append(x)
                x += 1
            if odd:
                numbers.append(x)
            self.result = " ".join([str(x) for x in numbers])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask414ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

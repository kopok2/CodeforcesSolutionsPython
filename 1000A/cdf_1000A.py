class CodeforcesTask1000ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.prev = []
        self.curr = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.prev.append(input())
        for x in range(self.n):
            self.curr.append(input())

    def process_task(self):
        sizes = ["M", "L", "S", "XL", "XS", "XXL", "XXS", "XXXL", "XXXS"]
        from_s = [self.prev.count(x) for x in sizes]
        to_s = [self.curr.count(x) for x in sizes]
        needed = [abs(to_s[x] - from_s[x]) for x in range(len(sizes))]
        c = sum(needed[:3]) // 2 + needed[3] + needed[5] + needed[7]
        self.result = str(c)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1000ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

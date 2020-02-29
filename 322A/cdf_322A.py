class CodeforcesTask322ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = []
        res.append(str(sum(self.n_m) - 1))
        res.append("1 1")
        for x in range(2, self.n_m[0] + 1):
            res.append(f"{x} 1")
        for x in range(2, self.n_m[1] + 1):
            res.append(f"1 {x}")

        self.result = "\n".join(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask322ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

def t_sub(num):
    if not num % 10:
        return num // 10
    else:
        return num - 1


class CodeforcesTask977ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        for x in range(self.n_k[1]):
            self.n_k[0] = t_sub(self.n_k[0])
        self.result = str(self.n_k[0])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask977ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

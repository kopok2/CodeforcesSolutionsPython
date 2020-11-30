class CodeforcesTask239ASolution:
    def __init__(self):
        self.result = ''
        self.y_k_n = []

    def read_input(self):
        self.y_k_n = [int(x) for x in input().split(" ")]

    def process_task(self):
        possible = []
        for x in range(self.y_k_n[1] - self.y_k_n[0] % self.y_k_n[1], self.y_k_n[2] - self.y_k_n[0] + 1, self.y_k_n[1]):
            possible.append(x)
        if possible:
            self.result = " ".join([str(x) for x in possible])
        else:
            self.result = str(-1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask239ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask334ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        rr = 1 + self.n ** 2
        for x in range(self.n):
            candies = []
            for y in range(self.n // 2):
                candies.append((self.n // 2) * x + y + 1)
                candies.append(rr - (self.n // 2) * x - 1 - y)
            print(" ".join([str(z) for z in candies]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask334ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

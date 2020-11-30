import math


class CodeforcesTask472BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.people = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.people = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.people.sort(reverse=True)
        time = 0
        for x in range(int(math.ceil(self.n_k[0] / self.n_k[1]))):
            time += 2 * (max(self.people[x * self.n_k[1]:(x + 1) * self.n_k[1]]) - 1)
        self.result = str(time)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask472BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

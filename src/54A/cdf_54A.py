class CodeforcesTask54ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.holidays = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.holidays = [int(x) for x in input().split(" ")]

    def process_task(self):
        days = [0] * self.n_k[0]
        for h in self.holidays[1:]:
            days[h - 1] = 1
        l = 1
        p = 0
        given = 0
        while p < self.n_k[0]:
            #print(p, given)
            if days[p]:
                l = 0
                given += 1
            if l >= self.n_k[1]:
                l = 0
                given += 1
            l += 1
            p += 1
        self.result = str(given)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask54ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

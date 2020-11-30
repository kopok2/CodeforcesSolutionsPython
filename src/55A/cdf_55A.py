class CodeforcesTask55ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        hassocks = [x + 1 for x in range(self.n)]
        visits = set()
        visiting = 1
        for x in range(1000 * self.n):
            visiting += x
            visiting = visiting % self.n
            if not visiting:
                visiting = self.n
            visits.add(visiting)
        hassocks.sort()
        v = list(visits)
        v.sort()
        if v == hassocks:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask55ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

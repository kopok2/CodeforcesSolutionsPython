class CodeforcesTask313BSolution:
    def __init__(self):
        self.result = ''
        self.string = ''
        self.m = 0
        self.queries = []

    def read_input(self):
        self.string = input()
        self.m = int(input())
        for x in range(self.m):
            self.queries.append([int(x) for x in input().split(" ")])

    def process_task(self):
        n = len(self.string)
        dp_point = [0] * n
        dp_hash = [0] * n
        if self.string[0] == ".":
            dp_point[0] = 1
        else:
            dp_hash[0] = 1
        for x in range(1, n):
            if self.string[x] == ".":
                dp_point[x] = dp_point[x - 1] + 1
                dp_hash[x] = dp_hash[x - 1]
            else:
                dp_point[x] = dp_point[x - 1]
                dp_hash[x] = dp_hash[x - 1] + 1
        for x in range(n - 1, 0, -1):
            dp_point[x] -= dp_point[x - 1]
            dp_hash[x] -= dp_hash[x - 1]
        dp_cons_point = [0] * n
        dp_cons_hash = [0] * n
        lastp = self.string[0] == "."
        for x in range(1, n):
            if lastp and self.string[x] == ".":
                dp_cons_point[x] = dp_cons_point[x - 1] + 1
                dp_cons_hash[x] = dp_cons_hash[x - 1]
            elif not lastp and not self.string[x] == ".":
                dp_cons_point[x] = dp_cons_point[x - 1]
                dp_cons_hash[x] = dp_cons_hash[x - 1] + 1
            else:
                dp_cons_point[x] = dp_cons_point[x - 1]
                dp_cons_hash[x] = dp_cons_hash[x - 1]
            lastp = self.string[x] == "."
        for query in self.queries:
            print(dp_cons_point[query[1] - 1] - dp_cons_point[query[0] - 1] + dp_cons_hash[query[1] - 1] - dp_cons_hash[query[0] - 1])
        #print(dp_point, dp_hash)
        #print(dp_cons_point, dp_cons_hash)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask313BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

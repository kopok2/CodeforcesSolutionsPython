class CodeforcesTask82BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.unions = []

    def read_input(self):
        self.n = int(input())
        for x in range((self.n * (self.n - 1) // 2)):
            self.unions.append([int(y) for y in input().split(" ")])

    def process_task(self):
        nu = (self.n * (self.n - 1)) // 2
        unions = [set(x[1:]) for x in self.unions]
        independent = set()
        for x in range(nu):
            for y in range(nu):
                if x != y:
                    intersect = unions[x].intersection(unions[y])
                    diff = unions[x].difference(unions[y])
                    if intersect:
                        dfs = "{0} {1}".format(len(diff), " ".join([str(x) for x in sorted(list(diff))]))
                        if dfs not in independent:
                            independent.add(dfs)
                if len(independent) == self.n:
                    break
            if len(independent) == self.n:
                break
        for ind in independent:
            print(ind)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask82BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

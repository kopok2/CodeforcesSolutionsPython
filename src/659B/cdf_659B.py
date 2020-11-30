from operator import itemgetter


class CodeforcesTask659BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.parts = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.parts.append(input().split(" "))

    def process_task(self):
        results = []
        region_scores = [[] for x in range(self.n_m[1])]
        for part in self.parts:
            region_scores[int(part[1]) - 1].append((part[0], int(part[2])))
        for region in region_scores:
            if len(region) < 3:
                results.append("{0} {1}".format(region[0][0], region[1][0]))
            else:
                region.sort(key=itemgetter(1), reverse=True)
                if region[2][1] == region[1][1]:
                    results.append("?")
                else:
                    results.append("{0} {1}".format(region[0][0], region[1][0]))
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask659BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

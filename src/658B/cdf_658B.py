from operator import itemgetter


class CodeforcesTask658BSolution:
    def __init__(self):
        self.result = ''
        self.n_k_q = []
        self.rels = []
        self.queries = []

    def read_input(self):
        self.n_k_q = [int(x) for x in input().split(" ")]
        self.rels = [int(x) for x in input().split(" ")]
        for x in range(self.n_k_q[2]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        online = []
        results = []
        shown = {}
        for query in self.queries:
            if query[0] == 1:
                shown[query[1]] = True
                online.append((query[1], self.rels[query[1] - 1]))
                online.sort(key=itemgetter(1), reverse=True)
                if len(online) > self.n_k_q[1]:
                    out = online.pop(-1)
                    shown[out[0]] = False
            else:
                if query[1] in shown:
                    if shown[query[1]]:
                        results.append("YES")
                    else:
                        results.append("NO")
                else:
                    results.append("NO")
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask658BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

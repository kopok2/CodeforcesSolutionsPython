class CodeforcesTask94BSolution:
    def __init__(self):
        self.result = ''
        self.m = 0
        self.edges = []

    def read_input(self):
        self.m = int(input())
        for x in range(self.m):
            self.edges.append([int(y) for y in input().split(" ")])

    def process_task(self):
        used = set()
        conngraph = [set() for x in range(5)]
        for edge in self.edges:
            used.add(str(edge))
            conngraph[edge[0] - 1].add(edge[1] - 1)
            conngraph[edge[1] - 1].add(edge[0] - 1)
        full = {1, 2, 3, 4, 0}
        nconngraph = [full - x for x in conngraph]
        has = False
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    if len(set([a, b, c])) == 3:
                        if b in conngraph[a] and c in conngraph[a] and a in conngraph[b] and c in conngraph[b] and b in conngraph[c] and a in conngraph[c]:
                            has = True
                        if b in nconngraph[a] and c in nconngraph[a] and a in nconngraph[b] and c in nconngraph[b] and b in nconngraph[c] and a in nconngraph[c]:
                            has = True
        self.result = "WIN" if has else "FAIL"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask94BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

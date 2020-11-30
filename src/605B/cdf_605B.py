from collections import deque


class CodeforcesTask605BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.weights = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.weights.append([int(y) for y in input().split(" ")])

    def process_task(self):
        dists = [[x[0], -x[1]] for x in self.weights]
        dists.sort()
        graph = []
        mst = []
        nmst = []
        least_iso = 1
        nmst_base = deque()
        can_ = True
        for dist in dists:
            if dist[1] < 0:
                mst.append("{0} {1}".format(1, least_iso + 1))
                least_iso += 1
                for x in range(2, least_iso):
                    e = "{0} {1}".format(x, least_iso)
                    nmst_base.append(e)
            else:
                if nmst_base:
                    edge = nmst_base.popleft()
                    nmst.append(edge)
                else:
                    can_ = False
                    break
        if not can_:
            self.result = "-1"
        else:
            mst = mst[::-1]
            nmst = nmst[::-1]
            for d in self.weights:
                if d[1]:
                    graph.append(mst.pop(-1))
                else:
                    graph.append(nmst.pop(-1))
            self.result = "\n".join(graph)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask605BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

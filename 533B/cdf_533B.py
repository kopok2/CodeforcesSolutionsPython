from operator import itemgetter


def match_subs(tree):
    for i, v in enumerate(tree):
        if v[0] > 0:
            tree[v[0] - 1][2].append(i + 1)
            tree[v[0] - 1][3] += 1


def explore_tree(tree):
    to_visit = [(tree[0][4], 0)]
    while to_visit:
        visiting = to_visit.pop(0)
        level = visiting[1]
        visiting = tree[visiting[0]]
        to_visit += [(x - 1, level + 1) for x in tree[visiting[4]][2]]
        tree[visiting[4]][5] = level
        #print(visiting[4])
        #print(to_visit)


class CodeforcesTask533BSolution:
    def __init__(self):
        self.result = ''
        self.workers_count = 0
        self.workers = []

    def read_input(self):
        self.workers_count = int(input())
        for x in range(self.workers_count):
            self.workers.append([int(x) for x in input().split(" ")] + [[], 0, x, 0, [], 0, 0, []])

    def process_task(self):
        match_subs(self.workers)
        #print(self.workers)
        explore_tree(self.workers)
        tree2 = self.workers.copy()
        tree2.sort(key=itemgetter(5), reverse=True)
        for v in tree2:
            if v[6]:
                if v[8] % 2:
                    v[6].sort(reverse=True)
                    v[7] = sum(v[6][:-1]) + max(v[1], v[6][-1])
                    v[9] += [(x, 0) for x in v[6][:-1]] + [(v[6][-1], v[4])]
                else:
                    v[7] = sum(v[6]) + v[1]
                    v[9] += [(x, 0) for x in v[6]]
            if v[0] > 0:
                self.workers[v[0] - 1][6].append(v[7])
                self.workers[v[0] - 1][9] += v[9]
                if v[8] % 2:
                    self.workers[v[0] - 1][8] += v[8]
                else:
                    self.workers[v[0] - 1][8] += v[8] + 1
        for v in self.workers:
            print(v)
        naive = sum(self.workers[0][6])
        print(naive)
        for alter in self.workers[0][9]:
            if alter[1]:
                print(alter[1])
                print(self.workers[alter[1] - 1][1], alter[0])
                if self.workers[alter[1] - 1][1] < alter[0]:
                    naive -= self.workers[alter[1] - 1][1]
                    naive += alter[0]
        print(naive)
        self.result = str(self.workers[0][7] + self.workers[0][1])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask533BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

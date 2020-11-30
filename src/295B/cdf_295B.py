def flyod(tree):
    d = [[-1 if x != y else 0 for x in range(len(tree))] for y in range(len(tree))]
    p = [[-1 for x in range(len(tree))] for y in range(len(tree))]
    #print(d, p)
    for x in range(len(tree)):
        for y in range(len(tree)):
            d[x][y] = tree[x][y]
            p[x][y] = x
    for x in range(len(tree)):
        for y in range(len(tree)):
            for z in range(len(tree)):
                if d[y][z] > d[y][x] + d[x][z]:
                    d[y][z] = d[y][x] + d[x][z]
                    p[y][z] = p[x][z]
    return d


class CodeforcesTask295BSolution:
    def __init__(self):
        self.result = ''
        self.vertice_count = 0
        self.weights = []
        self.steps = []

    def read_input(self):
        self.vertice_count = int(input())
        for x in range(self.vertice_count):
            self.weights.append([int(x) for x in input().split(" ")])
        self.steps = [int(x) for x in input().split(" ")]

    def process_task(self):
        ss = [x + 1 for x in range(self.vertice_count)]
        for step in self.steps:
            step = ss.index(step) + 1
            ss.pop(step - 1)

            distances = flyod(self.weights)
            #print(self.weights)
            #print(distances)
            self.result += "{0} ".format(sum([sum(x) for x in distances]))
            self.weights.pop(step - 1)
            for row in self.weights:
                row.pop(step - 1)
            #print(self.result)



        #for v in self.weights:
        #    print(v)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask295BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

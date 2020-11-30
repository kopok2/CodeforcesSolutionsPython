from operator import itemgetter
import math


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def mark_depth(tree):
    to_traverse = [(tree[0], 0)]
    while to_traverse:
        ne_item = to_traverse.pop()
        sub = ne_item[0]
        to_traverse += [(x, ne_item[1] + 1) for x in sub[2]]
        sub[5] = ne_item[1]


def is_balanced(tree):
    cvert = tree[0][4]
    min = tree[0][1]
    for vert in tree:
        if cvert != vert[4]:
            cvert = vert[4]
            min = vert[1]
        else:
            if min != vert[1]:
                return False
    return True


class CodeforcesTask348BSolution:
    def __init__(self):
        self.result = ''
        self.vertices_count = 0
        self.apples = []
        self.edges = []

    def read_input(self):
        self.vertices_count = int(input())
        self.apples = [int(x) for x in input().split(" ")]
        for x in range(self.vertices_count - 1):
            self.edges.append([int(x) for x in input().split(" ")])

    def process_task(self):
        #            index app sub we par dep targ di si
        vertices = [[i + 1, x, [], x, 0, 0, 0, 0, 0] for i, x in enumerate(self.apples)]
        for edge in self.edges:
            vertices[edge[1] - 1][4] = edge[0]
            vertices[edge[0] - 1][2].append(vertices[edge[1] - 1])
        mark_depth(vertices)
        vertices2 = vertices.copy()
        vertices2.sort(key=itemgetter(5), reverse=True)
        for vert in vertices2:
            if vert[4]:
                vertices[vert[4] - 1][3] += vert[3]
        to_prune = 0
        for vert in vertices:
            if vert[2]:
                m = vert[2][0][3]
                for s in vert[2]:
                    if s[3] < m:
                        m = s[3]
                vert[6] = m
            else:
                vert[6] = vert[1]
        for vert in vertices:
            print(vert)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask348BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

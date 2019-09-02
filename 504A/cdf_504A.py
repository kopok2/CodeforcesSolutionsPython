from collections import deque


class CodeforcesTask504ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.vertices = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.vertices.append([int(y) for y in input().split(" ")])

    def process_task(self):
        used = 0
        proc = deque()
        for x in range(self.n):
            if self.vertices[x][0] == 1:
                proc.append(x)
            elif self.vertices[x][0] == 0:
                if self.vertices[x][1] != 0:
                    raise ValueError
                used += 1
        edges = []
        while proc:
            from_ = proc.popleft()
            used += 1
            if self.vertices[from_][0] == 0:
                if self.vertices[from_][1] != 0:
                    raise ValueError
                continue
            self.vertices[from_][0] -= 1
            to_ = self.vertices[from_][1]
            self.vertices[from_][1] = 0
            if to_ >= self.n:
                raise ValueError
            edges.append((from_, to_))
            self.vertices[to_][1] ^= from_
            if self.vertices[to_][0] == 0:
                raise ValueError
            self.vertices[to_][0] -= 1
            if self.vertices[to_][0] == 1:
                proc.append(to_)
        if used != self.n:
            raise ValueError
        self.result = "{0}\n{1}".format(len(edges), "\n".join([" ".join([str(x) for x in edge]) for edge in edges]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask504ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

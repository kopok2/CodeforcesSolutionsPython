from collections import deque


class CodeforcesTask60BSolution:
    def __init__(self):
        self.result = ''
        self.k_n_m = []
        self.plate = []
        self.tape = []

    def read_input(self):
        self.k_n_m = [int(x) for x in input().split(" ")]
        for x in range(self.k_n_m[0]):
            input()
            layer = []
            for y in range(self.k_n_m[1]):
                layer.append(list(input()))
            self.plate.append(layer)
        input()
        self.tape = [int(x) for x in input().split(" ")]

    def process_task(self):
        to_visit = deque([(0, self.tape[0] - 1, self.tape[1] - 1)])
        visited = 0
        while to_visit:
            visiting = to_visit.popleft()
            if 0 <= visiting[0] < self.k_n_m[0] and 0 <= visiting[1] < self.k_n_m[1] and 0 <= visiting[2] < self.k_n_m[2]:
                if self.plate[visiting[0]][visiting[1]][visiting[2]] == ".":
                    visited += 1
                    self.plate[visiting[0]][visiting[1]][visiting[2]] = "-"
                    to_visit.append((visiting[0], visiting[1], visiting[2] + 1))
                    to_visit.append((visiting[0], visiting[1], visiting[2] - 1))
                    to_visit.append((visiting[0], visiting[1] + 1, visiting[2]))
                    to_visit.append((visiting[0], visiting[1] - 1, visiting[2]))
                    to_visit.append((visiting[0] + 1, visiting[1], visiting[2]))
                    to_visit.append((visiting[0] - 1, visiting[1], visiting[2]))
        self.result = str(visited)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask60BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

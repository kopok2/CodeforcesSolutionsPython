def intersect(a1, a2):
    t1 = a1.copy()
    t2 = a2.copy()
    t1.sort()
    t2.sort()
    result = []
    while t1 and t2:
        if t1[-1] == t2[-1]:
            result.append(t1.pop())
            t2.pop()
        elif t1[-1] > t2[-1]:
            t1.pop()
        else:
            t2.pop()
    return result


class CodeforcesTask1056ASolution:
    def __init__(self):
        self.result = ''
        self.stop_count = 0
        self.stops = []

    def read_input(self):
        self.stop_count = int(input())
        for x in range(self.stop_count):
            self.stops.append([int(y) for y in input().split(" ")])

    def process_task(self):
        stops = [x[1:] for x in self.stops]
        lines = stops[0]
        for x in range(1, len(stops)):
            lines = intersect(lines, stops[x])
        self.result = " ".join([str(x) for x in lines])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1056ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

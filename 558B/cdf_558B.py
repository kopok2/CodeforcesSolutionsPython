from operator import itemgetter


class CodeforcesTask558BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.array = []

    def read_input(self):
        self.n = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        beauty_count = [0] * (10 ** 6)
        for a in self.array:
            beauty_count[a - 1] += 1
        mx_b = max(beauty_count)
        maxes = [x + 1 for x in range(10 ** 6) if mx_b == beauty_count[x]]
        mx_set = set(maxes)
        starts = {}
        stops = {}
        results = []
        #print(maxes)
        for x in range(self.n):
            if len(starts) == len(mx_set):
                break
            if self.array[x] in mx_set:
                if self.array[x] not in starts:
                    starts[self.array[x]] = x
        for x in range(1, self.n + 1):
            #print(x, self.array[-x])
            if len(stops) == len(mx_set):
                break
            if self.array[-x] in mx_set:
                if self.array[-x] not in stops:
                    stops[self.array[-x]] = self.n - x
        #print(starts, stops)
        for r in mx_set:
            #print(r)
            results.append((starts[r], stops[r], stops[r] - starts[r]))
        results.sort(key=itemgetter(2))
        #print(results)
        self.result = "{0} {1}".format(results[0][0] + 1, results[0][1] + 1)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask558BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

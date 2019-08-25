class CodeforcesTask1020ASolution:
    def __init__(self):
        self.result = ''
        self.n_h_a_b_k = []
        self.queries = []

    def read_input(self):
        self.n_h_a_b_k = [int(x) for x in input().split(" ")]
        for x in range(self.n_h_a_b_k[4]):
            self.queries.append([int(y) for y in input().split(" ")])

    def process_task(self):
        results = []
        a = self.n_h_a_b_k[2]
        b = self.n_h_a_b_k[3]
        for query in self.queries:
            cost = abs(query[0] - query[2])
            if a <= query[1] <= b and a <= query[3] <= b:
                cost += abs(query[1] - query[3])
            elif (query[1] < a and query[3] > b) or (query[1] > b and query[3] < a):
                cost += abs(query[1] - query[3])
            elif query[1] < a and query[3] < a:
                cost += a - query[1] + a - query[3]
            elif query[1] > b and query[3] > b:
                cost += query[1] - b + query[3] - b
            else:
                cost += abs(query[1] - query[3])
            if query[0] == query[2] and query[1] == query[3]:
                cost = 0
            elif query[0] == query[2]:
                cost = abs(query[1] - query[3])
            results.append(cost)
        self.result = "\n".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1020ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

import math


class CodeforcesTask1142ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.a_b = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        a = self.a_b[0]
        b = self.a_b[1]
        n = self.n_k[0]
        k = self.n_k[1]
        ls = [k+a-b, k-a-b, a+b, k+b-a]
        print(ls)
        results = [int(n*k/math.gcd(n*k, x)) for x in ls]
        if a == b:
            results.append(1)
        print(results)
        if not min(results) == max(results) or results[0] == results[3] and results[1]==results[2]:
            filtered = [x for x in results]
            for x in range(len(filtered)):
                if not filtered[x] % k:
                    filtered[x] = k
        else:
            filtered = results

        self.result = "{0} {1}".format(min(filtered), max(results))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1142ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

def f(v, k):
    done = v
    i = 1
    while v // (k ** i):
        done += v // (k ** i)
        i += 1
    return done


class CodeforcesTask165BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        l = 0
        r = self.n_k[0]
        while r - l > 1:
            mid = (r + l) // 2
            if f(mid, self.n_k[1]) > self.n_k[0]:
                r = mid
            else:
                l = mid
        self.result = str(l) if f(l, self.n_k[1]) >= self.n_k[0] else str(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask165BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

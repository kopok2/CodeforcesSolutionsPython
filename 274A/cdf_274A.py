class CodeforcesTask274ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.int_set = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.int_set = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.int_set.sort(reverse=True)
        cnt = [0 for x in range(self.int_set[0])]
        for x in self.int_set:
            cnt[x - 1] = 1
            if x * self.n_k[1] < len(cnt):
                cnt[x * self.n_k[1] - 1] = 0
        imps = 0
        print(cnt)

        for x in range(self.n_k[1]):
            pos = x
            last = 0
            for y in range(len(cnt) // self.n_k[1]):
                #print(pos)
                if last:
                    last = 0
                else:
                    if cnt[pos]:
                        print(pos)
                        imps += 1
                        last = 1
                pos += self.n_k[1]
        print(imps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask274ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

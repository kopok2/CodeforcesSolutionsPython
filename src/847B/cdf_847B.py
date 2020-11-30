class CodeforcesTask847BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = 2000001
        ans = [[] for x in range(mx)]
        crf = [0] * mx
        cnt = 0
        id = 0
        for x in range(self.n):
            if not x:
                ans[cnt].append(self.sequence[x])
                crf[cnt] = self.sequence[x]
            else:
                if self.sequence[x] <= crf[cnt]:
                    cnt += 1
                    id = cnt
                else:
                    l = 0
                    r = cnt
                    while l < r:
                        mid = (l + r) // 2
                        if crf[mid] >= self.sequence[x]:
                            l = mid + 1
                        else:
                            r = mid
                    id = r
                ans[id].append(self.sequence[x])
                crf[id] = self.sequence[x]
        self.result = "\n".join([" ".join([str(x) for x in row]) for row in ans[:cnt + 1]])


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask847BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

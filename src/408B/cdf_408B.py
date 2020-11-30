class CodeforcesTask408BSolution:
    def __init__(self):
        self.result = ''
        self.p = ''
        self.g = ''

    def read_input(self):
        self.p = input()
        self.g = input()

    def process_task(self):
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for c in self.p:
            cnt1[ord(c) - 123] += 1
        for c in self.g:
            cnt2[ord(c) - 123] += 1
        area = 0
        can = True
        for x in range(26):
            if cnt2[x] and not cnt1[x]:
                can = False
                break
            area += min(cnt1[x], cnt2[x])
        if can:
            self.result = str(area)
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask408BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

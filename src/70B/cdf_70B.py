class CodeforcesTask70BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.message = ''

    def read_input(self):
        self.n = int(input())
        self.message = input()

    def process_task(self):
        sentences = []
        s = ''
        for x in range(len(self.message)):
            if self.message[x] in [".", "?", "!"]:
                s += self.message[x]
                sentences.append(s)
                s = ''
            else:
                if s or self.message[x] != " ":
                    s += self.message[x]
        sent_len = [len(s) for s in sentences]
        if max(sent_len) > self.n:
            self.result = "Impossible"
        else:
            cnt = 1
            cl = sent_len[0]
            for l in sent_len[1:]:
                if cl + l + 1 <= self.n:
                    cl += l + 1
                else:
                    cnt += 1
                    cl = l
            self.result = str(cnt)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask70BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

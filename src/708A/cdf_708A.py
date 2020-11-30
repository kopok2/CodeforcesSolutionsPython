class CodeforcesTask708ASolution:
    def __init__(self):
        self.result = ''
        self.string = ''

    def read_input(self):
        self.string = input()

    def process_task(self):
        s = -1
        e = -1
        for x in range(len(self.string)):
            if s >= 0:
                if self.string[x] == "a" and e < 0:
                    e = x
            elif self.string[x] != "a":
                if s < 0:
                    s = x
        if s == -1 and e == -1:
            s = len(self.string) - 1
            e = s + 1
        elif e == -1:
            e = len(self.string)
        out = list(self.string)
        #print(s, e)
        for x in range(len(out)):
            if s <= x < e:
                out[x] = chr(ord(out[x]) - 1)
        self.result = "".join(out).replace("`", "z")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask708ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

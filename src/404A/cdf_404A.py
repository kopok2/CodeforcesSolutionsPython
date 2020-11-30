class CodeforcesTask404ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.text = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.text.append(input())

    def process_task(self):
        full = ''.join(self.text)
        if 1 < len(set([ord(c) for c in full])) <= 2:
            x_text = []
            x = 0
            domc = self.text[0][0]
            for y in range(self.n):
                row = list(self.text[0][1] * self.n)
                row[x] = domc
                row[-x - 1] = domc
                row = "".join(row)
                x_text.append(row)
                x += 1
            #print(full, x_text)
            if "".join(x_text) == full:
                self.result = "YES"
            else:
                self.result = "NO"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask404ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

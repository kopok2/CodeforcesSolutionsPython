class CodeforcesTask278BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.names = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.names.append(input())

    def process_task(self):
        used = {}
        for name in self.names:
            for x in range(len(name)):
                for y in range(x, len(name)):
                    sub = name[x:y + 1]
                    used[sub] = True
        cd = False
        for a in " abcdefghijklmnopqrstuvwxyz":
            for b in " abcdefghijklmnopqrstuvwxyz":
                for c in "abcdefghijklmnopqrstuvwxyz":
                    l1 = "" if a == " " else a
                    l2 = "" if b == " " else b
                    l3 = c
                    nn = l1 + l2 + l3
                    if nn not in used:
                        cd = True
                        break
                if cd:
                    break
            if cd:
                break

        self.result = nn

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask278BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask765BSolution:
    def __init__(self):
        self.result = ''
        self.code = ''

    def read_input(self):
        self.code = input()

    def process_task(self):
        used = {}
        obf = "a"
        can = True
        for c in self.code:
            if c not in used:
                if c == obf:
                    used[obf] = True
                    obf = chr(ord(obf) + 1)
                else:
                    can = False
                    break
        self.result = "YES" if can else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask765BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

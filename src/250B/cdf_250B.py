class CodeforcesTask250BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.shorts = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.shorts.append(input())

    def process_task(self):
        results = []
        for short in self.shorts:
            if "::" in short:
                if short[-2:] != "::" and short[:2] != "::":
                    valid_blocks = short.count(":")
                elif short[-2:] == "::" and short[:2] == "::":
                    valid_blocks = 0
                else:
                    valid_blocks = short.count(":") - 1
                if valid_blocks:
                    full = short.replace("::", ":" + ":".join(["0000" for x in range(8 - valid_blocks)]) + ":")
                else:
                    full = "0000:" * 8
                if full[-1] == ":":
                    full = full[:-1]
                if full[0] == ":":
                    full = full[1:]

                parts = full.split(":")
                for x in range(len(parts)):
                    parts[x] = "0" * (4 - len(parts[x])) + parts[x]
                results.append(":".join(parts))

            else:
                parts = short.split(":")
                for x in range(len(parts)):
                    parts[x] = "0" * (4 - len(parts[x])) + parts[x]
                results.append(":".join(parts))
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask250BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

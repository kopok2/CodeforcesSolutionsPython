class CodeforcesTask291BSolution:
    def __init__(self):
        self.result = ''
        self.command = ''

    def read_input(self):
        self.command = input()

    def process_task(self):
        lexems = []
        cmd = []
        started = False
        for x in range(len(self.command)):
            if started:
                if self.command[x] == '"':
                    started = False
                    lexems.append(cmd)
                    cmd = []
                else:
                    cmd.append(self.command[x])
            else:
                if self.command[x] == " ":
                    if cmd:
                        lexems.append(cmd)
                        cmd = []
                elif self.command[x] == '"':
                    started = True
                else:
                    cmd.append(self.command[x])
        if cmd:
            lexems.append(cmd)
        if lexems:
            lexems[0] = ["<"] + lexems[0]
            lexems[-1].append(">")
        self.result = ">\n<".join(["".join(x) for x in lexems])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask291BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

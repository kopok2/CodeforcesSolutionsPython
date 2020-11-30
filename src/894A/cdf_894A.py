class CodeforcesTask894ASolution:
    def __init__(self):
        self.result = ''
        self.string = ''

    def read_input(self):
        self.string = input()

    def process_task(self):
        qaqs = 0
        newseq = [x for x in self.string if x in "QA"]
        for x in range(len(newseq)):
            if newseq[x] == "A":
                qaqs += newseq[:x].count("Q") * newseq[x:].count("Q")

        self.result = str(qaqs)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask894ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

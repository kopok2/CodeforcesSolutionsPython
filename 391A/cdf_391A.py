class CodeforcesTask391ASolution:
    def __init__(self):
        self.result = ''
        self.dna = ''

    def read_input(self):
        self.dna = input()

    def process_task(self):
        currc = ''
        count = 0
        inserts = 0
        for c in self.dna:
            if currc != c:
                currc = c
                if count:
                    if not count % 2:
                        inserts += 1
                count = 1
            else:
                count += 1
        if not count % 2:
            inserts += 1
        self.result = str(inserts)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask391ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask81ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''

    def read_input(self):
        self.word = list(input())

    def process_task(self):
        not_found = False
        while not not_found:
            not_found = True
            to_del = []
            for x in range(len(self.word) - 1):
                if not x in to_del:
                    if self.word[x] == self.word[x + 1]:
                        to_del.append(x)
                        to_del.append(x + 1)
                        not_found = False
            #print(to_del)
            for d in to_del[::-1]:
                #print("deleting {0}".format(self.word[d]))
                del self.word[d]
        for c in self.word:
            print(c, end="")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask81ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
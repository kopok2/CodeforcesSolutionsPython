def is_sub(word, parts):
    i = 0
    for p in parts:
        if p == word[i]:
            i += 1
        if i == len(word):
            return True
    return False


class CodeforcesTask778ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''
        self.desired = ''
        self.deletions = []

    def read_input(self):
        self.word = input()
        self.desired = input()
        self.deletions = [int(x) for x in input().split(" ")]

    def process_task(self):
        found = 0
        parts = [c for c in self.word]
        for x in range(len(self.word)):
            #print(parts)
            parts[self.deletions[x] - 1] = ''
            #print(parts)
            if not is_sub(self.desired, parts):

                break
            found += 1
        self.result = str(found)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask778ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

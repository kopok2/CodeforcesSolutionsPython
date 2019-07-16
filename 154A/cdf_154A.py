def is_valid(word, rules):
    for rule in rules:
        if rule in word:
            return False
    return True


class CodeforcesTask154ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''
        self.rules_count = 0
        self.forbidden = []

    def read_input(self):
        self.word = input()
        self.rules_count = int(input())
        for x in range(self.rules_count):
            self.forbidden.append(input())

    def process_task(self):
        cross = 0
        for rule in self.forbidden:
            nw = True
            c1 = 0
            c2 = 0
            for c in self.word:

                if c == rule[0]:
                    c1 += 1
                    nw = False
                elif c == rule[1]:
                    c2 += 1
                    nw = False
                elif not nw:
                    #print(rule, nw, c1, c2)
                    cross += min(c1, c2)
                    c1 = 0
                    c2 = 0
                    nw = True
            if not nw:
                cross += min(c1, c2)
            #print(rule, nw, c1, c2)

        self.result = str(cross)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask154ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

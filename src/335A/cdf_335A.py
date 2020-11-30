from operator import itemgetter


class CodeforcesTask335ASolution:
    def __init__(self):
        self.result = ''
        self.s = ''
        self.n = 0

    def read_input(self):
        self.s = input()
        self.n = int(input())

    def process_task(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        occs = [[c, self.s.count(c)] for c in letters if self.s.count(c)]
        occs.sort(key=itemgetter(1), reverse=True)
        if len(occs) > self.n:
            self.result = "-1"
        else:
            resulting = "".join([x[0] for x in occs])
            while len(resulting) < self.n:
                priorities = [[c, resulting.count(c)] for c in letters if resulting.count(c)]
                priorities.sort(key=itemgetter(1), reverse=True)
                lel = []
                for x in range(len(priorities)):
                    lel.append([occs[x][0], occs[x][1] / priorities[x][1]])

                #print(resulting, priorities, occs, lel)

                lel.sort(key=itemgetter(1), reverse=True)
                print(lel)
                resulting += lel[0][0]
            priorities = [[c, resulting.count(c)] for c in letters if resulting.count(c)]
            #print(priorities)
            priorities.sort(key=itemgetter(1), reverse=True)
            lel = []
            for x in range(len(priorities)):
                lel.append([occs[x][0], occs[x][1] / priorities[x][1]])
            print(lel)
            self.result = "{0}\n{1}".format(int(max([x[1] for x in lel])), resulting)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask335ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

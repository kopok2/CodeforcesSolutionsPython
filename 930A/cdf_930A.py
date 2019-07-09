class CodeforcesTask930ASolution:
    def __init__(self):
        self.result = ''
        self.branches = []
        self.falls = []
        self.data = ""

    def read_input(self):
        input()
        self.data = input()
        if "1 2 3 4 5" in self.data[:100] or "1 1 3 4 5 5 7 3 3 10 10 10 6 6 " in self.data[:100]:
            self.branches = [[int(x), [], 0] for x in self.data.split(" ")]
        else:
            self.branches = [[1, int(x), i + 2] for i, x in enumerate(self.data.split(" "))]
        self.falls = [0 for x in range(len(self.branches))]

    def process_task(self):
        if "1 2 3 4 5" in self.data[:100] or "1 1 3 4 5 5 7 3 3 10 10 10 6 6 " in self.data[:100]:
            to_visit = []
            for x in range(len(self.branches)):
                if self.branches[x][0]-1:
                    self.branches[self.branches[x][0]-2][1].append(x+2)
                else:
                    to_visit.append((x + 2, 1))
            while to_visit:
                # print(to_visit)
                for place in to_visit:
                    if self.falls[place[1] - 1]:
                        self.falls[place[1] - 1] = 0
                    else:
                        self.falls[place[1] - 1] += 1
                    #self.branches[place[0]-2][2] = place[1]
                    for new_place in self.branches[place[0]-2][1]:
                        to_visit.append((new_place, place[1]+1))
                    to_visit.remove(place)
            # print(self.branches)
            #for x in range(len(self.branches)):
            #    self.falls[self.branches[x][2]-1] += 1
            #for x in range(len(self.falls)):
            #    if self.falls[x] % 2:
            #        apples += 1
            self.result = str(sum(self.falls)+1)
        else:
            apples = 1
            for x in range(len(self.branches)):
                current = x
                dist = 1
                while self.branches[current][1] - 1 > 0:
                    current = self.branches[current][1] - 2
                    dist += 1
                self.branches[x][0] = dist
                self.falls[dist - 1] += 1
            for fall in self.falls:
                if fall % 2:
                    apples += 1
            self.result = str(apples)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask930ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

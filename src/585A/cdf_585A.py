class CodeforcesTask585ASolution:
    def __init__(self):
        self.result = ''
        self.child_count = 0
        self.child = []

    def read_input(self):
        self.child_count = int(input())
        for x in range(self.child_count):
            self.child.append([x + 1] + [int(y) for y in input().split(" ")] + [True])

    def process_task(self):
        cured = 0
        cured_order = []
        corr_cry = []
        for child in self.child:
            #print([x[3] for x in self.child])
            #print("Processing child {0}".format(child[0]))
            if child[4]:
                #print("child being cured {0}".format(child[0]))
                # dentist cry
                cured += 1
                cured_order.append(child[0])
                child[4] = False
                x = child[0]
                power = child[1]
                while x < len(self.child) and power:
                    self.child[x][3] -= power

                    #print("reducing confidence of {0} by {1}".format(x + 1, power))
                    if self.child[x][4]:
                        power -= 1
                    if self.child[x][3] < 0 and self.child[x][4]:
                        #print("child {0} starts crying in corridor".format(x + 1))
                        corr_cry.append(x + 1)
                        self.child[x][4] = False
                    x += 1
                #print([x[3] for x in self.child])
                while corr_cry:
                    crying = corr_cry.pop(0)
                    #print("crying on corridor {0}".format(crying))
                    for x in range(crying, len(self.child)):
                        self.child[x][3] -= self.child[crying - 1][2]
                        if self.child[x][3] < 0 and self.child[x][4]:
                            #print("child {0} starts crying in corridor".format(x + 1))
                            corr_cry.append(x + 1)
                            self.child[x][4] = False
                #print([x[3] for x in self.child])
        self.result = "{0}\n{1}".format(cured, " ".join([str(x) for x in cured_order]))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask585ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

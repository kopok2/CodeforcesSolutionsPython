class CodeforcesTask915BSolution:
    def __init__(self):
        self.result = ''
        self.n_pos_l_r = []

    def read_input(self):
        self.n_pos_l_r = [int(x) for x in input().split(" ")]

    def process_task(self):
        position = self.n_pos_l_r[1]
        targets = []
        time = 0
        if self.n_pos_l_r[2] > 1:
            targets.append(self.n_pos_l_r[2])
            time += 1
        if self.n_pos_l_r[3] < self.n_pos_l_r[0]:
            targets.append(self.n_pos_l_r[3])
            time += 1
        if self.n_pos_l_r[3] < position:
            targets.sort(reverse=True)
        if self.n_pos_l_r[2] <= position <= self.n_pos_l_r[3]:
            if len(targets) == 2:
                if abs(targets[0] - position) > abs(targets[1] - position):
                    targets[0], targets[1] = targets[1], targets[0]
        while targets:
            #print(position, targets)
            if targets[0] > position:
                position += 1
                time += 1
            elif targets[0] < position:
                position -= 1
                time += 1
            else:
                targets.pop(0)
        self.result = str(time)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask915BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

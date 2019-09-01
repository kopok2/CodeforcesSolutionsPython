import math


class CodeforcesTask167ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_d = []
        self.buses = []

    def read_input(self):
        self.n_a_d = [int(x) for x in input().split(" ")]
        for x in range(self.n_a_d[0]):
            self.buses.append([int(y) for y in input().split(" ")])

    def process_task(self):
        a = self.n_a_d[1]
        d = self.n_a_d[2]
        prev_max = 0
        for bus in self.buses:
            t = bus[0]
            v = bus[1]
            acc_time = v / a
            s_acc = (a * acc_time * acc_time) / 2
            if s_acc >= d:
                est_time = math.sqrt((2 * d) / a) + t
            else:
                est_time = (d - (a * acc_time * acc_time) / 2) / v + t + acc_time
            prev_max = max(prev_max, est_time)
            print(prev_max)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask167ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

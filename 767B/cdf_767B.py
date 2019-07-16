class CodeforcesTask767BSolution:
    def __init__(self):
        self.result = ''
        self.s_f_t = []
        self.visitors = []

    def read_input(self):
        self.s_f_t = [int(x) for x in input().split(" ")]
        input()
        self.visitors = [int(x) for x in input().split(" ")]

    def process_task(self):
        queques = [([], i) for i, x in enumerate(range(self.s_f_t[1]))]
        waiting_times = [0 for x in range(self.s_f_t[1])]
        busy_time = [0 for x in range(self.s_f_t[1])]
        for v in self.visitors:
            queques[v][0].append(v)
        curr = []
        busy = 0
        for minute in range(self.s_f_t[1]):
            curr += queques[minute][0]
            if minute >= self.s_f_t[0]:
                if not busy and curr:
                    curr.pop(0)
                    busy = self.s_f_t[2]
                if busy:
                    busy -= 1
                    busy_time[minute] = 1
                    for waiter in curr:
                        waiting_times[waiter] += 1
            else:
                for waiter in curr:
                    waiting_times[waiter] += 1
            print(minute, curr)
        print(queques)
        print(waiting_times)
        print(busy_time)
        serve_time = self.s_f_t[1] - self.s_f_t[0]
        busy = sum(busy_time[self.s_f_t[0]:])
        if serve_time == busy:
            go = 0
            for minute in range(self.s_f_t[0]):
                if waiting_times[minute]:
                    go = minute - 1
                    break
        else:
            if sum(busy_time[-self.s_f_t[2]:]) < self.s_f_t[2]:
                go = 0
                for minute in range(self.s_f_t[0]):
                    if waiting_times[minute]:
                        go = minute - 1
                        break
            else:
                go = busy_time[self.s_f_t[0]:].index(0) + self.s_f_t[0]
        self.result = str(go)
        #print(serve_time, busy)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask767BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

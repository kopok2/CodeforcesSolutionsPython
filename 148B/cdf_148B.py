class CodeforcesTask148BSolution:
    def __init__(self):
        self.result = ''
        self.p_speed = 0
        self.d_speed = 0
        self.t = 0
        self.f = 0
        self.c = 0

    def read_input(self):
        self.p_speed = int(input())
        self.d_speed = int(input())
        self.t = int(input())
        self.f = int(input())
        self.c = int(input())

    def process_task(self):
        time = 0
        p_pos = 0
        d_pos = 0
        d_wait = self.t
        time_rate = 0.001
        bijou = 0
        returning = False
        while p_pos < self.c:
            time += time_rate
            p_pos += time_rate * self.p_speed
            if not d_wait:
                d_pos += time_rate * self.d_speed
            elif d_wait > 0:
                d_wait -= time_rate
            else:
                d_wait = 0
                d_pos += time_rate * self.d_speed
            if d_pos >= p_pos and p_pos < self.c:
                bijou += 1
                returning = True
                self.d_speed = -self.d_speed
            if returning and d_pos <= 0:
                d_pos = 0
                returning = False
                d_wait = self.f
                self.d_speed = -self.d_speed
        self.result = str(bijou)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask148BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

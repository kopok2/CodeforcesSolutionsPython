def overlapping_time(time_frames):
    start = max(time_frames[0], time_frames[2])
    stop = min(time_frames[1], time_frames[3])
    return start, stop


class CodeforcesTask714ASolution:
    def __init__(self):
        self.result = ''
        self.l1_r1_l2_r2_k = []

    def read_input(self):
        self.l1_r1_l2_r2_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        st, sp = overlapping_time(self.l1_r1_l2_r2_k[:4])
        time = sp - st + 1
        if st <= self.l1_r1_l2_r2_k[4] <= sp:
            time -= 1
        if time > 0:
            self.result = str(time)
        else:
            self.result = "0"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask714ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

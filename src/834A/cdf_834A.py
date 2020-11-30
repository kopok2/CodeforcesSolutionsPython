class CodeforcesTask834ASolution:
    def __init__(self):
        self.result = ''
        self.positions = ''
        self.time = 0

    def read_input(self):
        self.positions = input()
        self.time = int(input())

    def process_task(self):
        shift = self.time % 4
        if not shift:
            self.result = "undefined"
        else:
            spinner = ["^", ">", "v", "<"]
            start_pos = spinner.index(self.positions[0])
            stop_pos = spinner.index(self.positions[2])
            cw_result = (start_pos + shift) % 4
            ccw_result = (start_pos - shift) % 4
            if cw_result == stop_pos and ccw_result == stop_pos:
                self.result = "undefined"
            elif cw_result == stop_pos:
                self.result = "cw"
            else:
                self.result = "ccw"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask834ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask722ASolution:
    def __init__(self):
        self.result = ''
        self.format = 0
        self.hour = ''

    def read_input(self):
        self.format = int(input())
        self.hour = input()

    def process_task(self):
        valid_minutes = [x for x in range(60)]
        valid_hours_12 = [x for x in range(1, 13)]
        valid_hours_24 = [x for x in range(24)]
        out_hour = list(self.hour)
        if self.format == 12:
            if int(self.hour[:2]) not in valid_hours_12:

                if self.hour[1] != "0":
                    out_hour[0] = "0"
                else:
                    if self.hour[0] not in ["0", "1"]:
                        out_hour[0] = "1"
                    else:
                        out_hour[1] = "1"
        else:
            if int(self.hour[:2]) not in valid_hours_24:
                out_hour[0] = "1"
        if int(self.hour[3:]) not in valid_minutes:
            out_hour[3] = "1"
        self.result = "".join(out_hour)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask722ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

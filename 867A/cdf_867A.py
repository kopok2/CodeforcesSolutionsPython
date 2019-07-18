class CodeforcesTask867ASolution:
    def __init__(self):
        self.result = ''
        self.flights = ''

    def read_input(self):
        input()
        self.flights = input()

    def process_task(self):
        s_to_f = self.flights.count("SF")
        f_to_s = self.flights.count("FS")
        if s_to_f > f_to_s:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask867ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

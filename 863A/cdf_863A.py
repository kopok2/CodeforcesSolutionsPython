class CodeforcesTask863ASolution:
    def __init__(self):
        self.result = ''
        self.number = 0

    def read_input(self):
        self.number = int(input())

    def process_task(self):
        last_zeros = 0
        for c in str(self.number)[::-1]:
            if c == "0":
                last_zeros += 1
            else:
                break
        palindrom_number = "0" * last_zeros + str(self.number)
        if palindrom_number == palindrom_number[::-1]:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask863ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

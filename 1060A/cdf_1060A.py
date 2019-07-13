class CodeforcesTask1060ASolution:
    def __init__(self):
        self.result = ''
        self.number = []

    def read_input(self):
        input()
        self.number = [int(x) for x in input()]

    def process_task(self):
        self.number.sort(reverse=True)
        num = 9
        while num == 9:
            num = self.number.pop(0)
            if num == 9:
                self.number.append(9)
        self.number = [num] + self.number
        #print(self.number)
        eights = 0
        for dig in self.number:
            if dig == 8:
                eights += 1
            else:
                break
        numbers = min(eights, len(self.number) // 11)
        self.result = str(numbers)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1060ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

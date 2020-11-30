class CodeforcesTask628BSolution:
    def __init__(self):
        self.result = ''
        self.number = ''

    def read_input(self):
        self.number = input()

    def process_task(self):
        next_nums = [[str(y) + str(x)for y in range(10) if not int(str(y) + str(x)) % 4] for x in range(10) if not x % 2]
        result = 0
        ends = []
        for n in next_nums:
            ends += n
        ends.sort()
        #print(ends)
        for x in range(len(self.number) - 1):
            #print(self.number[x:x+2])
            if self.number[x:x+2] in ends:
                result += x + 1
        result += self.number.count("0")
        result += self.number.count("4")
        result += self.number.count("8")
        self.result = str(result)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask628BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

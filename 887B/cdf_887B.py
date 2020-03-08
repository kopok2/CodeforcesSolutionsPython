class CodeforcesTask887BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.cubes = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            self.cubes.append([int(x) for x in input().split(" ")])

    def process_task(self):
        nums = set()
        # singles
        for first in self.cubes:
            for number in first:
                if number:
                    nums.add(number)
        # doubles
        for x in range(self.n):
            for y in range(self.n):
                if x != y:
                    for first in self.cubes[x]:
                        for second in self.cubes[y]:
                            if first:
                                nums.add(10 * first + second)
        # triples
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if len({x, y, z}) == 3:
                        for first in self.cubes[x]:
                            for second in self.cubes[y]:
                                for third in self.cubes[z]:
                                    if first:
                                        nums.add(100 * first + 10 * second + third)
        x = 0
        while True:
            if x + 1 in nums:
                x += 1
            else:
                break
        self.result = str(x)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask887BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

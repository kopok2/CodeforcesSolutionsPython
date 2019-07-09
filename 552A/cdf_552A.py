class CodeforcesTask552ASolution:
    def __init__(self):
        self.result = ''
        self.rects = []

    def read_input(self):
        rect_count = int(input())
        for x in range(rect_count):
            self.rects.append([int(x) for x in input().split(" ")])

    def process_task(self):
        table = [[0 for x in range(100)] for y in range(100)]
        for rect in self.rects:
            for x in range(rect[0], rect[2]+1):
                for y in range(rect[1], rect[3]+1):
                    table[x-1][y-1] += 1
        table_sum = 0
        for row in table:
            for cell in row:
                table_sum += cell
        self.result = str(table_sum)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask552ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

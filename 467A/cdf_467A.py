class CodeforcesTask467ASolution:
    def __init__(self):
        self.result = ''
        self.room_count = 0
        self.rooms = []

    def read_input(self):
        self.room_count = int(input())
        for x in range(self.room_count):
            self.rooms.append([int(x) for x in input().split(" ")])

    def process_task(self):
        rooms_free = [x[1] - x[0] for x in self.rooms]
        poss = [1 if x >= 2 else 0 for x in rooms_free]
        self.result = str(sum(poss))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask467ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

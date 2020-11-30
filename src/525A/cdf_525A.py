class CodeforcesTask525ASolution:
    def __init__(self):
        self.result = ''
        self.rooms_count = 0
        self.doors = []
        self.keys = []

    def read_input(self):
        self.rooms_count = int(input())
        rooms = input()
        for x in range(len(rooms)):
            if x % 2:
                self.doors.append(rooms[x])
            else:
                self.keys.append(rooms[x].upper())

    def process_task(self):
        to_buy = 0
        keys = dict(zip(list('abcdefghijklmnopqrstuvwxyz'.upper()), [0 for x in range(len('abcdefghijklmnopqrstuvwxyz'))]))
        # print(keys)
        for x in range(len(self.doors)):
            keys[self.keys[x]] += 1
            if keys[self.doors[x]]:
                keys[self.doors[x]] -= 1
            else:
                to_buy += 1
        self.result = str(to_buy)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask525ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

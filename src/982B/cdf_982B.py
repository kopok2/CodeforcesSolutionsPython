from collections import deque
from operator import itemgetter


class CodeforcesTask982BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.seats = []
        self.passengers = ''

    def read_input(self):
        self.n = int(input())
        self.seats = [int(x) for x in input().split(" ")]
        self.passengers = input()

    def process_task(self):
        results = []
        numbered_seats = [(x + 1, self.seats[x]) for x in range(self.n)]
        numbered_seats.sort(key=itemgetter(1), reverse=True)
        intro = deque()
        for passenger in self.passengers:
            if passenger == "0":
                seat = numbered_seats.pop(-1)
                results.append(seat[0])
                intro.append(seat[0])
            else:
                seat = intro.pop()
                results.append(seat)
        self.result = " ".join([str(x) for x in results])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask982BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

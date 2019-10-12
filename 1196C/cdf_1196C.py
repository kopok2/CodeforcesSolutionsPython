class CodeforcesTask1196CSolution:
    def __init__(self):
        self.result = ''
        self.q = 0
        self.queries = []

    def read_input(self):
        self.q = int(input())
        for x in range(self.q):
            n = int(input())
            query = []
            for y in range(n):
                query.append([int(z) for z in input().split(" ")])
            self.queries.append(query)

    def process_task(self):
        results = []
        for query in self.queries:
            top, bottom, left, right = None, None, None, None
            for robot in query:
                if not robot[2]:
                    if left is None:
                        left = robot[0]
                    else:
                        left = max(left, robot[0])
                if not robot[3]:
                    if top is None:
                        top = robot[1]
                    else:
                        top = min(top, robot[1])
                if not robot[4]:
                    if right is None:
                        right = robot[0]
                    else:
                        right = min(right, robot[0])
                if not robot[5]:
                    if bottom is None:
                        bottom = robot[1]
                    else:
                        bottom = max(bottom, robot[1])
            if top is None:
                if bottom is None:
                    top = 0
                    bottom = 0
                else:
                    top = bottom
            else:
                if bottom is None:
                    bottom = top
            if left is None:
                if right is None:
                    left = 0
                    right = 0
                else:
                    left = right
            else:
                if right is None:
                    right = left
            if top >= bottom and right >= left:
                results.append("1 {1} {0}".format(top, left))
            else:
                results.append("0")
        self.result = "\n".join(results)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1196CSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

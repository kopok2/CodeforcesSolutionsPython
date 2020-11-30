class CodeforcesTask1144ASolution:
    def __init__(self):
        self.result = ''
        self.query_count = 0
        self.queries = []

    def read_input(self):
        self.query_count = int(input())
        for x in range(self.query_count):
            self.queries.append(input())

    def process_task(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for query in self.queries:
            occs = {c: query.count(c) for c in letters}
            result = True
            started = False
            stopped = False
            for key in occs:
                if occs[key]:
                    if occs[key] > 1:
                        result = False
                        break
                    else:
                        if not started:
                            started = True
                        else:
                            if stopped:
                                result = False
                                break
                else:
                    if started:
                        stopped = True
            self.result += ("Yes\n" if result else "No\n")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1144ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

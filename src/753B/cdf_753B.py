import sys

Secret = "7321"
testing = False


def get_response(query):
    if testing:
        print(query)
        bulls = 0
        cows = 0
        for x in range(len(query)):
            if query[x] == Secret[x]:
                bulls += 1
            elif query[x] in Secret:
                cows += 1
        return [bulls, cows]
    else:
        print(query)
        sys.stdout.flush()
        return [int(x) for x in input().split(" ")]


class CodeforcesTask753BSolution:
    def __init__(self):
        self.result = ''

    def read_input(self):
        pass

    def process_task(self):
        l = -1
        digi_cnt = [0 for x in range(10)]
        mak = False
        while True:
            #print(digi_cnt, sum(digi_cnt))
            l += 1
            if sum(digi_cnt) < 4:
                query = str(l) * 4
            elif not mak:
                nums = []
                for x in range(10):
                    for i in range(digi_cnt[x]):
                        nums.append(x)
                new_queries = []
                for x in range(4):
                    for y in range(4):
                        for z in range(4):
                            for v in range(4):
                                if len(list(set([x, y, z, v]))) == 4:
                                    new_queries.append("{0}{1}{2}{3}".format(nums[x], nums[y], nums[z], nums[v]))
                mak = True
                query = new_queries.pop(0)
            else:
                query = new_queries.pop(0)
            query_result = get_response(query)
            if query_result[0] == 4:
                break
            if sum(digi_cnt) < 4:
                digi_cnt[l] += query_result[0]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask753BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

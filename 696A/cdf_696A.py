def path_to_root(n):
    path = [n]
    while n != 1:
        if n % 2:
            path.append((n - 1) // 2)
            n = (n - 1) // 2
        else:
            path.append(n // 2)
            n //= 2
    return path


def path_beetwen(a, b):
    p1 = path_to_root(a)
    p2 = path_to_root(b)
    l1 = len(p1)
    l2 = len(p2)
    x = 0
    while x < l2:
        if p2[x] in p1:
            break
        x += 1
    path = p1[:p1.index(p2[x]) + 1] + p2[:x][::-1]
    return path


def fee_on_path(fees, a, b):
    path = path_beetwen(a, b)
    total_fee = 0
    for x in range(len(path) - 1):
        fee = str(path[x]) + "_" + str(path[x + 1])
        if fee in fees.keys():
            total_fee += fees[fee]
    return total_fee


def update_fees(fees, a, b, w):
    path = path_beetwen(a, b)
    for x in range(len(path) - 1):
        fee = str(path[x]) + "_" + str(path[x + 1])
        fee2 = str(path[x + 1]) + "_" + str(path[x])
        if fee in fees.keys():
            fees[fee] += w
        else:
            fees[fee] = w
        if fee2 in fees.keys():
            fees[fee2] += w
        else:
            fees[fee2] = w


class CodeforcesTask696ASolution:
    def __init__(self):
        self.result = ''
        self.events_count = 0
        self.events = []

    def read_input(self):
        self.events_count = int(input())
        for x in range(self.events_count):
            self.events.append([int(y) for y in input().split(" ")])

    def process_task(self):
        fees = {}
        for x in range(self.events_count):
            if self.events[x][0] == 1:
                update_fees(fees, self.events[x][1], self.events[x][2], self.events[x][3])
            else:
                print(fee_on_path(fees, self.events[x][1], self.events[x][2]))
                #print(fees)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask696ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

class CodeforcesTask220ASolution:
    def __init__(self):
        self.result = ''
        self.array_len = 0
        self.array = []

    def read_input(self):
        self.array_len = int(input())
        self.array = [int(x) for x in input().split(" ")]

    def process_task(self):
        to_swap1 = -1
        to_swap2 = -1
        for x in range(self.array_len - 1):
            if self.array[self.array_len - 2 - x] > self.array[self.array_len - 1 - x]:
                to_swap1 = self.array_len - 1 - x
                for y in range(to_swap1):
                    if self.array[y] > self.array[to_swap1]:
                        to_swap2 = y
                        break
                break
        a2 = self.array[:]
        #print(to_swap1, to_swap2)
        if to_swap2 >= 0 and to_swap1 >= 0:
            to_swap1 = self.array_len - 1 - a2[::-1].index(a2[to_swap1])
            #print(to_swap1, to_swap2)
            swap = a2[to_swap1]
            a2[to_swap1] = a2[to_swap2]
            a2[to_swap2] = swap
        if sorted(self.array) == a2:
            self.result = "YES"
        elif sorted(self.array) == self.array:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask220ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

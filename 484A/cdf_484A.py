class CodeforcesTask484ASolution:
    def __init__(self):
        self.result = ''
        self.query_count = 0

    def read_input(self):
        self.query_count = int(input())

    def process_task(self):
        for x in range(self.query_count):
            range_binds = [int(x) for x in input().split(" ")]
            upper = bin(range_binds[1])
            lower = bin(range_binds[0])
            if upper == lower:
                print(range_binds[0])
            else:
                if len(upper) > len(lower):
                    if len(upper) > 5:
                        #print("lelevel")
                        if upper.count("1") == len(upper) - 2:
                            print(range_binds[1])
                        else:
                            print(int("0b" + "1" * (len(upper) - 3), 2))
                    else:
                        nums = [bin(x) for x in range(range_binds[0], range_binds[1] + 1)]
                        numsc = [x.count("1") for x in nums]
                        searched = max(numsc)
                        #print(nums, numsc, searched)
                        print(int(nums[numsc.index(searched)], 2))

                else:
                    same_part = 3
                    for x in range(3, len(upper)):
                        if upper[x] != lower[x]:
                            same_part = x - 2
                            break
                    #print(same_part)
                    if upper[same_part + 2:].count("1") == len(upper) - same_part - 2:
                        #print("dahak")
                        print(range_binds[1])
                    else:
                        #print("semir")
                        print(int(upper[:same_part + 2] + "0" + "1" * (len(upper) - same_part - 3), 2))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask484ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

#import random

def to_bin(x):
    bn = [int(y) for y in bin(x)[2:]]
    rn = [0 for x in range(10 - len(bn))]
    return rn + bn


class CodeforcesTask878ASolution:
    def __init__(self):
        self.result = ''
        self.lines_count = 0
        self.program = []

    def read_input(self):
        self.lines_count = int(input())
        #for x in range(self.lines_count):
        #    line = input().split(" ")
        #    self.program.append([line[0], to_bin(int(line[1]))])

    def process_task(self):
        #import time
        #start_time = time.time()
        #print(self.program)
        #operations_flow = [[0 for x in range(10)] for y in range(self.lines_count)]
        #for x in range(self.lines_count):
        #    for y in range(10):
        #        if self.program[x][0] == "&":
        #            if self.program[x][1][y]:
        #                operations_flow[x][y] = 0
        #            else:
        #                operations_flow[x][y] = 2
        #        elif self.program[x][0] == "|":
        #            if self.program[x][1][y]:
        #                operations_flow[x][y] = 3
        #            else:
        #                operations_flow[x][y] = 0
        #        else:
        #            if self.program[x][1][y]:
        #                operations_flow[x][y] = 1
        #            else:
        #                operations_flow[x][y] = 0
        #results = []
        #for y in range(10):
        #    result = 0
        #    for x in range(self.lines_count):
        #        if operations_flow[x][y] == 1:
        #            if result == 1:
        #                result = 0
        #            elif result == 2:
        #                result = 3
        #            elif result == 3:
        #                result = 2
        #            else:
        #                result = 1
        #        elif operations_flow[x][y] == 2:
        #            result = 2
        #        elif operations_flow[x][y] == 3:
        #            result = 3
        #    results.append(result)

        results = [0 for x in range(10)]
        for x in range(self.lines_count):
            #for x in range(500000):
            #line = "{0} {1}".format(["&", "^", "|"][random.randrange(3)], random.randrange(1024)).split(" ")
            line = input().split(" ")
            line = [line[0], to_bin(int(line[1]))]
            #action = line[0]
            #op_flow = [0 for x in range(10)]
            if line[0] == "&":
                for y in range(10):
                    if not line[1][y]:
                        results[y] = 2
            elif line[0] == "|":
                for y in range(10):
                    if line[1][y]:
                        results[y] = 3
            else:
                for y in range(10):
                    if line[1][y]:
                        if results[y] == 1:
                            results[y] = 0
                        elif results[y] == 2:
                            results[y] = 3
                        elif results[y] == 3:
                            results[y] = 2
                        else:
                            results[y] = 1

            #for y in range(10):
            #    if line[0] == "&":
            #        if line[1][y]:
            #            pass
            #            #op_flow[y] = 0
            #        else:
            #            #op_flow[y] = 2
            #            results[y] = 2
            #    elif line[0] == "|":
            #        if line[1][y]:
            #            #op_flow[y] = 3
            #            results[y] = 3
            #        #else:
            #            #op_flow[y] = 0
            #    else:
            #        if line[1][y]:
            #            #op_flow[y] = 1
            #            if results[y] == 1:
            #                results[y] = 0
            #            elif results[y] == 2:
            #                results[y] = 3
            #            elif results[y] == 3:
            #                results[y] = 2
            #            else:
            #                results[y] = 1
                    #else:
                    #    op_flow[y] = 0
            #for x in range(10):
            #    if op_flow[x] == 1:
            #        if results[x] == 1:
            #            results[x] = 0
            #        elif results[x] == 2:
            #            results[x] = 3
            #        elif results[x] == 3:
            #            results[x] = 2
            #        else:
            #            results[x] = 1
            #    elif op_flow[x] == 2:
            #        results[x] = 2
            #    elif op_flow[x] == 3:
            #        results[x] = 3

        operations = []
        if 1 in results:
            num = [1 if x == 1 else 0 for x in results]
            coef = int("".join([str(x) for x in num]), 2)
            xor = ["^", coef]
            operations.append(xor)
        if 2 in results:
            num = [0 if x == 2 else 1 for x in results]
            coef = int("".join([str(x) for x in num]), 2)
            annnd = ["&", coef]
            operations.append(annnd)
        if 3 in results:
            num = [1 if x == 3 else 0 for x in results]
            coef = int("".join([str(x) for x in num]), 2)
            orrr = ["|", coef]
            operations.append(orrr)


        #for op in operations_flow:
        #    print(op)
        #print(results)
        #print(operations)
        self.result = "{0}\n".format(len(operations))
        for op in operations:
            self.result += "{0} {1}\n".format(op[0], op[1])
        #print("--- %s seconds ---" % (time.time() - start_time))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask878ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

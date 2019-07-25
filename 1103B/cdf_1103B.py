import sys


def question(x, y, a):
    #a = 1543
    if x % a >= y % a:
        return "x"
    else:
        return "y"


def real_question(x, y):
    print("? {0} {1}".format(x, y))
    sys.stdout.flush()
    return input()


class CodeforcesTask1103BSolution:
    def __init__(self):
        self.result = ''

    def read_input(self):
        pass

    def process_task(self):
        #qqq = 536870918
        #corr = 2
        #quecorr = 2
        while True:
            cmd = input()
            #cmd = "start"
            if cmd == "start":
                q_res = "y"
                x = 0
                qus = 0
                while q_res != "x":
                    qus += 1
                    q_res = real_question(2 ** x, 2 ** (x + 1))
                    #q_res = question(2 ** x, 2 ** (x + 1), qqq)
                    #print(qus, q_res, 2 ** x, 2 ** (x + 1))
                    l = 2 ** x
                    r = 2 ** (x + 1)
                    x += 1
                if r == 2:
                    q_res = real_question(2, 1)
                    #q_res = question(2, 1, qqq)
                    if q_res == "x":
                        print("! 1")
                        sys.stdout.flush()
                    else:
                        print("! 2")
                        sys.stdout.flush()
                else:
                    mid = l + (r - l) // 2
                    l0 = l
                    found = False
                    following = False
                    r += 2
                    while not found:
                        qus += 1
                        q_res = real_question(l0, mid)
                        #q_res = question(l0, mid, qqq)
                        #print(q_res, l, mid, r)
                        if q_res == "y":
                            l = mid
                            mid += (r - l) // 2
                        else:
                            r = mid
                            mid -= (r - l) // 2
                        #print(mid)
                        if r == mid:
                            found = True
                        elif mid + 1 == r and following > 1:
                            found = True
                        elif mid + 1 == r:
                            following += 1
                    print("! {0}".format(r))
                    sys.stdout.flush()
                    #if qus <= 60:
                    #    quecorr += 1
                    #if r == qqq:
                    #    corr += 1
                    #print(qqq- 536870918 + 3, corr, quecorr)

                #qqq += 1

            elif cmd == "mistake":
                print("error")
                break
            else:
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1103BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

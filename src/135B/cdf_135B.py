import math
from itertools import permutations


def dist_cube(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))


def in_triangle(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    #print(abs(A - (A1 + A2 + A3)))
    return abs(A - (A1 + A2 + A3)) < 0.000001


class CodeforcesTask135BSolution:
    def __init__(self):
        self.result = ''
        self.points = []

    def read_input(self):
        for x in range(8):
            self.points.append([int(y) for y in input().split(" ")])

    def process_task(self):
        sol = []
        for perm in permutations([x + 1 for x in range(8)]):
            sq = []
            for p in perm[:4]:
                sq.append(self.points[p - 1])
            rc = []
            for p in perm[4:]:
                rc.append(self.points[p - 1])
            sq_dists = [dist_cube(sq[0], sq[1]), dist_cube(sq[1], sq[2]), dist_cube(sq[2], sq[3]),
                        dist_cube(sq[3], sq[1]), dist_cube(sq[0], sq[2]), dist_cube(sq[0], sq[3])]
            rc_dists = [dist_cube(rc[0], rc[1]), dist_cube(rc[1], rc[2]), dist_cube(rc[2], rc[3]),
                        dist_cube(rc[3], rc[1]), dist_cube(rc[0], rc[2]), dist_cube(rc[0], rc[3])]
            sq_cnt = [sq_dists.count(x) for x in list(set(sq_dists))]
            sq_cnt.sort(reverse=True)
            rc_cnt = [rc_dists.count(x) for x in list(set(rc_dists))]
            rc_cnt.sort(reverse=True)
            if len(set(sq_dists)) == 2 and sq_cnt[0] == 4 and sq_cnt[1] == 2 and ((rc_cnt == [4, 2] and 2 == len(set(rc_dists))) or (len(set(rc_dists)) == 3 and rc_cnt == [2, 2, 2])):
                if len(set(rc_dists)) == 3 and rc_cnt == [2, 2, 2]:
                    do_ = False
                    for j in range(4):
                        rcc = rc[:j] + rc[j + 1:]
                        #print(rcc, rc[j], in_triangle(rcc[0][0], rcc[0][1], rcc[1][0], rcc[1][1], rcc[2][0], rcc[2][1], rc[j][0], rc[j][1]))
                        if in_triangle(rcc[0][0], rcc[0][1], rcc[1][0], rcc[1][1], rcc[2][0], rcc[2][1], rc[j][0], rc[j][1]):
                            do_ = True
                            break
                    if not do_:
                        sol = perm
                        break
                else:
                    sol = perm
                    break
        if sol:
            self.result = "YES\n{0}\n{1}".format(" ".join([str(x) for x in sol[:4]]), " ".join([str(x) for x in sol[4:]]))
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask135BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

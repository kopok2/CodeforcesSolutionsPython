def intersect(a, b, c, d):
    if c < a and d > b:
        return b - a
    elif c < a:
        return d - a
    else:
        if d > b:
            return b - c
        else:
            return d - c


class CodeforcesTask542ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.videos = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.videos.append([int(y) for y in input().split(" ")])

    def process_task(self):
        eff = [0 for x in range(self.n_m[0])]
        st = [0 for x in range(self.n_m[0])]
        for x in range(self.n_m[1]):
            channel = [int(y) for y in input().split(" ")]
            neff = [intersect(*v, *channel[:2])*channel[2] for v in self.videos]
            #eff = [max(eff[x], neff[x]) for x in range(self.n_m[0])]
            for y in range(self.n_m[0]):
                if neff[y] > eff[y]:
                    eff[y] = neff[y]
                    st[y] = x + 1

        max_eff = max(eff)
        max_vid = eff.index(max_eff) + 1
        max_st = st[max_vid - 1]
        if max_eff > 0:
            self.result = "{0}\n{1} {2}".format(max_eff, max_vid, max_st)
        else:
            self.result = "0"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask542ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

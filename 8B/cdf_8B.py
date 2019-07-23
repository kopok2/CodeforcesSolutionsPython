class CodeforcesTask8BSolution:
    def __init__(self):
        self.result = ''
        self.movements = ''

    def read_input(self):
        self.movements = input()

    def process_task(self):
        cmap = [[0 for x in range(203)] for y in range(203)]

        posx = 101
        posy = 101
        cmap[posy][posx] = 3
        if not cmap[posy][posx + 1]:
            cmap[posy][posx + 1] += 1
        if not cmap[posy][posx - 1]:
            cmap[posy][posx - 1] += 1
        if not cmap[posy + 1][posx]:
            cmap[posy + 1][posx] += 1
        if not cmap[posy - 1][posx]:
            cmap[posy - 1][posx] += 1
        valid = True
        for m in self.movements:
            if m == "U":
                posy -= 1
            elif m == "D":
                posy += 1
            elif m == "L":
                posx -= 1
            else:
                posx += 1
            for row in cmap[posy - 5:posy + 5]:
                print("".join([str(x) for x in row[posx - 5: posx + 5]]))
            print("\n")
            if cmap[posy][posx] > 1:
                valid = False
                break
            else:
                cmap[posy][posx] = 3
                #if not cmap[posy][posx + 1]:
                cmap[posy][posx + 1] += 1
                #if not cmap[posy][posx - 1]:
                cmap[posy][posx - 1] += 1
                #if not cmap[posy + 1][posx]:
                cmap[posy + 1][posx] += 1
                #if not cmap[posy - 1][posx]:
                cmap[posy - 1][posx] += 1
        #for r in cmap:
        #    print("".join([str(x) for x in r]))
        if valid:
            self.result = "OK"
        else:
            self.result = "BUG"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask8BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

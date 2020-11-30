class CodeforcesTask691BSolution:
    def __init__(self):
        self.result = ''
        self.word = ''

    def read_input(self):
        self.word = input()

    def process_task(self):
        symetric_chars = [("A", "A"), ("b", "d"), ("I", "I"), ("o", "o"), ("O", "O"), ("X", "X"), ("x", "x"),
                          ("T", "T"), ("Y", "Y"), ("p", "q"), ("W", "W"), ("w", "w"), ("V", "V"), ("v", "v"),
                          ("U", "U"), ("M", "M"), ("H", "H")]
        sc = list(set([x[0] for x in symetric_chars] + [x[1] for x in symetric_chars]))
        canbe = True
        for c in self.word:
            if c not in sc:
                canbe = False
                break
        #print(sc, canbe)
        if canbe:
            for x in range(len(self.word) // 2):
                c1 = self.word[x]
                c2 = self.word[-x - 1]
                #print(c1, c2)
                canbe = False
                for pair in symetric_chars:
                    if pair[0] == c1:
                        if pair[1] != c2:
                            canbe = False
                            break
                        else:
                            canbe = True
                            break
                    elif pair[0] == c2:
                        if pair[1] != c1:
                            canbe = False
                            break
                        else:
                            canbe = True
                            break
                if not canbe:
                    break
        if len(self.word) % 2:
            c = self.word[len(self.word) // 2]
            canbe = c in "AIoOXxTYWwVvUMH" and canbe
        self.result = "TAK" if canbe else "NIE"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask691BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

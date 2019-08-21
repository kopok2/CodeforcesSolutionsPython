class CodeforcesTask626BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.cards = []

    def read_input(self):
        self.n = int(input())
        self.cards = input()

    def process_task(self):
        cards_cnt = [self.cards.count(x) for x in "BGR"]
        to_consider = [cards_cnt]
        results = [0, 0, 0]
        considered = []
        while to_consider and sum(results) < 3:
            considering = to_consider.pop(-1)
            considered.append(considering)
            #print(to_consider, considering)
            if sum(considering) > 1:
                if considering[0] and considering[1]:
                    variant = considering[::]
                    variant[0] -= 1
                    variant[1] -= 1
                    variant[2] += 1
                    if variant not in considered:
                        to_consider.append(variant)
                if considering[0] and considering[2]:
                    variant = considering[::]
                    variant[0] -= 1
                    variant[2] -= 1
                    variant[1] += 1
                    if variant not in considered:
                        to_consider.append(variant)
                if considering[1] and considering[2]:
                    variant = considering[::]
                    variant[2] -= 1
                    variant[1] -= 1
                    variant[0] += 1
                    if variant not in considered:
                        to_consider.append(variant)
                if considering[0] > 1:
                    variant = considering[::]
                    variant[0] -= 1
                    if variant not in considered:
                        to_consider.append(variant)
                if considering[1] > 1:
                    variant = considering[::]
                    variant[1] -= 1
                    if variant not in considered:
                        to_consider.append(variant)
                if considering[2] > 1:
                    variant = considering[::]
                    variant[2] -= 1
                    if variant not in considered:
                        to_consider.append(variant)
            else:
                #print(considering)
                if considering[0]:
                    results[0] = 1
                elif considering[1]:
                    results[1] = 1
                else:
                    results[2] = 1
        if results[0]:
            self.result += "B"
        if results[1]:
            self.result += "G"
        if results[2]:
            self.result += "R"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask626BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

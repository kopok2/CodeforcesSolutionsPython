from operator import itemgetter


def dif_c(s):
    cs = set()
    i = 0
    for c in s:
        if not c in cs:
            cs.add(c)
            i += 1
    return i


class CodeforcesTask101ASolution:
    def __init__(self):
        self.result = ''
        self.word = ''
        self.k = 0

    def read_input(self):
        self.word = input()
        self.k = int(input())

    def process_task(self):
        chars = map(chr, range(97, 123))
        occurs = []
        for c in chars:
            occurs.append((c,self.word.count(c)))
        occurs = sorted(occurs, key=itemgetter(1))
        sums = []
        for x in range(len(occurs)):
            l_sum = 0
            letters = []
            i = x
            while l_sum < self.k:
                if l_sum + occurs[i][1] <= self.k:
                    if occurs[i][1]:
                        letters.append(occurs[i][0])
                    l_sum += occurs[i][1]
                i += 1
                if i == len(occurs):
                    break
            sums.append((letters, l_sum, len(letters)))
            #if l_sum == self.k:
            #    break
        sums = sorted(sums, key=itemgetter(2), reverse=True)
        #print(sums)
        #print(occurs)
        new_word = self.word
        for char in sums[0][0]:
            new_word = new_word.replace(char, "")
        self.result = "{0}\n{1}".format(dif_c(self.word) - sums[0][2], new_word)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask101ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

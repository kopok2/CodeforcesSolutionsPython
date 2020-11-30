class HashTable:
    def __init__(self):
        self.size = 0
        self.table = []

    def hash_function(self, key):
        return key % self.size

    def store(self, array):
        self.size = len(array)
        self.table = [[] for x in range(self.size)]
        for key in array:
            self.table[self.hash_function(key[0])].append(key)

    def get(self, key):
        chain = self.table[self.hash_function(key)]
        for x in chain:
            if x[0] == key:
                return x[1]


class CodeforcesTask254ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.cards = []

    def read_input(self):
        lines = open("input.txt", "r").readlines()
        self.n = int(lines[0])
        self.cards = [(int(x), i) for i, x in enumerate(lines[1].split(" "), 1)]

    def process_task(self):
        ht = HashTable()
        ht.store(self.cards)
        valid = True
        for b in ht.table:
            if len(b) % 2:
                valid = False
                break
        outfile = open("output.txt", "w")
        if valid:
            for b in ht.table:
                for x in range(len(b) // 2):
                    outfile.write("{0} {1}\n".format(b[x * 2][1], b[x * 2 + 1][1]))
        else:
            print("-1", file=outfile)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask254ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

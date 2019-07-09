def get_num_divisions(nodes, subnodes, more=True):
    divisions = []
    lel = nodes <= 1
    if nodes - 1 and more:
        for x in range(min(subnodes + 1, 2)):
            for y in get_num_divisions(nodes-1, subnodes-x, lel):
                divisions.append([x]+y)
    else:
        divisions.append([subnodes])
    for div in divisions:
        div.sort()
    import itertools
    divisions.sort()
    result = list(k for k, _ in itertools.groupby(divisions))
    print(nodes, subnodes, result, result[0])
    if more:
        return result[:2]
    else:
        return [result[0]]


def get_trees_structs(levels):
    trees = []
    for x in range(len(levels)-1):
        trees.append(get_num_divisions(levels[x], levels[x+1]))
    return trees


def get_trees_variants(structure):
    variants = []
    if structure:
        for var in structure[0]:
            others = get_trees_variants(structure[1:])
            if others:
                for other in others:
                    variants.append(var + other)
            else:
                variants.append(var)
    return variants[:2]


def get_tree_represantion(variant):
    result = "0 "
    i = 1
    for var in variant:
        for x in range(var):
            result += "{0} ".format(i)
        i += 1
    return result


class CodeforcesTask901ASolution:
    def __init__(self):
        self.result = ''
        self.height = 0
        self.levels = []

    def read_input(self):
        self.height = int(input())
        self.levels = [int(x) for x in input().split(" ")]

    def process_task(self):
        struct = get_trees_structs(self.levels)
        variants = get_trees_variants(struct)
        #for var in variants:
        #    print(var)
        if len(variants) == 1:
            self.result = "perfect"
        else:
            self.result += "ambiguous\n"
            self.result += "{0}\n".format(get_tree_represantion(variants[0]))
            self.result += "{0}\n".format(get_tree_represantion(variants[1]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    #print(get_num_divisions(120, 102))
    Solution = CodeforcesTask901ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

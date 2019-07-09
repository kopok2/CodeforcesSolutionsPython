class Lorry:
    def __init__(self, space):
        self.space = space
        self.load = []
        self.best_kayak = None

    def add_load(self, load_type, load_capacity):
        self.load.append((str(len(self.load) + 1), load_type, load_capacity))

    def merge_load(self):
        kayaks = [boat for boat in self.load if boat[1] == 1]
        kayaks = sorted(kayaks, key=lambda x: x[2], reverse=True)
        if self.space % 2:
            best = self.get_best_kayak()
            self.best_kayak = best
            kayaks.pop(0)
        merged = [(kayaks[x*2][0] + " " + kayaks[x*2 + 1][0], 2, kayaks[x*2][2] + kayaks[x*2 + 1][2])
                  for x in range(min(int(len(kayaks) / 2), int(self.space / 2)))]
        catamarans = [boat for boat in self.load if boat[1] == 2]
        self.load = sorted(merged + catamarans, key=lambda x: x[2], reverse=True)

    def get_best_kayak(self):
        best = 0
        result = ""
        for boat in self.load:
            if boat[1] == 1:
                if boat[2] > best:
                    best = boat[2]
                    result = boat
        return result

    def get_best_load(self):
        capacity = 0
        boats = ""
        self.merge_load()
        for x in range(int((self.space - (self.space % 2)) / 2)):
            capacity += self.load[x][2]
            boats += " " + self.load[x][0]
        if self.best_kayak:
            capacity += self.best_kayak[2]
            boats += " " + self.best_kayak[0]
        return capacity, boats


if __name__ == "__main__":
    try:
        port = input()
        boats_count = int(port.split(" ")[0])
        lorry_volume = int(port.split(" ")[1])
        lorry = Lorry(lorry_volume)
        for x in range(boats_count):
            boat = input()
            lorry.add_load(int(boat.split(" ")[0]), int(boat.split(" ")[1]))
        result = lorry.get_best_load()
        print(result[0])
        print(result[1])
    except Exception as e:
        print(e)

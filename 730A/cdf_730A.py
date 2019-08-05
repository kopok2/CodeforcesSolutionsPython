# coding=utf-8
"""Codeforces 730a solution."""

from operator import itemgetter


class CodeforcesTask730ASolution:
    def __init__(self):
        self.result = ''
        self.players = 0
        self.rating = []

    def read_input(self):
        self.players = int(input())
        self.rating = [int(x) for x in input().split(" ")]

    def process_task(self):

        if self.players > 2:
            moves = []
            players = [[x + 1, self.rating[x]] for x in range(self.players)]
            players.sort(key=itemgetter(1), reverse=True)
            while players[1][1] != players[-1][1]:
                players[0][1] = max(0, players[0][1] - 1)
                players[1][1] = max(0, players[1][1] - 1)
                moves.append([players[0][0], players[1][0]])
                players.sort(key=itemgetter(1), reverse=True)
            if players[0][1] != players[-1][1]:
                added = False
                for m in moves:
                    if not players[0][0] in m:
                        m.append(players[0][0])
                        players[0][1] = max(0, players[0][1] - 1)
                        added = True
                        break
                if not added:
                    #print("edge case 1")
                    #print(players)
                    moves.append([players[-1][0], players[0][0]])
                    players[0][1] = max(0, players[0][1] - 1)
                    players[-1][1] = max(0, players[-1][1] - 1)
                    players.sort(key=itemgetter(1), reverse=True)
                    while players[0][1] != players[-1][1] and players[1][1] != players[-1][1]:
                        #print(players)
                        players[0][1] = max(0, players[0][1] - 1)
                        players[1][1] = max(0, players[1][1] - 1)
                        moves.append([players[0][0], players[1][0]])
                        players.sort(key=itemgetter(1), reverse=True)
                    if players[0][1] != players[-1][1]:
                        added = False
                        for m in moves:
                            if not players[0][0] in m:
                                m.append(players[0][0])
                                players[0][1] = max(0, players[0][1] - 1)
                                added = True
                                break
                        if not added:
                            #print(players)
                            #print("edge case 2")
                            moves.append([players[-1][0], players[0][0]])
                            players[0][1] = max(0, players[0][1] - 1)
                            players[-1][1] = max(0, players[-1][1] - 1)
                            players.sort(key=itemgetter(1), reverse=True)
                            while players[0][1] != players[-1][1] and players[1][1] != players[-1][1]:
                                # print(players)
                                players[0][1] = max(0, players[0][1] - 1)
                                players[1][1] = max(0, players[1][1] - 1)
                                moves.append([players[0][0], players[1][0]])
                                players.sort(key=itemgetter(1), reverse=True)
                            if players[0][1] != players[-1][1]:
                                added = False
                                for m in moves:
                                    if not players[0][0] in m:
                                        m.append(players[0][0])
                                        players[0][1] = max(0, players[0][1] - 1)
                                        added = True
                                        break
                                if not added:
                                    # print(players)
                                    #print("edge case 3")
                                    moves.append([players[-1][0], players[0][0]])
                                    players[0][1] = max(0, players[0][1] - 1)
                                    players[-1][1] = max(0, players[-1][1] - 1)
                                    players.sort(key=itemgetter(1), reverse=True)
                                    while players[0][1] != players[-1][1] and players[1][1] != players[-1][1]:
                                        # print(players)
                                        players[0][1] = max(0, players[0][1] - 1)
                                        players[1][1] = max(0, players[1][1] - 1)
                                        moves.append([players[0][0], players[1][0]])
                                        players.sort(key=itemgetter(1), reverse=True)
                                    if players[0][1] != players[-1][1]:
                                        added = False
                                        for m in moves:
                                            if not players[0][0] in m:
                                                m.append(players[0][0])
                                                players[0][1] = max(0, players[0][1] - 1)
                                                added = True
                                                break
                                        if not added:
                                            # print(players)
                                            #print("edge case 4")
                                            moves.append([players[-1][0], players[0][0]])
                                            players[0][1] = max(0, players[0][1] - 1)
                                            players[-1][1] = max(0, players[-1][1] - 1)
                                            players.sort(key=itemgetter(1), reverse=True)
                                            while players[0][1] != players[-1][1] and players[1][1] != players[-1][1]:
                                                # print(players)
                                                players[0][1] = max(0, players[0][1] - 1)
                                                players[1][1] = max(0, players[1][1] - 1)
                                                moves.append([players[0][0], players[1][0]])
                                                players.sort(key=itemgetter(1), reverse=True)
                                            if players[0][1] != players[-1][1]:
                                                added = False
                                                for m in moves:
                                                    if not players[0][0] in m:
                                                        m.append(players[0][0])
                                                        players[0][1] = max(0, players[0][1] - 1)
                                                        added = True
                                                        break
                                                if not added:
                                                    # print(players)
                                                    print("edge case 5")


            players.sort(key=itemgetter(1), reverse=True)
            print(players[-1][1])
            print(len(moves))
            for m in moves:
                print("".join(["1" if x + 1 in m else "0" for x in range(self.players)]))
        else:
            if self.rating[0] == self.rating[1]:
                print(self.rating[0])
                print("0")
            else:
                print("0")
                print(max(self.rating))
                for x in range(max(self.rating)):
                    print("11")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask730ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())

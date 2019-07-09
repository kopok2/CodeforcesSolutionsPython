def add_score(scores, new, iteration):
    name = new.split(" ")[0]
    score = int(new.split(" ")[1])
    if name in board.keys():
        board[name].append((board[name][0][0], board[name][0][1]))
        board[name][0] = (board[name][0][0] + score, iteration)
    else:
        board[name] = [(score, iteration)]

    return scores


def get_first_highest_score(scores):
    highest = 0
    first_achieved = None
    winner = ''
    for player, score in scores.items():
        if score[0][0] > highest:
            highest = score[0][0]
            first_achieved = score[0][1]
            winner = player
    for player, score in scores.items():
        if score[0][0] == highest:
            for sub_score in score:
                if sub_score[0] >= highest:
                    if sub_score[1] < first_achieved:
                        first_achieved = sub_score[1]
                        winner = player
    return winner


if __name__ == "__main__":
    n = int(input())
    board = {}
    for x in range(n):
        board = add_score(board, input(), x)
    print(get_first_highest_score(board))

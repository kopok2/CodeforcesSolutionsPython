n = int(input())
words = [input() for x in range(n)]
for word in words:
    if len(word)<=10:
        print(word)
    else:
        print("{0}{1}{2}".format(word[0], len(word)-2, word[-1]))

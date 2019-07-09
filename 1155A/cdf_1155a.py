n = input()
import random
s = input()
def is_lex(s):
    result ="NO"
    for z in range(len(s)**2):
            try:
                y = random.randrange(len(s))
                x = random.randrange(len(s)-y)
                if s[:y]+s[y:y+x][::-1]+s[y+x:] < s:
                    result = "YES\n{0} {1}".format(y+1, y+x)
                    return result
            except:
                pass
    return result
print(is_lex(s))
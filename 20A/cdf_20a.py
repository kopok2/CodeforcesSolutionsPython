s = input()
print("/".join([""]+[x for x in s.split("/") if x]) if "/".join([""]+[x for x in s.split("/") if x]) else "/")
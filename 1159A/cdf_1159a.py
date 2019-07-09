n = int(input())

operations = input()
base = 0
state = 0
for operation in operations:
    if operation == "+":
        state += 1
    else:
        state -= 1
        if state < 0:
            base += 1
            state = 0
print(state)

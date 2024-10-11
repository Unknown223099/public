capacity = (12, 8, 5)
x = capacity[0]
y = capacity[1]
z = capacity[2]


memory = {}

ans = []

def get_all_states(state):
    a = state[0]
    b = state[1]
    c = state[2]

    if a == 6 and b == 6 and c == 0:
        ans.append(state)
        return True

    if (a, b, c) in memory:
        return False
    memory[(a, b, c)] = 1

    if a > 0 and b < y:
        if a <= y - b:
            if get_all_states((0, b + a, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                ans.append(state)
                return True

    if a > 0 and c < z:
        if a <= z - c:
            if get_all_states((0, b, c + a)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                ans.append(state)
                return True

    # Empty jug b into a
    if b > 0 and a < x:
        if b <= x - a:
            if get_all_states((a + b, 0, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                ans.append(state)
                return True

    if b > 0 and c < z:
        if b <= z - c:
            if get_all_states((a, 0, c + b)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                ans.append(state)
                return True

    if c > 0 and a < x:
        if c <= x - a:
            if get_all_states((a + c, b, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                ans.append(state)
                return True

    if c > 0 and b < y:
        if c <= y - b:
            if get_all_states((a, b + c, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                ans.append(state)
                return True

    return False

initial_state = (12, 0, 0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
    print(i)

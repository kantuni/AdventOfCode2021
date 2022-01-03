from collections import defaultdict

state = defaultdict(int)
fish = list(map(int, input().split(",")))

for f in fish:
    state[f] += 1


def next_generation(state):
    new_state = defaultdict(int)
    for key, value in state.items():
        if key == 0:
            new_state[6] += value
            new_state[8] += value
        else:
            new_state[key - 1] += value
    return new_state


days = 80
for _ in range(days):
    state = next_generation(state)

ans = sum(state.values())
print(ans)

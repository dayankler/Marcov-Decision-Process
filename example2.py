states = ["A", "B"]
rewards = {"A": 0, "B": 1}
gamma = 0.9

V = {"A": 0, "B": 0}

for _ in range(10):
    new_V = {}
    for s in states:
        if s == "A":
            new_V[s] = max(
                rewards["A"] + gamma * V["A"],
                rewards["B"] + gamma * V["B"]
            )
        else:
            new_V[s] = rewards["B"] + gamma * V["A"]
    V = new_V

print("Value Function:", V)

import random

states = ["A", "B"]
actions = ["left", "right"]

# Transition probabilities
transition = {
    ("A", "right"): ("B", 1),
    ("A", "left"): ("A", 0),
    ("B", "left"): ("A", 1),
    ("B", "right"): ("B", 0)
}

state = "A"

for _ in range(5):
    action = random.choice(actions)
    next_state, reward = transition[(state, action)]
    print(f"State: {state}, Action: {action}, Next: {next_state}, Reward: {reward}")
    state = next_state

# Value Iteration for Smart Traffic Signal Control

states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9

# Reward based on traffic density
reward = {"Low": 10, "Medium": 5, "High": -10}

# Transition model: (action → next state probabilities)
transitions = {
    "Low": {
        "Short": [(1.0, "Medium")],
        "Medium": [(1.0, "Low")],
        "Long": [(1.0, "Low")]
    },
    "Medium": {
        "Short": [(1.0, "High")],
        "Medium": [(1.0, "Medium")],
        "Long": [(1.0, "Low")]
    },
    "High": {
        "Short": [(1.0, "High")],
        "Medium": [(1.0, "Medium")],
        "Long": [(1.0, "Low")]
    }
}

# Initialize state values
V = {s: 0 for s in states}

# Value Iteration
for _ in range(20):
    new_V = V.copy()
    for s in states:
        action_values = []
        for a in actions:
            value = sum(
                p * (reward[next_state] + gamma * V[next_state])
                for p, next_state in transitions[s][a]
            )
            action_values.append(value)
        new_V[s] = max(action_values)
    V = new_V

print("Optimal State Values for Traffic Control:")
for state, value in V.items():
    print(f"{state}: {round(value, 2)}")
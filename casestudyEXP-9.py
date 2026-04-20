# Policy Iteration for Warehouse Robot

states = ["Idle", "Working"]
actions = ["Work", "Charge"]
gamma = 0.9

# Rewards for (state, action)
rewards = {
    ("Idle", "Work"): 5,
    ("Idle", "Charge"): 2,
    ("Working", "Work"): 6,
    ("Working", "Charge"): 1
}

# Transition model: (state, action) -> [(probability, next_state)]
transitions = {
    ("Idle", "Work"): [(1.0, "Working")],
    ("Idle", "Charge"): [(1.0, "Idle")],
    ("Working", "Work"): [(0.7, "Working"), (0.3, "Idle")],
    ("Working", "Charge"): [(1.0, "Idle")]
}

# Initialize policy and state values
policy = {s: "Work" for s in states}
V = {s: 0 for s in states}

# Policy Iteration
for _ in range(10):

    # --- Policy Evaluation ---
    for _ in range(20):  # iterate until approximate convergence
        new_V = V.copy()
        for s in states:
            a = policy[s]
            new_V[s] = sum(
                p * (rewards[(s, a)] + gamma * V[next_state])
                for p, next_state in transitions[(s, a)]
            )
        V = new_V

    # --- Policy Improvement ---
    policy_stable = True
    for s in states:
        old_action = policy[s]

        # Choose best action
        action_values = {}
        for a in actions:
            action_values[a] = sum(
                p * (rewards[(s, a)] + gamma * V[next_state])
                for p, next_state in transitions[(s, a)]
            )

        policy[s] = max(action_values, key=action_values.get)

        if old_action != policy[s]:
            policy_stable = False

    if policy_stable:
        break

# Output
print("Optimal Policy:")
for s in states:
    print(f"{s} -> {policy[s]}")

print("\nState Values:")
for s in states:
    print(f"{s}: {round(V[s], 2)}")
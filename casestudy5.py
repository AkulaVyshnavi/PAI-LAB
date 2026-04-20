
def minimax(depth, is_defender):
    if depth == 0:
        return 0  # Neutral score at leaf

    if is_defender:
        # Defender tries to maximize score
        return max(
            minimax(depth - 1, False),
            minimax(depth - 1, False)
        )
    else:
        # Attacker tries to minimize score
        return min(
            minimax(depth - 1, True),
            minimax(depth - 1, True)
        )

score = minimax(3, True)
print("Optimal Security Outcome Score:", score)
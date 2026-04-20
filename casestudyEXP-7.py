from hmmlearn import hmm
import numpy as np

# 3 hidden states: Interested, Neutral, Disengaged
model = hmm.MultinomialHMM(
    n_components=3,
    n_iter=100,
    random_state=42
)

# Define model parameters
model.startprob_ = np.array([0.5, 0.3, 0.2])

model.transmat_ = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

# 2 observable symbols: 0 = click, 1 = no-click
model.n_features = 2

model.emissionprob_ = np.array([
    [0.7, 0.3],  # Interested
    [0.4, 0.6],  # Neutral
    [0.2, 0.8]   # Disengaged
])

# Observed sequence (must be 2D array)
observations = np.array([0, 1, 1, 0]).reshape(-1, 1)

# Predict hidden states
hidden_states = model.predict(observations)

print("Predicted Hidden Engagement States:", hidden_states)
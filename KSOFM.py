import numpy as np
data = np.array([
    [0.1, 0.8],
    [0.2, 0.9],
    [0.9, 0.2],
    [0.8, 0.1],
])

# SOM parameters
num_neurons = 2                 # number of output neurons (clusters)
learning_rate = 0.5
num_epochs = 10

weights = np.random.rand(num_neurons,data.shape[1])

print("Initial Weights:\n", weights)

for epoch in range(num_epochs):
    print(f"\nEpoch {epoch+1}")
    for x in data:
        # Compute Euclidean distance
        distances = np.linalg.norm(x - weights, axis=1)

        # Winner neuron
        winner = np.argmin(distances)

        # Update weights
        weights[winner] = weights[winner] + learning_rate * (x - weights[winner])

        print(f"Input: {x}, Winner: {winner}, Updated Weights: {weights}")


print("\nFinal Weights (after training):\n", weights)
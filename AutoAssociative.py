import numpy as np

X = np.array([
    [ 1,  1, -1, -1],
    [-1,  1, -1,  1]
])

def bsign(v):
    return np.where(v >= 0, 1, -1)

W = np.zeros((X.shape[1],X.shape[1]))

for x in X:
    W += np.outer(x,x)

print("Weight Matrix:\n", W)

def recall(x, steps=1):
    for _ in range(steps):
        x = bsign(x @ W)
    return x

test = np.array([1, -1, -1, -1])  
output = recall(test,steps=1)

print("\nInput :", test)
print("Output:", output)
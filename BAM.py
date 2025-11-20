import numpy as np

def bsign(v):
    return np.where(v>=0,1,-1)

X = np.array([
    [1, 1, -1],
    [-1, 1, 1]
])

Y = np.array([
    [1, -1],
    [-1, 1]
])

W = sum(np.outer(x, y) for x, y in zip(X, Y))
print("Weight Matrix:\n", W)

def recall_x_to_y(x):
    return bsign(x @ W)

def recall_y_to_x(y):
    return bsign(y @ W.T)

x_test = np.array([1, 1, -1])
print("\nGiven X → Y:", recall_x_to_y(x_test))

y_test = np.array([-1, 1])
print("Given Y → X:", recall_y_to_x(y_test))
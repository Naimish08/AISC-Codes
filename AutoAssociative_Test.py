import numpy as np

def bsign(v):
    return np.where(v>=0,1,-1)

X = np.array([
    [1,1,-1,-1],
    [1,1,1,1]
])

W = np.zeros((X.shape[1],X.shape[1]))

for x in X:
    W += np.outer(x,x)

print("Weights ",W)

test = [1,1,1,1]

def compute(test):
    return bsign(test @ W)

print(compute(test))


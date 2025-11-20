import numpy as np

def bsign(v):
    return np.where(v>=0,1,-1)

X = np.array([
    [1,1,1,1,-1,-1],
    [1,1,1,1,1,1]
])

Y = np.array([
    [-1,1],
    [1,1]
])

W = sum(np.outer(x,y) for x,y in zip(X,Y))

test = np.array([1,1,1,1,1,1])
def x_to_y(test):
    return bsign(test @ W)

def y_to_x(test2):
    return bsign(test2 @ W.T)

test2 = [1,1]
print("X_to_Y ",x_to_y(test))
print("Y_to_X ",y_to_x(test2))
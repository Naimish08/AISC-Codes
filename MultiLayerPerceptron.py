import numpy as np
import matplotlib.pyplot as plt

# Define the model
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def binary_sigmoid(self, x):
        return np.where(x >= 0, 1, 0)
    
    def forward(self, x):
        self.layer1 = self.binary_sigmoid(self.weights1.dot(x) + self.bias1)
        self.layer2 = self.sigmoid(self.weights2.dot(self.layer1) + self.bias2)
        return self.layer2
    
    def cost(self, y, y_pred):
        return -(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
    
    def backward(self, x, y, learning_rate=0.01):
        layer2_delta = self.layer2 - y
        layer2_grad = self.sigmoid(self.weights2.dot(self.layer1) + self.bias2)
        self.weights2 += layer2_delta.dot(self.layer1.T) * layer2_grad * (1 - layer2_grad) * learning_rate
        self.bias2 += layer2_delta * layer2_grad * (1 - layer2_grad) * learning_rate
        layer1_delta = self.weights2.T.dot(layer2_delta) * self.binary_sigmoid(self.weights1.dot(x) + self.bias1) * (1 - self.binary_sigmoid(self.weights1.dot(x) + self.bias1))
        self.weights1 += layer1_delta.dot(x.T) * learning_rate
        self.bias1 += layer1_delta * learning_rate

# Train the model
def train(model, X, y, epochs=100):
    for i in range(epochs):
        for j, x in enumerate(X):
            y_pred = model.forward(x)
            cost = model.cost(y[j], y_pred)
            model.backward(x, y[j])
        print(f'Epoch {i+1}: Cost = {cost:.4f}')

# Test the model
def test(model, X, y):
    y_pred = [np.argmax(model.forward(x)) for x in X]
    correct = sum([int(y_pred[i] == y[i]) for i in range(len(y_pred))])
    print(f'Accuracy: {correct/len(y_pred)*100:.2f}%')

# Example usage
input_size = 4
hidden_size = 2
output_size = 3
model = NeuralNetwork(input_size, hidden_size, output_size)
X = np.random.randn(10, input_size)
y = np.random.randint(0, output_size, (10,))
train(model, X, y, epochs=100)
test(model, X, y)
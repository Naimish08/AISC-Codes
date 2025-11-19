import numpy as np

class Perceptron:
    def __init__(self,input_size,learning_rate=0.1,epochs=100):
        self.weights = np.zeros(input_size+1) # +1 for bias
        self.lr = learning_rate
        self.epochs = epochs
    
    def activation_function(self,x):
        return 1 if x>=0 else 0
    
    def predict(self,x):
        z = self.weights[0]+np.dot(x,self.weights[1:])
        return self.activation_function(z)
    
    def train(self,input,labels):
        print(f"Training started...")
        for epoch in range(self.epochs):
            global_error = 0
            for x,label in zip(input,labels):
                predcition = self.predict(x)
                error = label - predcition
                
                
                self.weights[0] += self.lr*error
                self.weights[1:] += self.lr*error*x
                
                global_error += abs(error)
                if(global_error == 0):
                    print(f"Converged at epoch {epoch} ")
                    break;
                    
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y_and = np.array([0,0,0,1])
y_or = np.array([0,1,1,1])
y_xor = np.array([0,1,1,0])

# --- Execution ---

# 1. Train AND Gate
print("--- Learning AND Gate ---")
p_and = Perceptron(input_size=2)
p_and.train(X, y_and)
print(f"Learned Weights: {p_and.weights[1:]}, Bias: {p_and.weights[0]}")
print("Testing AND Gate:")
for x in X:
    print(f"{x} -> {p_and.predict(x)}")

print("\n" + "="*30 + "\n")

# 2. Train OR Gate (Used for Carry-out in Full Adder)
print("--- Learning OR Gate ---")
p_or = Perceptron(input_size=2)
p_or.train(X, y_or)
print(f"Learned Weights: {p_or.weights[1:]}, Bias: {p_or.weights[0]}")
print("Testing OR Gate:")
for x in X:
    print(f"{x} -> {p_or.predict(x)}")

print("\n" + "="*30 + "\n")

# 3. Attempting XOR Gate (The 'Sum' logic for Adders)
print("--- Attempting to Learn XOR Gate (Half Adder Sum) ---")
p_xor = Perceptron(input_size=2, epochs=50) # Limit epochs so it doesn't run forever
p_xor.train(X, y_xor)
print(f"Learned Weights: {p_xor.weights[1:]}, Bias: {p_xor.weights[0]}")
print("Testing XOR Gate (Expect Failure):")
for i, x in enumerate(X):
    pred = p_xor.predict(x)
    actual = y_xor[i]
    status = "CORRECT" if pred == actual else "WRONG"
    print(f"{x} -> Predicted: {pred} | Actual: {actual} [{status}]")
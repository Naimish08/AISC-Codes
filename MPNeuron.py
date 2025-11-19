class MPNeuron:
  def __init__(self,weights,threshold):
    self.weights = weights
    self.threshold = threshold

  def evaluate(self,inputs):
    weighted_sum = sum(x*w for x,w in zip(inputs,self.weights))

    if weighted_sum >= self.threshold:
      return 1
    else:
      return 0

def AND_gate(x1,x2):
  neuron = MPNeuron(weights=[1,1], threshold=2)
  return neuron.evaluate([x1,x2])

def OR_gate(x1,x2):
  neuron = MPNeuron(weights=[1,1], threshold=1)
  return neuron.evaluate([x1,x2])

def XOR_gate(x1,x2):
  neuron1 = MPNeuron(weights=[1,-1], threshold=1).evaluate([x1,x2])
  neuron2 = MPNeuron(weights=[-1,1], threshold=1).evaluate([x1,x2])

  return OR_gate(neuron1,neuron2)

def half_adder(x1,x2):
  sum_bit = XOR_gate(x1,x2)
  carry_bit = AND_gate(x1,x2)

  return sum_bit,carry_bit

def full_adder(x1,x2,c_in):
  sum1,carry1 = half_adder(x1,x2)

  final_sum, carry2 = half_adder(sum1, c_in)

  final_carry = OR_gate(carry1,carry2)

  return final_sum, final_carry

if __name__ == "__main__":
    print("--- 1. AND Gate Truth Table ---")
    print("A | B | Output")
    print("-" * 14)
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} | {b} |   {AND_gate(a, b)}")

    print("\n--- 2. Half Adder Truth Table ---")
    print("A | B | Sum | Carry")
    print("-" * 21)
    for a in [0, 1]:
        for b in [0, 1]:
            s, c = half_adder(a, b)
            print(f"{a} | {b} |  {s}  |   {c}")

    print("\n--- 3. Full Adder Truth Table ---")
    print("A | B | Cin | Sum | Cout")
    print("-" * 26)
    inputs = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), 
              (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
    
    for a, b, cin in inputs:
        s, cout = full_adder(a, b, cin)
        print(f"{a} | {b} |  {cin}  |  {s}  |   {cout}")
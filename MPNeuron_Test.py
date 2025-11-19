class MPNeuron:
    def __init__(self,weights,threshold):
        self.weights = weights
        self.threshold = threshold

    def compute(self,input):
        weighted_sum = sum(x*w for x,w in zip(input,self.weights))

        if weighted_sum>=self.threshold:
            return 1
        else:
            return 0

def AND(a,b):
    neuron = MPNeuron(weights=[1,1],threshold=2)
    return neuron.compute([a,b])

def OR(a,b):
    neuron = MPNeuron(weights=[1,1],threshold=1)
    return neuron.compute(input=[a,b])

def XOR(a,b):
    neuron1 = MPNeuron(weights=[1,-1],threshold=1).compute([a,b])
    neuron2 = MPNeuron(weights=[-1,1],threshold=1).compute([a,b])
    return OR(neuron1,neuron2)

def half_adder(a,b):
    finalsum = XOR(a,b)
    carry = AND(a,b)
    return finalsum,carry

def full_adder(a,b,c_in):
    sum1,carry1 = half_adder(a,b)
    finalsum,carry2 = half_adder(sum1,c_in)

    finalcarry = OR(carry1,carry2)

    return finalsum,finalcarry

if __name__ == '__main__':
    print("--AND TABLE--")
    print("a | b | Y")
    for a in [0,1]:
        for b in [0,1]:
            print(f"{a} | {b} | {AND(a,b)}")
    

    print("--OR TABLE--")
    print("a | b | Y")
    for a in [0,1]:
        for b in [0,1]:
            print(f"{a} | {b} | {OR(a,b)}")

    print("--Half-Adder TABLE--")
    print("a | b | Sum | Carry")
    for a in [0,1]:
        for b in [0,1]:
            s,c = half_adder(a,b)
            print(f"{a} | {b} | {s}   | {c}")
    
    print("--Full-Adder TABLE--")
    print("a | b | c_in | Sum | Carry")
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                s,c = full_adder(a,b,c)
                print(f"{a} | {b} | {c}    | {s}   | {c}")


        
# Triangular membership function
def trimf(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    return 1

# Fuzzification
def dirt_membership(x):
    return {
        "low": trimf(x, 0, 0, 5),
        "medium": trimf(x, 0, 5, 10),
        "high": trimf(x, 5, 10, 10)
    }

def load_membership(x):
    return {
        "small": trimf(x, 0, 0, 5),
        "medium": trimf(x, 0, 5, 10),
        "large": trimf(x, 5, 10, 10)
    }

# Crisp Output Values
output_values = {
    "short": 15,
    "medium": 35,
    "long": 55
}

# ------------------------------
# RULES (IF–THEN)
# ------------------------------
def apply_rules(dirt_fz, load_fz):
    rules = []

    # IF dirt is low AND load is small THEN wash = short
    rules.append((min(dirt_fz["low"], load_fz["small"]), "short"))

    # IF dirt is medium AND load is medium THEN wash = medium
    rules.append((min(dirt_fz["medium"], load_fz["medium"]), "medium"))

    # IF dirt is high AND load is large THEN wash = long
    rules.append((min(dirt_fz["high"], load_fz["large"]), "long"))

    # IF dirt is high AND load is small THEN wash = medium
    rules.append((min(dirt_fz["high"], load_fz["small"]), "medium"))

    # IF dirt is low AND load is large THEN wash = medium
    rules.append((min(dirt_fz["low"], load_fz["large"]), "medium"))

    return rules


# Defuzzification (Weighted Average)
def defuzzify(rules):
    num = denom = 0
    for strength, label in rules:
        num += strength * output_values[label]
        denom += strength
    return num / denom if denom != 0 else 0


# Wrapper function
def washing_machine_fuzzy(dirt_val, load_val):
    dirt_fz = dirt_membership(dirt_val)
    load_fz = load_membership(load_val)
    rules = apply_rules(dirt_fz, load_fz)
    return defuzzify(rules)


dirt = 8   # High dirt
load = 6   # Medium load

print("Recommended Wash Time:", washing_machine_fuzzy(dirt, load), "minutes")

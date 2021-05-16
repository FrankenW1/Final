from collections import defaultdict


print("WITHOUT DEFAULTDICT:")
Dict = {1: 'Alex', 2: 'Carlos', 3: 'James'}
print("Dictionary:")
print(Dict)
print(Dict[1])
print(Dict[4])

# USING DEFAULT DICT TO RETURN NO VALUE
def def_value():
    return "Not Present"

# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["f"])


from collections import defaultdict


print("WITHOUT DEFAULTDICT:")
Dict = {1: 'Alex', 2: 'Carlos', 3: 'James'}
print("Dictionary:")
print(Dict)
print(Dict[1])
# print(Dict[4])

# USING DEFAULT DICT TO RETURN NO VALUE
def def_value():
    return "Not Present"

d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["f"])

# USING DEFAULTDICT TO CAST A LIST TO A DICTIONARY WITH IDS
print("SEPERATE")
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:
    d[i] += 1

print(d)
print(d[9])
print(d)

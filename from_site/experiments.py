import copy
memo = {}
x = range(5)
y = copy.deepcopy(x, memo)
print(memo)
print(id(x))
print(id(y))
z = [x, x]
t = copy.deepcopy(z, memo)
print (id(t[0]), id(t[1]), id(y))
print("lala")

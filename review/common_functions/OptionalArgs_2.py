# A demo of optional function arguments (2)

def area(x, y=None):
    if y is None:
        return x * x
    else:
        return x * y


print(area(15))
print(area(2, 18))


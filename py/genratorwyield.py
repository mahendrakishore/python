
def genrate():
    yield 1
    yield 2
    yield 3

for val in genrate():
    print(val)
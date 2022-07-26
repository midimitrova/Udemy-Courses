
# Create a generator that generates the squares of numbers up to some number N.

def gen_sequence(n):
    for num in range(n):
        yield num ** 2
for i in gen_sequence(10):
    print(i)
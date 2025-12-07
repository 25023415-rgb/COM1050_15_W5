a, b = map(int, input().split())
def hamming(a, b):
    sosanhbit = a ^ b
    return bin(sosanhbit).count('1')
print(hamming(a, b))
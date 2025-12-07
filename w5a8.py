n = int(input())
def tongchuso(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
print(tongchuso(n))
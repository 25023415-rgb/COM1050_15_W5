n = int(input())
def tongchuso(n):
    tong = 0
    if n > 0:
        while n > 0:
            t = n % 10
            tong += t
            n = n // 10
        return tong
    else:
        print("n phải là số nguyên dương")
print(tongchuso(n))
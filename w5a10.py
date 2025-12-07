a = input()
b = input()
def anhxa(a, b):
    pattern1 = []
    pattern2 = []
    for char in a:
        vitri = a.index(char)
        pattern1.append(vitri)
    for char in b:
        vitri = b.index(char)
        pattern2.append(vitri)
    if pattern1 == pattern2:
        return True
    return False
print(anhxa(a, b))

a, b = map(input().split())
def anhxa(a, b):
    a_to_b = {}
    b_to_a = {}
    for char_a, char_b in zip(a, b):
        if char_a in a_to_b:
            if a_to_b[char_a] != char_b:
                return False
        else:
            a_to_b[char_a] = char_b
        if char_b in b_to_a:
            if b_to_a[char_b] != char_a:
                return False
        else:
            b_to_a[char_b] = char_a
    return True
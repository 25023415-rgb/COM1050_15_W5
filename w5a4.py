lst = list(map(int, input().split()))
k = int(input())
def timvitri(lst, k):
    for index, value in enumerate(lst):
        if value == k:
            return index
    return -1
print(timvitri(lst, k))
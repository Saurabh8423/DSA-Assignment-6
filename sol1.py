def findPermutation(s):
    n = len(s)
    perm = []
    current = 1

    for c in s:
        if c == 'I':
            perm.append(current)
            current += 1
        elif c == 'D':
            perm.append(n)
            n -= 1

    perm.append(current)
    return perm
s = "IDID"
print(findPermutation(s))

def isPossibleDP(OR, SUM, CARRY = 0):

    if len(SUM) == 0 and len(OR) != 0:
        return False

    if len(OR) == 0:
        if len(SUM) == 0 and CARRY == 0:
            return True
        elif len(SUM) == 1 and CARRY == 1:
            return True
        else:
            return False

    # a = 0, b = 0, c = 0
    if OR[-1] == 0 and SUM[-1] == 0 and CARRY == 0:
        res = isPossibleDP(OR[:-1], SUM[:-1], 0)

    # a = 0, b = 0, c = 1
    elif OR[-1] == 0 and SUM[-1] == 1 and CARRY == 1:
        res = isPossibleDP(OR[:-1], SUM[:-1], 0)

    # a = 1, b = 1, c = 0
    elif OR[-1] == 1 and SUM[-1] == 0 and CARRY == 0:
        res = isPossibleDP(OR[:-1], SUM[:-1], 1)

    # a = 1, b = 0, c = 1
    elif OR[-1] == 1 and SUM[-1] == 0 and CARRY == 1:
        res = isPossibleDP(OR[:-1], SUM[:-1], 1)

    # a = 1, b = 0, c = 0
    elif OR[-1] == 1 and SUM[-1] == 1 and CARRY == 0:
        res = isPossibleDP(OR[:-1], SUM[:-1], 0)

    # a = 1, b = 1, c = 1
    elif OR[-1] == 1 and SUM[-1] == 1 and CARRY == 1:
        res = isPossibleDP(OR[:-1], SUM[:-1], 1)

    else:
        return False

    return res


from math import log
def log2(x):
    return log(x, 2)

def to_bits(num):
    if num == 0:
        return [0]

    N = int(log2(num)) + 1
    bits = [0] * N
    for i in range(N):
        bits[N - i - 1] = (num >> i) % 2

    return bits

class OrAndSumEasy:
    def isPossible(self, pairOr, pairSum):
        OR = to_bits(pairOr)
        SUM = to_bits(pairSum)


        res = isPossibleDP(OR, SUM)

        return res


oas = OrAndSumEasy()

print(oas.isPossible(999799115789631487, 999999999999999999))
print(oas.isPossible(3, 5))
print(oas.isPossible(7, 11))        # Yes
print(oas.isPossible(11, 7))        # No
print(oas.isPossible(1, 100))
print(oas.isPossible(0, 0))
print(oas.isPossible(1, 2))


'''
0)
7
11
Returns: "Possible"
One of the solution is: A = 5 and B = 6.
1)
11
7
Returns: "Impossible"
We can show the sum should be at least as large as or, so it is impossible.
2)
999799115789631487
999999999999999999
Returns: "Possible"
One of the solution is a = 111111111111111111, b = 888888888888888888.
3)
1
100
Returns: "Impossible"
4)
0
0
Returns: "Possible"
'''
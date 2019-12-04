start = 138241
end = 674034


def valid(number):
    snumber = str(number)
    twice = False
    for a, b in zip(snumber[:-1], snumber[1:]):
        if a == b:
            twice = True
        if b < a:
            return False
    return twice


print(valid(111111))  # meets these criteria (double 11, never decreases)
# does not meet these criteria (decreasing pair of digits 50).
print(valid(223450))
# print(valid(123455))
print(valid(123789))  # does not meet these criteria (no double).


count = 0
for i in range(start, end+1):
    if valid(i):
        count += 1

print("Count ", count)


def valid2(number):
    snumber = "*"+str(number)+"XX"
    twice = False
    for i, digit in enumerate(snumber[1:-2]):
        index = i+1
        if (digit == snumber[index+1] and digit != snumber[index-1]
                and snumber[index+1] != snumber[index+2]):
            twice = True
        if snumber[index+1] < digit:
            return False
    return twice


print(valid2(112233))
print(valid2(123444))
print(valid2(111122))


count = 0
for i in range(start, end+1):
    if valid2(i):
        count += 1

print("Count ", count)

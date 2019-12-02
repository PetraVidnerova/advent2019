sum = 0
with open("input.txt") as f:
    for line in f:
        mass = int(line)
        sum += (mass // 3) - 2

print(sum)


# second part
def fuel(mass):
    return (mass // 3) - 2


def rec_fuel(mass):
    sum = 0
    while True:
        mass = fuel(mass)
        if mass > 0:
            sum += mass
        else:
            return sum


# print(rec_fuel(14))
# print(rec_fuel(1969))
# print(rec_fuel(100756))

sum = 0
with open("input.txt") as f:
    for line in f:
        mass = int(line)
        sum += rec_fuel(mass)
print(sum)

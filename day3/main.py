input1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
input2 = "U62,R66,U55,R34,D71,R55,D58,R83"

input1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
input2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"


with open("input.txt") as f:
    input1 = f.readline()
    input2 = f.readline()

w1_instr = input1.split(",")
w2_instr = input2.split(",")


def create_line(x, y, time, direction, number):

    if direction == "R":
        return {(x+i, y): time+i for i in range(number+1)}, (x+number, y)
    elif direction == "L":
        return {(x-i, y): time+i for i in range(number+1)}, (x-number, y)
    elif direction == "U":
        return {(x, y-i): time+i for i in range(number+1)}, (x, y-number)
    elif direction == "D":
        return {(x, y+i): time+i for i in range(number+1)}, (x, y+number)
    else:
        raise ValueError()


def create_wire(instr):
    wire = dict()
    x, y = 0, 0
    time = 0
    for couple in instr:
        direction, number = couple[0], int(couple[1:])
        line, point = create_line(x, y, time, direction, number)
        for key, value in line.items():
            if key not in wire:
                wire[key] = value
        x, y = point
        time += number
    return wire


w1 = create_wire(w1_instr)
w2 = create_wire(w2_instr)
intersection = set(w1.keys()) & set(w2.keys())     # prunik kabelu
intersection -= {(0, 0)}   # odebrat origin


dists = []
for point in intersection:
    dists.append(abs(point[0])+abs(point[1]))

print(min(dists))

time_dists = [w1[point] + w2[point] for point in intersection]
print(min(time_dists))

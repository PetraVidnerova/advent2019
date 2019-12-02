from itertools import product

# string_input = "1,9,10,3,2,3,11,0,99,30,40,50"
# string_input = "1,1,1,4,99,5,6,0,99"

with open("input.txt") as f:
    string_input = f.read()

program_code = [int(x) for x in string_input.split(",")]


def run_program(program, noun, verb):
    mem = program.copy()
    mem[1] = noun
    mem[2] = verb

    cursor = 0
    while True:
        op = mem[cursor]
        if op not in (1, 2, 99):
            raise ValueError()

        if op == 99:
            break

        a = mem[mem[cursor+1]]
        b = mem[mem[cursor+2]]
        result_index = mem[cursor+3]

        if op == 1:
            mem[result_index] = a + b
        else:
            mem[result_index] = a * b

        cursor += 4

    return mem[0]


# part 1
print(run_program(program_code, 12, 2))

# part 2
for noun, verb in product(range(100), repeat=2):
    if run_program(program_code, noun, verb) == 19690720:
        break


print(100*noun + verb)

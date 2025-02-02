def solve(heads, legs):
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if (chickens*2 + rabbits*4) == legs:
            return chickens, rabbits
    return "this task cannot be solved"

heads = int(input("Heads: "))
legs = int(input("Legs: "))

print(solve(heads, legs))
from simpleai.search import CspProblem, backtrack


def constraint_func(variables, values):
    return values[0] != values[1]


if __name__ == '__main__':

    regions = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')

    colors = {region: ['red', 'green', 'blue'] for region in regions}

    constraints = [
        (('WA', 'NT'), constraint_func),
        (('WA', 'SA'), constraint_func),
        (('NT', 'SA'), constraint_func),
        (('NT', 'Q'), constraint_func),
        (('SA', 'Q'), constraint_func),
        (('SA', 'NSW'), constraint_func),
        (('SA', 'V'), constraint_func),
        (('Q', 'NSW'), constraint_func),
        (('NSW', 'V'), constraint_func),
    ]

    problem = CspProblem(regions, colors, constraints)
    output = backtrack(problem)

    print("\nAustralia Map Coloring:\n")
    for region, color in output.items():
        print(region, "==>", color)

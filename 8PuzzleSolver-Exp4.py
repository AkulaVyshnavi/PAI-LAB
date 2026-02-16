from simpleai.search import astar, SearchProblem
def list_to_string(input_list):
    return '\n'.join(['-'.join(x) for x in input_list])


def string_to_list(input_string):
    return [x.split('-') for x in input_string.split('\n')]


def get_location(rows, element):
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            if item == element:
                return i, j


# ---------- Puzzle Solver Class ----------

class PuzzleSolver(SearchProblem):

    def actions(self, state):
        rows = string_to_list(state)
        row_e, col_e = get_location(rows, 'e')

        actions = []

        if row_e > 0:
            actions.append(rows[row_e - 1][col_e])
        if row_e < 2:
            actions.append(rows[row_e + 1][col_e])
        if col_e > 0:
            actions.append(rows[row_e][col_e - 1])
        if col_e < 2:
            actions.append(rows[row_e][col_e + 1])

        return actions

    def result(self, state, action):
        rows = string_to_list(state)
        row_e, col_e = get_location(rows, 'e')
        row_n, col_n = get_location(rows, action)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]
        return list_to_string(rows)

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        rows = string_to_list(state)
        distance = 0

        for num in '12345678e':
            r, c = get_location(rows, num)
            rg, cg = goal_positions[num]
            distance += abs(r - rg) + abs(c - cg)

        return distance



GOAL = '''1-2-3
4-5-6
7-8-e'''

INITIAL = '''1-e-2
6-3-4
7-5-8'''

# Precompute goal positions
goal_positions = {}
rows_goal = string_to_list(GOAL)
for num in '12345678e':
    goal_positions[num] = get_location(rows_goal, num)



result = astar(PuzzleSolver(INITIAL))

for i, (action, state) in enumerate(result.path()):
    print()

    if action is None:
        print("Initial configuration")
    elif i == len(result.path()) - 1:
        print(f"Move {action} into empty space. Goal achieved!")
    else:
        print(f"Move {action} into empty space")

    print(state)

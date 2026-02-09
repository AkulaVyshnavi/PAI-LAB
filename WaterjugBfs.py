from collections import deque

def Solution(a, b, target):
    visited = set()
    q = deque()

   
    q.append(((0, 0), [(0, 0)]))

    while q:
        (x, y), path = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

       
        if x == target or y == target:
            print("Path from initial state to solution state ::")
            for state in path:
                print(state)
            return

       
        next_states = [
            (a, y),          
            (x, b),          
            (0, y),         
            (x, 0),         
        ]

        pour = min(x, b - y)
        next_states.append((x - pour, y + pour))


        pour = min(y, a - x)
        next_states.append((x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                q.append((state, path + [state]))

    print("Solution not possible")


if __name__ == "__main__":
    Jug1 = int(input("Enter the capacity of Jug1: "))
    Jug2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target: "))
    Solution(Jug1, Jug2, target)


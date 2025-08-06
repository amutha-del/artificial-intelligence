from collections import deque

# Define the goal state
goal_state = '123456780'  # 0 represents the blank

# Moves: Up, Down, Left, Right (index shifts)
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])  # state, path

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        if current_state in visited:
            continue
        visited.add(current_state)

        zero_index = current_state.index('0')
        for move in moves[zero_index]:
            new_state = list(current_state)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state_str = ''.join(new_state)

            if new_state_str not in visited:
                queue.append((new_state_str, path + [current_state]))

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(' '.join(state[i:i+3]))
    print()

# Example usage
start_state = '123405786'  # You can change this as needed
solution = bfs(start_state)

if solution:
    print("Steps to solve the 8 Puzzle:\n")
    for step in solution:
        print_board(step)
else:
    print("No solution found.")

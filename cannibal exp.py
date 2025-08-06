def is_safe(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True

def missionaries_and_cannibals():
    # Initial state: 3 missionaries, 3 cannibals on the left, boat on left (1)
    start = (3, 3, 1)
    # Goal state: all on right side, boat on right (0)
    goal = (0, 0, 0)
    visited = []
    queue = [(start, [])]

    # All possible boat moves (missionaries, cannibals)
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

    while queue:
        (m_left, c_left, boat), path = queue.pop(0)
        if (m_left, c_left, boat) == goal:
            path.append((m_left, c_left, boat))
            return path

        if (m_left, c_left, boat) in visited:
            continue
        visited.append((m_left, c_left, boat))

        for m, c in moves:
            if boat == 1:
                new_state = (m_left - m, c_left - c, 0)
            else:
                new_state = (m_left + m, c_left + c, 1)

            m_right = 3 - new_state[0]
            c_right = 3 - new_state[1]

            if is_safe(new_state[0], new_state[1], m_right, c_right):
                queue.append((new_state, path + [(m_left, c_left, boat)]))

    return None

# Run the function
solution = missionaries_and_cannibals()

# Display the result
if solution:
    print("Steps to solve the problem:\n")
    for i, (m, c, b) in enumerate(solution):
        print(f"Step {i}: M_left={m}, C_left={c}, Boat={'Left' if b==1 else 'Right'}")
else:
    print("No solution found.")

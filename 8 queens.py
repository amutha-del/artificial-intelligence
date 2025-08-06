N = 8
board = [-1] * N  # board[i] = column of queen in row i

def is_safe(row, col):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        print_solution()
        return True
    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
    return False

def print_solution():
    for i in range(N):
        row = ["."] * N
        row[board[i]] = "Q"
        print(" ".join(row))
    print()

# Start solving from row 0
solve(0)

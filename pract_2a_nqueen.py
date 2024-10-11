def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1]*n)
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

def print_board(board):
    for row in board:
        print(" ".join(row))

def main():
    n = int(input("Enter the number of queens: "))
    solutions = solve_n_queens(n)
    print(f"There are {len(solutions)} solutions for {n}-Queen problem:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        print_board(solution)
        print()

if __name__ == "__main__":
    main()

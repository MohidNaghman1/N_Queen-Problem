# Check if it's safe to place a queen at board[row][col]
def is_safe(board, row, col, n):    
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check the column above
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the right side
    for i, j in zip(range(row, n), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board, n):
    """Print the current state of the board."""
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

def user_place_queen(board, n, queens_placed):
    """Allow the user to place a queen on the board."""
    print("\nCurrent Board:")
    print_board(board, n)
    
    while True:
        try:
            row = int(input(f"Enter row (0-{n-1}) to place a queen: "))
            col = int(input(f"Enter column (0-{n-1}) to place a queen: "))
            
            if row < 0 or row >= n or col < 0 or col >= n:
                print("Invalid position. Try again.")
                continue
            
            if board[row][col] == 1:
                print("A queen is already placed here. Try again.")
                continue
            
            if not is_safe(board, row, col, n):
                print("This position is not safe. Queens are attacking each other. Try again.")
                continue
            
            board[row][col] = 1  # Place the queen
            queens_placed += 1
            print("Queen placed successfully!")
            break
        
        except ValueError:
            print("Invalid input. Please enter integers.")
    
    return queens_placed

def main():
    """Main function to run the N-Queens game."""
    n = int(input("Enter the size of the board (N): "))
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize empty board
    queens_placed = 0
    
    while True:
        print("\n1. Place a queen")
        print("2. Check if the current board is valid")
        print("3. Reset the board")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            if queens_placed < n:
                queens_placed = user_place_queen(board, n, queens_placed)
            else:
                print(f"All {n} queens have already been placed. You cannot place more.")
        elif choice == "2":
            if queens_placed == n:  # Check if all queens are placed
                print("\nCurrent Board:")
                print_board(board, n)
                print("All queens are placed. Checking if the board is valid...")
                valid = True
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == 1 and not is_safe(board, i, j, n):
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    print("The board is valid! You've solved the N-Queens problem!")
                else:
                    print("The board is invalid. Queens are attacking each other.")
            else:
                print(f"Only {queens_placed} queens have been placed. Place all {n} queens to check validity.")
        elif choice == "3":
            board = [[0 for _ in range(n)] for _ in range(n)]  # Reset the board
            queens_placed = 0
            print("The board has been reset.")
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
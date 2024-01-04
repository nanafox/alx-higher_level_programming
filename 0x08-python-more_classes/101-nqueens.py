#!/usr/bin/python3

"""Solves the N-Queens challenge."""


def n_queens(n: int) -> "list[list[list[int]]]":
    """
    Solves the N-Queens challenge.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list[list[list[int]]]: The chessboard with the Queens placed in
        non-attacking positions.
    """

    def is_non_attack(board: list, row: int, col: int) -> bool:
        """
        Checks whether a slot is non-attacking when a Queen is placed.

        Args:
            board (list): The board to check.
            row (int): The current row on the board.
            col (int): The column of the board.

        Returns:
            bool: True if the position leads to a non-attacking placement,
            else False
        """
        for i in range(row):
            if (
                board[i] == col  # check for vertical possible attacks
                or board[i] - i == col - row
                or board[i] + i == col + row
            ):
                return False

        return True

    def insert_queen(board: list, row: int) -> None:
        """
        Handles the placement of Queens in a non-attacking fashion.

        Args:
            board (list): The board to insert into (temporal).
            row (int): The current row in the board.
        """
        if row == n:  # base case
            chessboard.append([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_non_attack(board, row, col):
                board[row] = col
                insert_queen(board, row + 1)
                board[row] = 0

    chessboard = []
    board = [0] * n
    insert_queen(board, 0)

    return chessboard


def print_non_attack_combinations(chessboard: "list[list[list[int]]]") -> None:
    """
    Prints all the non-attacking combinations of N-Queens.

    Args:
        chessboard (list[list[list[int]]]): The list of all non-attacking
        combinations.
    """
    for row in chessboard:
        print(row)


if __name__ == "__main__":
    """Entry point"""
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_non_attack_combinations(n_queens(N))

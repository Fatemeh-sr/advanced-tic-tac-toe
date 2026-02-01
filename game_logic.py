board = [
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
]
move = {"a1": 0, "b1": 0, "a2": 0, "b2": 1, "symbol_first": "X"}


def moving(board, move):
    # انتخاب نماد دوم
    symbol_second = "O" if move["symbol_first"] == "X" else "X"

    # قرار دادن نمادها روی board
    board[move["a1"]][move["b1"]] = move["symbol_first"]
    board[move["a2"]][move["b2"]] = symbol_second


moving(board, move)
board2 = [row[:] for row in board]
move = {"a1": 3, "b1": 0, "a2": 2, "b2": 1, "symbol_first": "O"}
moving(board, move)

# چاپ board
for row in board:
    print(" ".join(row))

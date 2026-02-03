# move = {"a1": 0, "b1": 0, "a2": 0, "b2": 1, "symbol_first": "X"}


class Move:
    def __init__(self, a1, b1, a2, b2, symbol_first):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
        self.symbol_first = symbol_first

    # متد برای اعمال حرکت روی board
    def apply(self, board):
        symbol_second = "O" if self.symbol_first == "X" else "X"
        board[self.a1][self.b1] = self.symbol_first
        board[self.a2][self.b2] = symbol_second


board = [
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
]

# ایجاد حرکت‌ها
move1 = Move(0, 0, 0, 1, "X")  # دومینو X-O
move2 = Move(3, 0, 2, 0, "O")  # دومینو O-X

# اعمال حرکت‌ها
move1.apply(board)
move2.apply(board)
Move(3, 1, 3, 2, "X").apply(board)

# چاپ board
for row in board:
    print(" ".join(row))

def get_user_move(board) :
    #Hi

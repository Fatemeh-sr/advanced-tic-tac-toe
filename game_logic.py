# move = {"a1": 0, "b1": 0, "a2": 0, "b2": 1, "symbol_first": "X"}


class Move:
    def __init__(self, a1, b1, a2, b2, symbol_first):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
        self.symbol_first = symbol_first

    def apply(self, board):
        symbol_second = "O" if self.symbol_first == "X" else "X"
        board[self.a1][self.b1] = self.symbol_first
        board[self.a2][self.b2] = symbol_second


# تابع اعتبارسنجی
def is_valid_move(board, move):
    r1, c1 = move.a1, move.b1
    r2, c2 = move.a2, move.b2

    if not (0 <= r1 < 4 and 0 <= c1 < 4 and 0 <= r2 < 4 and 0 <= c2 < 4):
        return False
    if board[r1][c1] != "-" or board[r2][c2] != "-":
        return False
    if abs(r1 - r2) + abs(c1 - c2) != 1:
        return False
    return True


# تابع wrapper برای ورودی کاربر / تست
def user_move(board, r1, c1, r2, c2, symbol_first):
    try:
        move = Move(r1, c1, r2, c2, symbol_first)
        if not is_valid_move(board, move):
            print("حرکت نامعتبر است!")
            return False
        move.apply(board)
        return True
    except Exception as e:
        print("خطا در حرکت:", e)
        return False


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

import chess

board = chess.Board()

for i in board.legal_moves:
	print(i)

board.push_san("e4")
board.push_san("e5")

print(board)


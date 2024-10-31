import pygame
import pygame.gfxdraw
import random
import enum
from copy import deepcopy
import os

# Graphical size settings
SQUARE_SIZE = 100
DISC_SIZE_RATIO = 0.8

# Colours
BLUE_COLOR = (23, 93, 222)
YELLOW_COLOR = (255, 240, 0)
RED_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (19, 72, 162)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)


class Event(enum.Enum):
	PIECE_PLACED = 1
	GAME_WON = 2
	GAME_RESET = 3


class Observer:

	def __init__(self):
		pass

	def update(self, obj, event, *argv):
		pass


class Observable:

	def __init__(self):
		self._observers = []

	def notify(self, event, *argv):
		for obs in self._observers:
			obs.update(self, event, *argv)

	def add_observer(self, obs):
		self._observers.append(obs)

	def remove_observer(self, obs):
		if obs in self._observers:
			self._observers.remove(obs)


class Connect4Game(Observable):

	def __init__(self, rows=6, cols=7):
		super().__init__()
		self._rows = rows
		self._cols = cols
		self._board = None
		self._turn = None
		self._won = None
		self.reset_game()

	def reset_game(self):
		"""
		Resets the game state (board and variables)
		"""
		self._board = [[0 for _ in range(self._rows)] for _ in range(self._cols)]
		self._turn = random.randint(1, 2)
		self._won = None
		self.notify(Event.GAME_RESET)

	def place(self, c):
		"""
		Tries to place the playing colour on the cth column
		:param c: column to place on
		:return: position of placed colour or None if not placeable
		"""
		for r in range(self._rows):
			if self._board[c][r] == 0:
				self._board[c][r] = self._turn

				if self._turn == 1:
					self._turn = 2
				else:
					self._turn = 1

				self.notify(Event.PIECE_PLACED, (c, r))
				self.check_win((c, r))
				return c, r
		return None

	def check_win(self, pos):
		"""
		Checks for win/draw from newly added disc
		:param pos: position from which to check the win
		:return: player number if a win occurs, 0 if a draw occurs, None otherwise
		"""
		c = pos[0]
		r = pos[1]
		player = self._board[c][r]

		min_col = max(c-3, 0)
		max_col = min(c+3, self._cols-1)
		min_row = max(r - 3, 0)
		max_row = min(r + 3, self._rows - 1)

		# Horizontal check
		count = 0
		for ci in range(min_col, max_col + 1):
			if self._board[ci][r] == player:
				count += 1
			else:
				count = 0
			if count == 4:
				self._won = player
				self.notify(Event.GAME_WON, self._won)
				return self._won

		# Vertical check
		count = 0
		for ri in range(min_row, max_row + 1):
			if self._board[c][ri] == player:
				count += 1
			else:
				count = 0
			if count == 4:
				self._won = player
				self.notify(Event.GAME_WON, self._won)
				return self._won

		count1 = 0
		count2 = 0
		# Diagonal check
		for i in range(-3, 4):
			# bottom-left -> top-right
			if 0 <= c + i < self._cols and 0 <= r + i < self._rows:
				if self._board[c + i][r + i] == player:
					count1 += 1
				else:
					count1 = 0
				if count1 == 4:
					self._won = player
					self.notify(Event.GAME_WON, self._won)
					return self._won
			# bottom-right -> top-let
			if 0 <= c + i < self._cols and 0 <= r - i < self._rows:
				if self._board[c + i][r - i] == player:
					count2 += 1
				else:
					count2 = 0
				if count2 == 4:
					self._won = player
					self.notify(Event.GAME_WON, self._won)
					return self._won

		# Draw check
		if sum([x.count(0) for x in self._board]) == 0:
			self._won = 0
			self.notify(Event.GAME_WON, self._won)
			return self._won

		self._won = None
		return self._won

	def get_cols(self):
		"""
		:return: The number of columns of the game
		"""
		return self._cols

	def get_rows(self):
		"""
		:return: The number of rows of the game
		"""
		return self._rows

	def get_win(self):
		"""
		:return: If one play won or not
		"""
		return self._won

	def get_turn(self):
		"""
		:return: To which player is the turn
		"""
		return self._turn

	def get_board(self):
		"""
		:return: The game board
		"""
		return self._board

	def board_at(self, c, r):
		"""
		:param: c, the column
		:param: r, the row
		:return: What value is held at column c, row r in the board
		"""
		return self._board[c][r]

	def copy_state(self):
		"""
		Use this instead of the copy() method. Useful as we don't want our graphical interface (viewed as an Observer in this class)
		to be updated when we are playing moves in our tree search.
		"""

		# Temporary removes the
		temporary_observers = self._observers
		self._observers = []

		new_one = deepcopy(self)
		new_one._observers.clear()  # Clear observers, such as GUI in our case.

		# Reassign the observers after deepcopy
		self._observers = temporary_observers

		return new_one


class Connect4Viewer(Observer):

	def __init__(self, game):
		super(Observer, self).__init__()
		assert game is not None
		self._game = game
		self._game.add_observer(self)
		self._screen = None
		self._font = None

	def initialize(self):
		"""
		Initialises the view window
		"""
		pygame.init()
		icon = pygame.image.load(f"{os.path.dirname(__file__)}/icon.png")
		pygame.display.set_icon(icon)
		pygame.display.set_caption("Connect Four")
		self._font = pygame.font.SysFont(None, 80)
		self._screen = pygame.display.set_mode([self._game.get_cols() * SQUARE_SIZE, self._game.get_rows() * SQUARE_SIZE])
		self.draw_board()

	def draw_board(self):
		"""
		Draws board[c][r] with c = 0 and r = 0 being bottom left
		0 = empty (background colour)
		1 = yellow
		2 = red
		"""
		self._screen.fill(BLUE_COLOR)

		for r in range(self._game.get_rows()):
			for c in range(self._game.get_cols()):
				colour = BACKGROUND_COLOR
				if self._game.board_at(c, r) == 1:
					colour = YELLOW_COLOR
				if self._game.board_at(c, r) == 2:
					colour = RED_COLOR

				# Anti-aliased circle drawing
				pygame.gfxdraw.aacircle(self._screen, c * SQUARE_SIZE + SQUARE_SIZE // 2,
										self._game.get_rows() * SQUARE_SIZE - r * SQUARE_SIZE - SQUARE_SIZE // 2,
										int(DISC_SIZE_RATIO * SQUARE_SIZE / 2),
										colour)

				pygame.gfxdraw.filled_circle(self._screen, c * SQUARE_SIZE + SQUARE_SIZE // 2,
											 self._game.get_rows() * SQUARE_SIZE - r * SQUARE_SIZE - SQUARE_SIZE // 2,
											 int(DISC_SIZE_RATIO * SQUARE_SIZE / 2),
											 colour)
		pygame.display.update()

	def update(self, obj, event, *argv):
		"""
		Called when notified. Updates the view.
		"""
		if event == Event.GAME_WON:
			won = argv[0]
			self.draw_win_message(won)
		elif event == Event.GAME_RESET:
			self.draw_board()
		elif event == Event.PIECE_PLACED:
			self.draw_board()

	def draw_win_message(self, won):
		"""
		Displays win message on top of the board
		"""
		if won == 1:
			img = self._font.render("Yellow won", True, BLACK_COLOR, YELLOW_COLOR)
		elif won == 2:
			img = self._font.render("Red won", True, WHITE_COLOR, RED_COLOR)
		else:
			img = self._font.render("Draw", True, WHITE_COLOR, BLUE_COLOR)

		rect = img.get_rect()
		rect.center = ((self._game.get_cols() * SQUARE_SIZE) // 2, (self._game.get_rows() * SQUARE_SIZE) // 2)

		self._screen.blit(img, rect)
		pygame.display.update()


if __name__ == '__main__':
	game = Connect4Game()
	game.reset_game()

	view = Connect4Viewer(game=game)
	view.initialize()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				if game.get_win() is None:
					game.place(pygame.mouse.get_pos()[0] // SQUARE_SIZE)
				else:
					game.reset_game()

	pygame.quit()

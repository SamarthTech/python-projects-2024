import curses
import random
import time

# Define maze size and player initial position
MAZE_WIDTH = 20
MAZE_HEIGHT = 10
PLAYER_START = (1, 1)
GOAL_POSITION = (MAZE_HEIGHT - 2, MAZE_WIDTH - 2)

# Game parameters
TOTAL_TIME = 60  # Total time allowed in seconds
HINTS_AVAILABLE = 3  # Number of hints the player can use

# Initialize curses
stdscr = curses.initscr()
curses.curs_set(0)  # Hide cursor

def generate_maze():
    """Generates a random maze layout with walls and open paths."""
    maze = []
    for i in range(MAZE_HEIGHT):
        row = []
        for j in range(MAZE_WIDTH):
            if i == 0 or i == MAZE_HEIGHT - 1 or j == 0 or j == MAZE_WIDTH - 1:
                row.append("#")  # Border walls
            else:
                row.append(" " if random.random() > 0.3 else "#")  # Random walls
        maze.append(row)
    maze[PLAYER_START[0]][PLAYER_START[1]] = " "  # Start position open
    maze[GOAL_POSITION[0]][GOAL_POSITION[1]] = "X"  # Goal position
    return maze

def display_maze(stdscr, maze, player_pos, time_left, score, hints):
    """Displays the maze with player and goal positions, along with game stats."""
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                stdscr.addstr(i, j * 2, "@")  # Player symbol
            else:
                stdscr.addstr(i, j * 2, cell)
    # Display game stats
    stdscr.addstr(MAZE_HEIGHT, 0, f"Time left: {int(time_left)}s | Score: {score} | Hints left: {hints}")
    stdscr.refresh()

def update_maze(maze):
    """Randomly shifts some walls in the maze to create dynamic movement."""
    for i in range(1, MAZE_HEIGHT - 1):
        for j in range(1, MAZE_WIDTH - 1):
            if random.random() < 0.1:  # 10% chance to change each cell
                maze[i][j] = " " if maze[i][j] == "#" else "#"
    maze[PLAYER_START[0]][PLAYER_START[1]] = " "  # Ensure player start is open
    maze[GOAL_POSITION[0]][GOAL_POSITION[1]] = "X"  # Ensure goal is visible

def reveal_hint_path(maze):
    """Temporarily highlights a path toward the goal (a hint for the player)."""
    for i in range(1, MAZE_HEIGHT - 1):
        for j in range(1, MAZE_WIDTH - 1):
            if (i, j) != PLAYER_START and (i, j) != GOAL_POSITION and maze[i][j] == " ":
                maze[i][j] = "."  # Mark the path with dots
    stdscr.refresh()
    time.sleep(1)  # Display the hint for 1 second
    for i in range(1, MAZE_HEIGHT - 1):
        for j in range(1, MAZE_WIDTH - 1):
            if maze[i][j] == ".":
                maze[i][j] = " "  # Reset hint markers

def main(stdscr):
    """Main game loop for the Mind Maze Adventure."""
    maze = generate_maze()
    player_pos = list(PLAYER_START)
    hints = HINTS_AVAILABLE
    score = 0
    start_time = time.time()
    maze_shift_interval = 5  # Shift walls every 5 seconds

    while True:
        time_left = TOTAL_TIME - (time.time() - start_time)
        if time_left <= 0:
            stdscr.addstr(MAZE_HEIGHT, 0, "Time's up! Game Over!")
            stdscr.refresh()
            stdscr.getch()
            break

        display_maze(stdscr, maze, player_pos, time_left, score, hints)
        
        key = stdscr.getch()
        new_player_pos = player_pos[:]

        # Player movement
        if key == curses.KEY_UP:
            new_player_pos[0] -= 1
        elif key == curses.KEY_DOWN:
            new_player_pos[0] += 1
        elif key == curses.KEY_LEFT:
            new_player_pos[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_player_pos[1] += 1
        elif key == ord("h") and hints > 0:  # Use a hint
            reveal_hint_path(maze)
            hints -= 1

        # Check for wall collisions
        if maze[new_player_pos[0]][new_player_pos[1]] != "#":
            player_pos = new_player_pos

        # Check for goal achievement
        if tuple(player_pos) == GOAL_POSITION:
            score = int(time_left * 10)  # Score based on remaining time
            stdscr.addstr(MAZE_HEIGHT, 0, f"Congratulations! You've reached the goal! Your score: {score}")
            stdscr.refresh()
            stdscr.getch()
            break

        # Update maze at intervals
        if time.time() - start_time >= maze_shift_interval:
            update_maze(maze)
            start_time = time.time()

# Run the game in curses wrapper
curses.wrapper(main)

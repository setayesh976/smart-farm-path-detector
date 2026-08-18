"""
Farm Path Detector
--------------------
A simple simulation of path detection for an autonomous spraying robot
moving between crop rows on a farm.

The farm is represented as a 2D grid:
  'R' = crop row (the robot must stay between rows, not drive over them)
  '.' = open path (safe to drive through)
  'S' = starting position of the robot

The robot moves in a "boustrophedon" pattern (back-and-forth, like how a
lawnmower or an actual crop sprayer works): it drives straight down one
row gap, then turns to move into the next row gap, and drives back up.
This is a classic, well-known coverage-path algorithm — not a trained
AI model. It was chosen because it's simple to explain and mirrors how
real agricultural spraying robots plan their coverage path.

For each step, the program prints the movement command the robot would
follow: Forward, Left, or Right.
"""

# Farm grid: each row of the list is one row of the field.
# 'R' = crop row (blocked), '.' = drivable path, 'S' = start position
FARM_GRID = [
    list("R.R.R.R"),
    list("R.R.R.R"),
    list("R.R.R.R"),
    list("R.R.R.R"),
    list("S.R.R.R"),
]

ROWS = len(FARM_GRID)
COLS = len(FARM_GRID[0])


def print_farm():
    print("\n=== Farm Layout ===")
    for row in FARM_GRID:
        print("  " + " ".join(row))
    print("  (R = crop row, . = open path, S = start)")


def find_start():
    for r in range(ROWS):
        for c in range(COLS):
            if FARM_GRID[r][c] == "S":
                return (r, c)
    return None


def get_path_columns():
    """
    Returns the list of column indices that are open paths ('.' or 'S')
    in the first row, i.e. the lanes between crop rows the robot can
    drive through.
    """
    columns = []
    for c in range(COLS):
        if FARM_GRID[0][c] in (".", "S"):
            columns.append(c)
    return columns


def generate_coverage_path():
    """
    Generates the full sequence of (row, col) grid positions the robot
    should visit to cover every open lane in the field, using a
    boustrophedon (back-and-forth) pattern: down one lane, across to the
    next, up that lane, across again, and so on.
    """
    lanes = get_path_columns()
    path = []

    going_down = True
    for lane in lanes:
        row_range = range(ROWS) if going_down else range(ROWS - 1, -1, -1)
        for r in row_range:
            path.append((r, lane))
        going_down = not going_down  # reverse direction for the next lane

    return path


def path_to_commands(path):
    """
    Converts a sequence of grid positions into movement commands:
    Forward (same lane, moving up/down), Left/Right (switching lanes).
    """
    commands = []
    for i in range(1, len(path)):
        prev_r, prev_c = path[i - 1]
        curr_r, curr_c = path[i]

        if curr_c != prev_c:
            # Switching lanes: decide turn direction based on column change
            commands.append("Right" if curr_c > prev_c else "Left")
        else:
            commands.append("Forward")

    return commands


def print_path_commands(commands):
    print("\n=== Movement Commands ===")
    for i, cmd in enumerate(commands, start=1):
        print(f"  Step {i:>2}: {cmd}")


def print_path_summary(path):
    total_steps = len(path) - 1
    lanes_covered = len(get_path_columns())
    print("\n=== Coverage Summary ===")
    print(f"  Lanes covered: {lanes_covered}")
    print(f"  Total movement steps: {total_steps}")
    print(f"  Start position: {path[0]}")
    print(f"  End position:   {path[-1]}")


def main():
    print("=== Farm Path Detector ===")
    print("Simulated path planning for an autonomous spraying robot.\n")

    print_farm()

    start = find_start()
    if start is None:
        print("\nNo start position ('S') found in the grid.")
        return

    path = generate_coverage_path()
    commands = path_to_commands(path)

    print_path_commands(commands)
    print_path_summary(path)


if __name__ == "__main__":
    main()

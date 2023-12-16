from collections import deque


def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().splitlines()


def get_number_of_energized_tiles() -> int:
    rows = get_file_rows('input.txt')
    # BFS
    # row, column, row_direction, column_direction
    start = [(0, -1, 0, 1)]  # Start in the top-left corner and heading to the right
    already_seen = set()
    queue = deque(start)
    while queue:
        row, column, row_direction, column_direction = queue.popleft()
        row += row_direction
        column += column_direction
        # Out of bounds check
        if row < 0 or row >= len(rows) or column < 0 or column >= len(rows[0]):
            continue  # skip
        # Different behavior based on the char value
        char = rows[row][column]
        # Empty cell => pass through
        if char == '.' or (char == '-' and column_direction != 0) or (char == '|' and row_direction != 0):
            if (row, column, row_direction, column_direction) not in already_seen:
                already_seen.add((row, column, row_direction, column_direction))
                queue.append((row, column, row_direction, column_direction))
        elif char == '/':
            # (0, 1)  => (-1, 0)
            # (0, -1) => (1, 0)
            # (1, 0)  => (0, -1)
            # (-1, 0) => (0, 1)
            row_direction, column_direction = - column_direction, -row_direction
            if (row, column, row_direction, column_direction) not in already_seen:
                already_seen.add((row, column, row_direction, column_direction))
                queue.append((row, column, row_direction, column_direction))
        elif char == '\\':
            # (0, 1)  => (1, 0)
            # (0, -1) => (-1, 0)
            # (1, 0)  => (0, 1)
            # (-1, 0) => (0, -1)
            row_direction, column_direction = column_direction, row_direction
            if (row, column, row_direction, column_direction) not in already_seen:
                already_seen.add((row, column, row_direction, column_direction))
                queue.append((row, column, row_direction, column_direction))
        else:  # vertical splitters
            for row_direction, column_direction in [(1, 0), (-1, 0)] if char == "|" else [(0, 1), (0, -1)]:
                if (row, column, row_direction, column_direction) not in already_seen:
                    already_seen.add((row, column, row_direction, column_direction))
                    queue.append((row, column, row_direction, column_direction))

    energized_tiles_coordinates = {(row, column) for (row, column, _, _) in already_seen}

    return len(energized_tiles_coordinates)


def get_number_of_energized_tiles_starting_from(
        row: int, column: int, row_direction: int, column_direction: int, rows: list[str]
) -> int:
    # BFS
    start = [(row, column, row_direction, column_direction)]
    already_seen = set()
    queue = deque(start)
    while queue:
        row, column, row_direction, column_direction = queue.popleft()
        row += row_direction
        column += column_direction
        # Out of bounds check
        if row < 0 or row >= len(rows) or column < 0 or column >= len(rows[0]):
            continue  # skip
        # Different behavior based on the char value
        char = rows[row][column]
        # Empty cell => pass through
        if char == '.' or (char == '-' and column_direction != 0) or (char == '|' and row_direction != 0):
            if (row, column, row_direction, column_direction) not in already_seen:
                already_seen.add((row, column, row_direction, column_direction))
                queue.append((row, column, row_direction, column_direction))
        elif char == '/':
            # (0, 1)  => (-1, 0)
            # (0, -1) => (1, 0)
            # (1, 0)  => (0, -1)
            # (-1, 0) => (0, 1)
            row_direction, column_direction = - column_direction, -row_direction
            if (row, column, row_direction, column_direction) not in already_seen:
                already_seen.add((row, column, row_direction, column_direction))
                queue.append((row, column, row_direction, column_direction))
        elif char == '\\':
            # (0, 1)  => (1, 0)
            # (0, -1) => (-1, 0)
            # (1, 0)  => (0, 1)
            # (-1, 0) => (0, -1)
            row_direction, column_direction = column_direction, row_direction
            if (row, column, row_direction, column_direction) not in already_seen:
                already_seen.add((row, column, row_direction, column_direction))
                queue.append((row, column, row_direction, column_direction))
        else:  # vertical splitters
            for row_direction, column_direction in [(1, 0), (-1, 0)] if char == "|" else [(0, 1), (0, -1)]:
                if (row, column, row_direction, column_direction) not in already_seen:
                    already_seen.add((row, column, row_direction, column_direction))
                    queue.append((row, column, row_direction, column_direction))

    energized_tiles_coordinates = {(row, column) for (row, column, _, _) in already_seen}

    return len(energized_tiles_coordinates)


def get_max_number_of_energized_tiles() -> int:
    rows = get_file_rows('input.txt')
    result = 0
    # The beam could start on any tile in the top row (heading downward),
    # any tile in the bottom row (heading upward),
    for row in range(len(rows)):
        result = max(result, get_number_of_energized_tiles_starting_from(row, -1, 0, 1, rows))
        result = max(result, get_number_of_energized_tiles_starting_from(row, len(rows[0]), 0, -1, rows))
    # any tile in the leftmost column (heading right),
    # or any tile in the rightmost column (heading left)
    for column in range(len(rows[0])):
        result = max(result, get_number_of_energized_tiles_starting_from(-1, column, 1, 0, rows))
        result = max(result, get_number_of_energized_tiles_starting_from(len(rows), column, -1, 0, rows))
    return result


if __name__ == '__main__':
    print(f'Part 1 - number of energized tiles = {get_number_of_energized_tiles()}')
    print(f'Part 2 - max number of energized tiles = {get_max_number_of_energized_tiles()}')

from heapq import heappop, heappush


def get_file_rows(path: str) -> list[list[int]]:
    with open(path) as file:
        return [list(map(int, line.strip())) for line in file]


def get_heat_loss() -> int:
    rows = get_file_rows('input.txt')
    # From top-left corner to the bottom-right corner
    # Same direction max 3 times in a row
    # Dijkstra's algorithm to find the shortest path between 2 points in a weighted graph
    visited = set()
    # heat_loss, row, column, row_direction, column_direction, times_same_direction
    priority_queue = [(0, 0, 0, 0, 0, 0)]  # queue where each item has a special key that quantifies its priority
    while priority_queue:
        heat_loss, row, column, row_direction, column_direction, times_same_direction = heappop(priority_queue)
        # Exit condition
        if row == len(rows) - 1 and column == len(rows[0]) - 1:
            return heat_loss
        # To avoid loops we avoid to consider the same state
        if (row, column, row_direction, column_direction, times_same_direction) in visited:
            continue  # skip
        visited.add((row, column, row_direction, column_direction, times_same_direction))
        if times_same_direction < 3 and (row_direction, column_direction) != (0, 0):
            next_row = row + row_direction
            next_column = column + column_direction
            # Out of bounds check
            if 0 <= next_row < len(rows) and 0 <= next_column < len(rows[0]):
                new_heat_loss = heat_loss + rows[next_row][next_column]
                heappush(
                    priority_queue,
                    (new_heat_loss, next_row, next_column, row_direction, column_direction, times_same_direction + 1)
                )
        # Try all the 4 possible directions
        for next_row_direction, next_column_direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            # Direction is valid only if his not the current direction (already considered)
            # and not the opposite of the current direction (going back)
            if ((next_row_direction, next_column_direction) != (row_direction, column_direction)
                    and (next_row_direction, next_column_direction) != (-row_direction, -column_direction)):
                next_row = row + next_row_direction
                next_column = column + next_column_direction
                # Out of bounds check
                if 0 <= next_row < len(rows) and 0 <= next_column < len(rows[0]):
                    new_heat_loss = heat_loss + rows[next_row][next_column]
                    # First time in this direction
                    heappush(
                        priority_queue,
                        (new_heat_loss, next_row, next_column, next_row_direction, next_column_direction, 1)
                    )
    return 0


def get_heat_loss_ultra_crucibles() -> int:
    rows = get_file_rows('input.txt')
    # From top-left corner to the bottom-right corner
    # Same direction min 4 times and max 10 times in a row
    # Dijkstra's algorithm to find the shortest path between 2 points in a weighted graph
    visited = set()
    # heat_loss, row, column, row_direction, column_direction, times_same_direction
    priority_queue = [(0, 0, 0, 0, 0, 0)]  # queue where each item has a special key that quantifies its priority
    while priority_queue:
        heat_loss, row, column, row_direction, column_direction, times_same_direction = heappop(priority_queue)
        # Exit condition
        if row == len(rows) - 1 and column == len(rows[0]) - 1 and times_same_direction >= 4:
            return heat_loss
        # To avoid loops we avoid to consider the same state
        if (row, column, row_direction, column_direction, times_same_direction) in visited:
            continue  # skip
        visited.add((row, column, row_direction, column_direction, times_same_direction))
        if times_same_direction < 10 and (row_direction, column_direction) != (0, 0):
            next_row = row + row_direction
            next_column = column + column_direction
            # Out of bounds check
            if 0 <= next_row < len(rows) and 0 <= next_column < len(rows[0]):
                new_heat_loss = heat_loss + rows[next_row][next_column]
                heappush(
                    priority_queue,
                    (new_heat_loss, next_row, next_column, row_direction, column_direction, times_same_direction + 1)
                )
        if times_same_direction >= 4 or (row_direction, column_direction) == (0, 0):
            # Try all the 4 possible directions
            for next_row_direction, next_column_direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                # Direction is valid only if his not the current direction (already considered)
                # and not the opposite of the current direction (going back)
                if ((next_row_direction, next_column_direction) != (row_direction, column_direction)
                        and (next_row_direction, next_column_direction) != (-row_direction, -column_direction)):
                    next_row = row + next_row_direction
                    next_column = column + next_column_direction
                    # Out of bounds check
                    if 0 <= next_row < len(rows) and 0 <= next_column < len(rows[0]):
                        new_heat_loss = heat_loss + rows[next_row][next_column]
                        # First time in this direction
                        heappush(
                            priority_queue,
                            (new_heat_loss, next_row, next_column, next_row_direction, next_column_direction, 1)
                        )
    return 0


if __name__ == '__main__':
    print(f'Part 1: heat loss = {get_heat_loss()}')
    print(f'Part 2: heat loss with ultra crucibles = {get_heat_loss_ultra_crucibles()}')

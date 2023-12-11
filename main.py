from collections import deque

EXPANSION_FACTOR = 1000000


def get_file_matrix(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().splitlines()


def get_flipped_matrix(matrix: list[str]) -> list[str]:
    flipped_matrix = [''] * len(matrix[0])
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            flipped_matrix[j] += char
    return flipped_matrix


def get_expanded_galaxies_by_rows(galaxies: list[str]) -> list[str]:
    rows_to_expand = []
    for i, row in enumerate(galaxies):
        to_expand = True
        for char in row:
            if char != '.':
                to_expand = False
                break
        if to_expand:
            rows_to_expand.append(i)
    galaxies_to_expand = []
    # rows expansion
    for i, row in enumerate(galaxies):
        galaxies_to_expand.append(row)
        if i in rows_to_expand:
            galaxies_to_expand.append('.' * len(row))
    return galaxies_to_expand


def get_shortest_path_between_two_galaxies(galaxy_0: tuple[int, int], galaxy_1: tuple[int, int]) -> int:
    diff_x = abs(galaxy_0[0] - galaxy_1[0])
    diff_y = abs(galaxy_0[1] - galaxy_1[1])
    return diff_x + diff_y


def get_sum_shortest_paths_between_all_galaxies() -> int:
    galaxies = get_file_matrix('input.txt')
    galaxies_expanded_by_rows = get_expanded_galaxies_by_rows(galaxies)
    # Flip the matrix to re-use the same expansion function
    flipped_galaxies = get_flipped_matrix(galaxies_expanded_by_rows)
    galaxies_expanded_by_columns = get_expanded_galaxies_by_rows(flipped_galaxies)
    expanded_galaxies = get_flipped_matrix(galaxies_expanded_by_columns)
    # Find all the galaxies positions
    galaxies_positions = {}
    galaxy_index = 1
    for i, row in enumerate(expanded_galaxies):
        for j, char in enumerate(row):
            if char != '.':
                galaxies_positions[galaxy_index] = (i, j)
                galaxy_index += 1
    # Calculate the distance between every galaxy
    result = 0
    queue = deque(galaxies_positions.values())
    while len(queue) > 1:
        current = queue.pop()
        for galaxy in queue:
            result += get_shortest_path_between_two_galaxies(current, galaxy)
    return result


def get_galaxies_rows_to_expand(galaxies: list[str]) -> list[int]:
    rows_to_expand = []
    for i, row in enumerate(galaxies):
        to_expand = True
        for char in row:
            if char != '.':
                to_expand = False
                break
        if to_expand:
            rows_to_expand.append(i)
    return rows_to_expand


def get_shortest_path_between_two_galaxies_part_2(
        galaxy_0: tuple[int, int], galaxy_1: tuple[int, int], rows_to_expand: list[int], columns_to_expand: list[int]
) -> int:
    total = 0
    x1, y1 = galaxy_0
    x2, y2 = galaxy_1
    # Control of every point between the 2 galaxies:
    # if it is a point to expand => add the EXPANSION_FACTOR
    # else => add 1
    for x in range(min(x1, x2), max(x1, x2)):
        total += EXPANSION_FACTOR if x in rows_to_expand else 1
    for y in range(min(y1, y2), max(y1, y2)):
        total += EXPANSION_FACTOR if y in columns_to_expand else 1
    return total


def get_sum_shortest_paths_between_all_galaxies_part_2() -> int:
    galaxies = get_file_matrix('input.txt')
    rows_to_expand = get_galaxies_rows_to_expand(galaxies)
    # Flip the matrix to re-use the same expansion function
    flipped_galaxies = get_flipped_matrix(galaxies)
    columns_to_expand = get_galaxies_rows_to_expand(flipped_galaxies)
    # Find all the galaxies positions
    galaxies_positions = {}
    galaxy_index = 1
    for i, row in enumerate(galaxies):
        for j, char in enumerate(row):
            if char != '.':
                galaxies_positions[galaxy_index] = (i, j)
                galaxy_index += 1
    # Calculate the distance between every galaxy
    result = 0
    queue = deque(galaxies_positions.values())
    while len(queue) > 1:
        current = queue.pop()
        for galaxy in queue:
            result += get_shortest_path_between_two_galaxies_part_2(current, galaxy, rows_to_expand, columns_to_expand)
    return result


if __name__ == '__main__':
    # print(f'Sum of the shortest paths between all the galaxies: {get_sum_shortest_paths_between_all_galaxies()}')
    print(f'Sum of the shortest paths between all the galaxies with expansion factor:'
          f' {get_sum_shortest_paths_between_all_galaxies_part_2()}')

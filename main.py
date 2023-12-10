from collections import deque


def get_file_matrix(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().splitlines()


def get_steps_to_reach_the_farthest_position():
    # test_0 = square loop of pipe
    # test_1 = pipes not connected to the loop
    # test_2 = more complex main loop
    matrix = get_file_matrix('input.txt')
    # Find the starting position := 'S'
    # (number_of_row, number_of_column)
    starting_position = (-1, -1)
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == 'S':
                starting_position = (i, j)
                break
        if starting_position != (-1, -1):
            break
    print(f'Starting position: {starting_position}')
    # Breath-first search
    already_seen = {starting_position}
    distances = {starting_position: 0}
    # As queue
    queue = deque([starting_position])
    while queue:
        row, column = queue.popleft()
        current_char = matrix[row][column]
        north = (row - 1, column)
        south = (row + 1, column)
        west = (row, column - 1)
        east = (row, column + 1)
        # Comment for every direction:
        # If the coordinate is valid and the current char and the direction char is valid and the direction is new
        # Then add the direction in the already seen and in the queue + calculate the distance from the start
        # North
        if (row > 0 and current_char in "S|JL" and matrix[north[0]][north[1]] in "|F7"
                and north not in already_seen):
            already_seen.add(north)
            queue.append(north)
            distances[north] = distances[(row, column)] + 1
        # South
        if (row < len(matrix) - 1 and current_char in "S|7F" and matrix[south[0]][south[1]] in "|JL"
                and south not in already_seen):
            already_seen.add(south)
            queue.append(south)
            distances[south] = distances[(row, column)] + 1
        # West
        if (column > 0 and current_char in "S-J7" and matrix[west[0]][west[1]] in "-LF"
                and west not in already_seen):
            already_seen.add(west)
            queue.append(west)
            distances[west] = distances[(row, column)] + 1
        # East
        if (column < len(matrix[row]) - 1 and current_char in "S-LF" and matrix[east[0]][east[1]] in "-J7"
                and east not in already_seen):
            already_seen.add(east)
            queue.append(east)
            distances[east] = distances[(row, column)] + 1
    print(distances)
    return max(distances.values())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Steps to reach the farthest point from the starting position: {get_steps_to_reach_the_farthest_position()}')

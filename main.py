# Up, down, left, right
DIRECTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def get_meters_to_fill_the_lagoon() -> int:
    boundary_points = 0
    points = [(0, 0)]  # starting point = (0, 0)
    with open('input.txt') as file:
        for row in file:
            direction, step_number, _ = row.split()  # we ignore the RGB info
            row_direction, column_direction = DIRECTIONS[direction]
            step_number = int(step_number)
            boundary_points += step_number
            # Add a new vertex of the polygon
            row, column = points[-1]
            points.append((row + row_direction * step_number, column + column_direction * step_number))
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = abs(
        sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))
    ) // 2
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    internal_points = area - boundary_points // 2 + 1
    return internal_points + boundary_points


def get_meters_to_fill_the_lagoon_part_two() -> int:
    boundary_points = 0
    points = [(0, 0)]  # starting point = (0, 0)
    with open('input.txt') as file:
        for row in file:
            _, _, info = row.split()  # we ignore the direction and step_number info
            info = info[2:-1]  # ignore the hashtag char
            direction = "RDLU"[int(info[-1])]  # the last char indicate the direction
            row_direction, column_direction = DIRECTIONS[direction]
            step_number = int(info[:-1], 16)  # conversion of the five-digit hexadecimal number
            boundary_points += step_number
            # Add a new vertex of the polygon
            row, column = points[-1]
            points.append((row + row_direction * step_number, column + column_direction * step_number))
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = abs(
        sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))
    ) // 2
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    internal_points = area - boundary_points // 2 + 1
    return internal_points + boundary_points


if __name__ == '__main__':
    print(f'Part 1: cubic meters of lava to fill the lagoon = {get_meters_to_fill_the_lagoon()}')
    print(f'Part 2: cubic meters of lava to fill the lagoon = {get_meters_to_fill_the_lagoon_part_two()}')

def get_flipped_matrix(matrix: list[str]) -> list[str]:
    flipped_matrix = [''] * len(matrix[0])
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            flipped_matrix[j] += char
    return flipped_matrix


def get_separator(matrix: list[str]) -> int:
    for separator in range(1, len(matrix)):
        above = matrix[:separator][::-1]  # flipped to do the equality check
        below = matrix[separator:]
        # make the two part of the same length
        above = above[:len(below)]
        below = below[:len(above)]
        if above == below:
            return separator
    return 0


def get_number_from_patterns_notes() -> int:
    result = 0
    with open('input.txt') as file:
        patterns = file.read().split('\n\n')
        for pattern in patterns:
            matrix = pattern.splitlines()
            # row reflection
            row = get_separator(matrix)
            result += row * 100
            # column reflection
            column = get_separator(get_flipped_matrix(matrix))
            result += column
    return result


def get_separator_considering_smudges(matrix: list[str]) -> int:
    for separator in range(1, len(matrix)):
        above = matrix[:separator][::-1]  # flipped to do the equality check
        below = matrix[separator:]
        # if the number of difference between the two part are exactly one
        if sum(sum(0 if i == j else 1 for i, j in zip(x, y)) for x, y in zip(above, below)) == 1:
            return separator
    return 0


def get_number_from_patterns_notes_considering_smudges() -> int:
    result = 0
    with open('input.txt') as file:
        patterns = file.read().split('\n\n')
        for pattern in patterns:
            matrix = pattern.splitlines()
            # row reflection
            row = get_separator_considering_smudges(matrix)
            result += row * 100
            # column reflection
            column = get_separator_considering_smudges(get_flipped_matrix(matrix))
            result += column
    return result


if __name__ == '__main__':
    print(f'Part 1 number: {get_number_from_patterns_notes()}')
    print(f'Part 2 number: {get_number_from_patterns_notes_considering_smudges()}')

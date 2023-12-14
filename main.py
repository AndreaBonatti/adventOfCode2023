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


def get_total_load_on_the_north_support_beams() -> int:
    file = get_file_matrix('input.txt')
    flipped_file = get_flipped_matrix(file)
    # Sorting rocks
    sorted_flipped_file = []
    for row in flipped_file:
        groups = []
        for group in row.split('#'):
            groups.append("".join(list(sorted(group, reverse=True))))
        sorted_flipped_file.append("#".join(groups))
    sorted_file = get_flipped_matrix(sorted_flipped_file)
    # print(sorted_file)
    result = 0
    for i, row in enumerate(sorted_file):
        result += row.count('O') * (len(sorted_file) - i)
    return result


if __name__ == '__main__':
    print(f'Part 1: total load on the north support beams = {get_total_load_on_the_north_support_beams()}')

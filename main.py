def get_file_matrix(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().splitlines()


def get_groups_arrangement(arrangement: str) -> list[int]:
    groups = []
    count = 0
    for char in arrangement:
        if char == '#':
            count += 1
        else:
            if count != 0:
                groups.append(count)
                count = 0
    if count != 0:
        groups.append(count)
        count = 0
    return groups


def get_sum_of_hot_spring_arrangements(row: str) -> int:
    result = 0
    list_of_springs, contiguous_group_of_damaged_springs = row.split(' ')
    if '?' not in list_of_springs:
        result += 1
    else:
        # There could be 1 or more arrangements
        groups = [int(group) for group in contiguous_group_of_damaged_springs.split(',')]
        # Creation of all possible arrangements
        arrangements = [row]
        for i, char in enumerate(row):
            if char == '?':
                new_arrangements = []
                for arrangement in arrangements:
                    list_arrangement = list(arrangement)
                    list_arrangement[i] = '.'
                    new_arrangements.append("".join(list_arrangement))
                    list_arrangement[i] = '#'
                    new_arrangements.append("".join(list_arrangement))
                arrangements = new_arrangements
        # Add only the valids arrangements
        for arrangement in arrangements:
            if get_groups_arrangement(arrangement) == groups:
                result += 1

    return result


def get_sum_of_hot_springs_arrangements():
    matrix = get_file_matrix('input.txt')
    result = 0
    for row in matrix:
        result += get_sum_of_hot_spring_arrangements(row)
    return result


if __name__ == '__main__':
    print(f'Sum of all possibles hot springs arrangements: {get_sum_of_hot_springs_arrangements()}')

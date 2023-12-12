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
        arrangements = [list_of_springs]
        for i, char in enumerate(list_of_springs):
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


cache = {}


def count_arrangements(spring_conditions, numbers_of_groups):
    if spring_conditions == "":
        return 1 if numbers_of_groups == () else 0
    if numbers_of_groups == ():
        return 0 if "#" in spring_conditions else 1

    key = (spring_conditions, numbers_of_groups)
    if key in cache:
        return cache[key]

    result = 0
    if spring_conditions[0] in ".?":
        result += count_arrangements(spring_conditions[1:], numbers_of_groups)

    if spring_conditions[0] in "#?":
        if (numbers_of_groups[0] <= len(spring_conditions) and "." not in spring_conditions[:numbers_of_groups[0]]
                and (numbers_of_groups[0] == len(spring_conditions) or spring_conditions[numbers_of_groups[0]] != "#")):
            result += count_arrangements(spring_conditions[numbers_of_groups[0] + 1:], numbers_of_groups[1:])

    cache[key] = result
    return result


def get_sum_of_hot_springs_arrangements_part_2():
    matrix = get_file_matrix('input.txt')
    result = 0
    for row in matrix:
        spring_conditions, numbers_of_groups = row.split()
        numbers_of_groups = tuple(map(int, numbers_of_groups.split(",")))

        spring_conditions = "?".join([spring_conditions] * 5)
        numbers_of_groups *= 5

        result += count_arrangements(spring_conditions, numbers_of_groups)

    return result


if __name__ == '__main__':
    # print(f'Sum of all possibles hot springs arrangements: {get_sum_of_hot_springs_arrangements()}')
    print(f'Part 2: sum of all possibles hot springs arrangements: {get_sum_of_hot_springs_arrangements_part_2()}')

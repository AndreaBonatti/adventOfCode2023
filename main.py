import sys


def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split("\n")


def get_numbers(row: str) -> list[int]:
    result = []
    number = ""
    for char in row:
        if char.isdigit():
            number += char
        else:
            if number != "":
                result.append(int(number))
                number = ""
    if number != "":
        result.append(int(number))
    return result


# The list contains every mapped range.
# The range is composed by 3 values: the start of the range, the end of the range and the conversion value
def get_range_list_between_two_objects(raw_data: list[str]):
    range_list = []
    for i in range(1, len(raw_data)):
        temp_numbers = get_numbers(raw_data[i])
        start = temp_numbers[1]
        end = start + temp_numbers[2]
        conversion_factor = temp_numbers[0] - temp_numbers[1]
        new_range = [start, end, conversion_factor]
        range_list.append(new_range)
    return range_list


def get_lowest_location_number_of_the_initial_seeds():
    rows = get_file_rows('input.txt')
    seed_row = rows[0]
    seed_numbers = get_numbers(seed_row)
    not_seeds_part = rows[2:]
    not_seeds_part_list: list[list[str]] = []
    start = 0
    for index, row in enumerate(not_seeds_part):
        if row == '':
            not_seeds_part_list.append(not_seeds_part[start:index])
            start = index + 1  # To exclude the blank lines
    if not_seeds_part[start:len(not_seeds_part)] not in not_seeds_part_list:
        not_seeds_part_list.append(not_seeds_part[start:len(not_seeds_part)])
    range_list = []
    for index, part in enumerate(not_seeds_part_list):
        range_list.insert(index, get_range_list_between_two_objects(part))
    min_location = sys.maxsize
    for seed_number in seed_numbers:
        string_to_print = f'Seed {seed_number}, '
        current_value = seed_number
        for index, current_ranges in enumerate(range_list):
            for current_range in current_ranges:
                if current_range[0] <= current_value < current_range[1]:
                    current_value += current_range[2]
                    break
            if index == 0:
                string_to_print += f'soil {current_value}, '
            elif index == 1:
                string_to_print += f'fertilizer {current_value}, '
            elif index == 2:
                string_to_print += f'water {current_value}, '
            elif index == 3:
                string_to_print += f'light {current_value}, '
            elif index == 4:
                string_to_print += f'temperature {current_value}, '
            elif index == 5:
                string_to_print += f'humidity {current_value}, '
            elif index == 6:
                string_to_print += f'location {current_value}'
        print(string_to_print)
        if min_location > current_value:
            min_location = current_value
    return min_location


if __name__ == '__main__':
    print(f'The lowest location number is {get_lowest_location_number_of_the_initial_seeds()}')

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


# We cannot use the numbers anymore because there are too many to compute
# We use the start and end (excluded) of the range
def get_seeds_range(row: str) -> list[tuple[int, int]]:
    numbers = []
    number = ""
    for char in row:
        if char.isdigit():
            number += char
        else:
            if number != "":
                numbers.append(int(number))
                number = ""
    if number != "":
        numbers.append(int(number))
    seeds_range = []
    for i in range(0, len(numbers), 2):
        seeds_range.append((numbers[i], numbers[i] + numbers[i + 1]))
    return seeds_range


def get_lowest_location_number_of_the_initial_seeds():
    rows = get_file_rows('input.txt')
    seed_row = rows[0]
    seeds_ranges = get_seeds_range(seed_row)
    not_seeds_part = rows[2:]
    not_seeds_part_list: list[list[str]] = []
    start = 0
    for index, row in enumerate(not_seeds_part):
        if row == '':
            not_seeds_part_list.append(not_seeds_part[start:index])
            start = index + 1  # To exclude the blank lines
    if not_seeds_part[start:len(not_seeds_part)] not in not_seeds_part_list:
        not_seeds_part_list.append(not_seeds_part[start:len(not_seeds_part)])
    range_container = []
    for index, part in enumerate(not_seeds_part_list):
        range_container.insert(index, get_range_list_between_two_objects(part))
    locations_ranges = seeds_ranges.copy()
    for range_list in range_container:
        updated_data = []
        # We consider every possible interval
        while len(locations_ranges) != 0:
            start, end = locations_ranges.pop()
            for current_range in range_list:
                overlap_start = max(start, current_range[0])
                overlap_end = min(end, current_range[1])
                # Check if the intersection between the interval and the current range exist
                if overlap_start < overlap_end:
                    # If so we add that to the updated_data
                    updated_data.append((overlap_start + current_range[2], overlap_end + current_range[2]))
                    # We also need to check the possible external data interval,
                    # so if they exist we add them to the location ranges to check in the internal for loop
                    if overlap_start > start:
                        locations_ranges.append((start, overlap_start))
                    if end > overlap_end:
                        locations_ranges.append((overlap_end, end))
                    break
            else:
                updated_data.append((start, end))
        locations_ranges = updated_data

    return min(locations_ranges)[0]


if __name__ == '__main__':
    print(f'The lowest location number is {get_lowest_location_number_of_the_initial_seeds()}')

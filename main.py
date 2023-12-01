def get_calibration_value_of_a_line(line: str) -> int:
    literal_to_number = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                         '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
                         'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    start = 0
    numbers = []
    for position in range(1, len(line) + 1):
        # keys = everything we consider as a valid number
        possible_number = line[start:position]
        if possible_number in literal_to_number.keys():
            numbers.append(literal_to_number[possible_number])
            start = position
        else:
            next_position = start + 1
            while next_position < position:
                possible_number_2 = line[next_position:position]
                if possible_number_2 in literal_to_number.keys():
                    numbers.append(literal_to_number[possible_number_2])
                    start = position
                    break
                next_position += 1
    return numbers[0] * 10 + numbers[-1]


def get_sum_of_all_calibration_values():
    result = 0
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        for line in lines:
            result += get_calibration_value_of_a_line(line)
    return result


if __name__ == '__main__':
    print(f'Sum of all calibration values in the input file: {get_sum_of_all_calibration_values()}')

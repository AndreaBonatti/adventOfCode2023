def get_calibration_value_of_a_line(line: str) -> int:
    first_digit, last_digit = 0, 0
    for position in range(len(line)):
        if line[position].isdigit():
            first_digit = line[position]
            break
    for position in reversed(range(len(line))):
        if line[position].isdigit():
            last_digit = line[position]
            break
    result = int(first_digit) * 10 + int(last_digit)
    return result


def get_sum_of_all_calibration_values():
    result = 0
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        for line in lines:
            result += get_calibration_value_of_a_line(line)
    return result


if __name__ == '__main__':
    print(f'Sum of all calibration values in the input file: ${get_sum_of_all_calibration_values()}')

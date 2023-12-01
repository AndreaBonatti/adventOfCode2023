def get_calibration_value_of_a_line(line: str) -> int:
    valid_numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                     'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero'}
    first_digit, last_digit = -1, -1
    start, end = 0, 0
    for position in range(len(line)):
        end = position
        if line[position].isdigit():
            first_digit = line[position]
            break
        for i in range(start, end):
            if line[i:end + 1] in valid_numbers:
                first_digit = line[i:end + 1]
                break
        if first_digit in valid_numbers:
            break
    start, end = len(line) - 1, len(line) - 1
    for position in reversed(range(len(line))):
        start = position - 1
        if line[position].isdigit():
            last_digit = line[position]
            break
        for i in reversed(range(start + 1, end + 2)):
            if line[start + 1:i] in valid_numbers:
                last_digit = line[start + 1:i]
                break
        if last_digit in valid_numbers:
            break
    literal_to_number = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    if str(first_digit) in literal_to_number.keys():
        first_digit = literal_to_number[str(first_digit)]
    if str(last_digit) in literal_to_number.keys():
        last_digit = literal_to_number[str(last_digit)]
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
    print(f'Sum of all calibration values in the input file: {get_sum_of_all_calibration_values()}')

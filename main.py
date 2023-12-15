def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split(',')


def get_hash_value(word: str) -> int:
    current_value = 0
    for char in word:
        # Determine the ASCII code for the current character of the string.
        ascii_code = ord(char)
        # Increase the current value by the ASCII code you just determined.
        current_value += ascii_code
        # Set the current value to itself multiplied by 17.
        current_value *= 17
        # Set the current value to the remainder of dividing itself by 256.
        current_value %= 256
    return current_value


def get_sum_of_all_hash_values():
    result = 0
    rows = get_file_rows('input.txt')
    for row in rows:
        result += get_hash_value(row)
    return result


if __name__ == '__main__':
    print(f'Part 1: sum = {get_sum_of_all_hash_values()}')

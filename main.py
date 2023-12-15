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


def get_sum_of_all_hash_values() -> int:
    result = 0
    rows = get_file_rows('input.txt')
    for row in rows:
        result += get_hash_value(row)
    return result


def get_focusing_power() -> int:
    result = 0
    rows = get_file_rows('input.txt')
    boxes = [[] for _ in range(256)]
    focal_lengths = {}
    # Hashmap to elaborate all the file data
    for row in rows:
        if '-' in row:
            label = row[:-1]
            box_number = get_hash_value(label)
            if label in boxes[box_number]:
                boxes[box_number].remove(label)
        else:
            label, length = row.split("=")
            length = int(length)

            index = get_hash_value(label)
            if label not in boxes[index]:
                boxes[index].append(label)

            focal_lengths[label] = length
    # Sum of each the focusing power of each lens
    for box_number, box in enumerate(boxes, 1):
        for slot, label in enumerate(box, 1):
            result += box_number * slot * focal_lengths[label]
    return result


if __name__ == '__main__':
    print(f'Part 1: sum = {get_sum_of_all_hash_values()}')
    print(f'Part 2: focusing power = {get_focusing_power()}')

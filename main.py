def is_symbol(max_length: int, max_height: int, x: int, y: int, file: list[str]) -> bool:
    # Out of the matrix bounds
    if not (0 <= x < max_height and 0 <= y < max_length):
        return False
    if file[x][y] != '.' and not file[x][y].isdigit():
        return True


def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split("\n")


def get_sum_of_all_part_numbers():
    rows = get_file_rows('input.txt')
    max_length, max_height = len(rows[0]), len(rows)
    result = 0
    for i, row in enumerate(rows):
        start, current_position = 0, 0
        while current_position < max_length:
            start = current_position
            number = ""
            # Reading the full number
            while current_position < max_length and row[current_position].isdigit():
                number += row[current_position]
                current_position += 1

            if number == "":
                current_position += 1
                continue

            # Now we have a number => check if is valid
            number = int(number)

            # Left/Right
            if (is_symbol(max_length, max_height, i, start - 1, rows)
                    or is_symbol(max_length, max_height, i, current_position, rows)):
                result += number
                continue
            # Top/Bottom
            for j in range(start - 1, current_position + 1):
                if (is_symbol(max_length, max_height, i - 1, j, rows)
                        or is_symbol(max_length, max_height,i + 1, j, rows)):
                    result += number
                    break
    return result


if __name__ == '__main__':
    print(get_sum_of_all_part_numbers())

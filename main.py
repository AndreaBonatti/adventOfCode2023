def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split("\n")


def get_numbers_from_string(numbers_string: str):
    result = []
    number = ""
    for char in numbers_string:
        if char.isdigit():
            number += char
        else:
            if number != "":
                result.append(int(number))
                number = ""
    if number != "":
        result.append(int(number))
    return result


def get_scratchcard_points(scratchcard: str) -> int:
    points = 0
    scratchcard_parts = scratchcard.split(':')
    numbers = scratchcard_parts[1].split('|')
    winning_numbers = get_numbers_from_string(numbers[0])
    played_numbers = get_numbers_from_string(numbers[1])
    exponent = 0
    first = True
    for played_number in played_numbers:
        if played_number in winning_numbers:
            if first:
                first = False
            else:
                exponent += 1
    if not first:
        points = 2 ** exponent
    return points


def get_pile_of_scratchcards_points():
    rows = get_file_rows('input.txt')
    result = 0
    for row in rows:
        result += get_scratchcard_points(row)
    return result


if __name__ == '__main__':
    print(f'The large pile of colorful cards is worth: {get_pile_of_scratchcards_points()} points')

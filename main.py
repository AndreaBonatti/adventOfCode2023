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


def get_total_scratchcards():
    rows = get_file_rows('input.txt')
    cards_dictionary = {}
    max_card_number = len(rows) + 1
    for i in range(1, max_card_number):
        cards_dictionary[i] = 1
    for index, row in enumerate(rows):
        card_number = index + 1
        scratchcard_parts = row.split(':')
        numbers = scratchcard_parts[1].split('|')
        winning_numbers = get_numbers_from_string(numbers[0])
        played_numbers = get_numbers_from_string(numbers[1])
        counter = 0
        for played_number in played_numbers:
            if played_number in winning_numbers:
                counter += 1
        if counter > 0:
            # We do the same operation for the number of the same card that we have
            # e.g. we have 2 cards n°2 => we add 2 times the winning cards from the card°2
            for time in range(0,cards_dictionary[card_number]):
                for i in range(card_number + 1, card_number + 1 + counter):
                    if i < max_card_number:
                        cards_dictionary[i] += 1
    result = 0
    for value in cards_dictionary.values():
        result += value
    return result


if __name__ == '__main__':
    print(f'The large pile of colorful cards is worth: {get_pile_of_scratchcards_points()} points')
    print(f'Total of scratch cards: {get_total_scratchcards()}')

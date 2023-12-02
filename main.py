COLORS = {'red': 12, 'green': 13, 'blue': 14}


# return -1 if the game is not valid else the id of the game
def get_game_id(selected_game: str) -> int:
    start = len(selected_game)
    end = len(selected_game) + 1
    while start >= 0:
        if selected_game[start:end] in COLORS.keys():
            color = selected_game[start:end]
            number = 0
            while not selected_game[start].isdigit():
                start -= 1
            number += int(selected_game[start])
            power_of_ten = 1
            start -= 1
            while selected_game[start].isdigit():
                number += 10 ** power_of_ten * int(selected_game[start])
                power_of_ten += 1
                start -= 1
            # verify if the selected color extraction is valid
            selected = COLORS[color]
            if number > selected:
                return -1
            else:
                while selected_game[start] not in [';', ',']:
                    start -= 1
                    if start == 0:
                        break
                end = start
                start -= 1
                if start == 0:
                    break
        start -= 1
    # The game is valid, and now we search the id of this game
    result = 0
    power_of_ten = 0
    for i in range(0, len(selected_game)):
        if selected_game[i].isdigit():
            result += 10 ** power_of_ten * result + int(selected_game[i])
            power_of_ten += 1
            i += 1
            while selected_game[i].isdigit():
                result = 10 ** power_of_ten * result + int(selected_game[i])
                power_of_ten += 1
                i += 1
            break
    return result


def get_total_valid_games():
    sum_of_valid_ids = 0
    with open('input.txt') as input_file:
        games = input_file.readlines()
        for selected_game in games:
            game_id = get_game_id(selected_game.strip())
            if game_id != -1:
                sum_of_valid_ids += game_id
    return sum_of_valid_ids


if __name__ == '__main__':
    print(f'Valid games number: {get_total_valid_games()}')

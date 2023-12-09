def get_history_value(history: list[int]) -> int:
    if all(value == 0 for value in history):
        return 0
    next_sequence = [b - a for a, b in zip(history, history[1:])]
    difference = get_history_value(next_sequence)
    return history[-1] + difference


def get_sum_of_histories_values() -> int:
    result = 0
    rows = open('input.txt')
    for row in rows:
        history = list(map(int, row.split()))
        result += get_history_value(history)
    return result


def get_history_value_part_2(history: list[int]) -> int:
    if all(value == 0 for value in history):
        return 0
    next_sequence = [b - a for a, b in zip(history, history[1:])]
    difference = get_history_value_part_2(next_sequence)
    return history[0] - difference


def get_sum_of_histories_values_part_2() -> int:
    result = 0
    rows = open('input.txt')
    for row in rows:
        history = list(map(int, row.split()))
        result += get_history_value_part_2(history)
    return result


if __name__ == '__main__':
    print(f'Sum of histories values: {get_sum_of_histories_values()}')
    print(f'Sum of histories values part 2: {get_sum_of_histories_values_part_2()}')

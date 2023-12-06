def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split("\n")


def get_numbers(row: str) -> list[int]:
    result = []
    number = ""
    for char in row:
        if char.isdigit():
            number += char
        else:
            if number != "":
                result.append(int(number))
                number = ""
    if number != "":
        result.append(int(number))
    return result


def get_numbers_of_ways_to_beat_the_record(race: tuple[int, int]) -> int:
    record_time, record_distance = race
    result = 0
    # We need to beat the distance from the record by using a time <= record_time
    for time in range(record_time + 1):
        time_left = record_time - time
        distance = time_left * time
        if distance > record_distance:
            result += 1
    print(f'The record {race} can be beaten in {result} ways.')
    return result


def get_product_of_all_ways_to_beat_every_records():
    data_rows = get_file_rows('input.txt')
    times_row = data_rows[0]
    distances_row = data_rows[1]
    times_values = get_numbers(times_row)
    distance_values = get_numbers(distances_row)
    races = []
    for i in range(len(times_values)):
        races.append((times_values[i], distance_values[i]))
        print(f'Race n°{i + 1} record: time {times_values[i]}ms, distance {distance_values[i]}mm')
    numbers_of_ways_to_beat_records = []
    for race in races:
        numbers_of_ways_to_beat_records.append(get_numbers_of_ways_to_beat_the_record(race))
    product = 1
    for number in numbers_of_ways_to_beat_records:
        product *= number
    print(f'The requested product is {product}')


if __name__ == '__main__':
    get_product_of_all_ways_to_beat_every_records()

class Node:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def get_value(self):
        return self.value

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node


def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split("\n")


def extract_nodes(string: str):
    left_right = ''
    for char in string:
        if char.isalpha():
            left_right += char
    return left_right[:3], left_right[3:]


def get_number_of_minimum_steps_to_reach_the_destination():
    result = 0
    rows = get_file_rows('input.txt')
    steps = [*rows[0]]
    map_rows = rows[2:]
    nodes_map = {}
    for row in map_rows:
        name, left_right = row.split(' = ')
        nodes_map[name] = extract_nodes(left_right)
    current_node = 'AAA'
    same_steps = steps.copy()
    while current_node != 'ZZZ':
        if len(steps) == 0:
            steps += same_steps
        direction = steps.pop(0)
        if direction == 'L':
            current_node = nodes_map[current_node][0]
        elif direction == 'R':
            current_node = nodes_map[current_node][1]
        result += 1
    return result


if __name__ == '__main__':
    print(f'Minimum number of steps to reach ZZZ: {get_number_of_minimum_steps_to_reach_the_destination()}')

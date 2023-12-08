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
        if char.isalnum():
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


def get_initial_nodes(nodes:  dict[str, tuple[str, str]]) -> list[str]:
    initial_nodes = []
    for node, _ in nodes.items():
        if node[2] == 'A':
            initial_nodes.append(node)
    return initial_nodes


def destination_reached(current_nodes: list[str]):
    for node in current_nodes:
        if node[2] != 'Z':
            return False
    return True


# direction is the same for all the nodes: L = left or R = right
def get_next_nodes(current_nodes: list[str], direction: str, node_map:  dict[str, tuple[str, str]]) -> list[str]:
    next_nodes = []
    for node in current_nodes:
        if direction == 'L':
            next_nodes.append(node_map[node][0])
        elif direction == 'R':
            next_nodes.append(node_map[node][1])
    return next_nodes


def get_number_of_minimum_steps_to_reach_the_destination_part_2():
    result = 0
    rows = get_file_rows('input.txt')
    steps = [*rows[0]]
    map_rows = rows[2:]
    nodes_map = {}
    for row in map_rows:
        name, left_right = row.split(' = ')
        nodes_map[name] = extract_nodes(left_right)
    # Fetch the initial nodes (ending with 'A')
    current_nodes = get_initial_nodes(nodes_map)
    same_steps = steps.copy()
    while not destination_reached(current_nodes):
        if len(steps) == 0:
            steps += same_steps
        direction = steps.pop(0)
        current_nodes = get_next_nodes(current_nodes, direction, nodes_map)
        result += 1
    return result


if __name__ == '__main__':
    print(f'Minimum number of steps to reach ZZZ: {get_number_of_minimum_steps_to_reach_the_destination()}')
    print(f'Part 2: minimum number of steps to reach all the nodes that ends with Z: '
          f'{get_number_of_minimum_steps_to_reach_the_destination_part_2()}')

from math import gcd


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


def get_number_of_minimum_steps_to_reach_the_destination_part_2():
    rows = get_file_rows('input.txt')
    steps = rows[0]
    map_rows = rows[2:]
    nodes_map = {}
    for row in map_rows:
        name, left_right = row.split(' = ')
        nodes_map[name] = extract_nodes(left_right)
    # Fetch the initial nodes (ending with 'A')
    initial_nodes = get_initial_nodes(nodes_map)
    # now we look the number of steps for each initial nodes to reach every possible different node that ends with 'Z'
    # at least we aspect to find 2 cycles: A -> Z1 and Z1->Z1.
    # They could be more if there is the chance to reach more Z starting from the same node.
    cycles = []
    for node in initial_nodes:
        cycle = []
        current_steps = steps
        steps_count = 0
        first_z = None
        while True:
            while steps_count == 0 or not node.endswith('Z'):
                steps_count += 1
                direction = current_steps[0]
                node = nodes_map[node][0 if direction == 'L' else 1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(steps_count)
            if first_z is None:
                first_z = node
                steps_count = 0
            elif node == first_z:
                break
        cycles.append(cycle)
    # print(cycles)
    # We always reach Z from every node in the same number of steps A->Z1 = Z1->Z2 = Z2->Z3,...
    # So we consider only the first number of steps for each initial node
    numbers = [cycle[0] for cycle in cycles]
    # We want the least common divisor between every step's number
    least_common_divisor = numbers.pop()
    for number in numbers:
        least_common_divisor = least_common_divisor * number // gcd(least_common_divisor, number)
    return least_common_divisor


if __name__ == '__main__':
    # print(f'Minimum number of steps to reach ZZZ: {get_number_of_minimum_steps_to_reach_the_destination()}')
    print(f'Part 2: minimum number of steps to reach all the nodes that ends with Z: '
          f'{get_number_of_minimum_steps_to_reach_the_destination_part_2()}')

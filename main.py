from collections import deque

from Module import Module

TIMES_BUTTON_IS_PUSHED = 1000


def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().splitlines()


def get_product_of_all_pulses() -> int:
    rows = get_file_rows('input.txt')
    modules = {}
    broadcast_targets = []
    for row in rows:
        left, right = row.strip().split(" -> ")
        outputs = right.split(', ')
        if left == "broadcaster":  # Broadcast
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)
    # Memory initialization
    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "low"
    # print(modules)
    low = high = 0
    for _ in range(TIMES_BUTTON_IS_PUSHED):
        low += 1
        queue = deque([("broadcaster", x, "low") for x in broadcast_targets])

        while queue:
            origin, target, pulse = queue.popleft()

            if pulse == "low":
                low += 1
            else:
                high += 1

            if target not in modules:
                continue

            module = modules[target]

            if module.type == "%":
                if pulse == "low":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "high" if module.memory == "on" else "low"
                    for new_output in module.outputs:
                        queue.append((module.name, new_output, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "low" if all(x == "high" for x in module.memory.values()) else "high"
                for new_output in module.outputs:
                    queue.append((module.name, new_output, outgoing))

    return low * high


if __name__ == '__main__':
    print(f'Part 1 - Product of the total number of low pulses sent by the total number of high pulses sent: '
          f'{get_product_of_all_pulses()}')

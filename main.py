def get_workflows_and_ratings(path):
    with open(path) as file:
        first_block, second_block = file.read().split("\n\n")
        workflows, ratings = first_block.splitlines(), second_block.splitlines()
        return workflows, ratings


def get_sum_rating_numbers_accepted_parts() -> int:
    def item_is_accepted(parts, parts_name="in") -> bool:
        if parts_name == "R":
            return False
        elif parts_name == "A":
            return True
        workflows_rules, fallback = workflows_dictionary[parts_name]
        for k, op, num, t in workflows_rules:
            if op == '>':
                if parts[k] > num:
                    return item_is_accepted(parts, t)
            elif op == '<':
                if parts[k] < num:
                    return item_is_accepted(parts, t)
        return item_is_accepted(parts, fallback)

    workflows, ratings = get_workflows_and_ratings('input.txt')
    workflows_dictionary = {}
    for row in workflows:
        name, rest = row[:-1].split('{')
        rules = rest.split(',')
        workflows_dictionary[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(':')
            key = comparison[0]
            operator = comparison[1]
            number = int(comparison[2:])
            workflows_dictionary[name][0].append((key, operator, number, target))
    result = 0
    for row in ratings:
        item = {}  # contains the x,m,a,s parts
        for segment in row[1:-1].split(','):
            char, number = segment.split('=')
            item[char] = int(number)
        if item_is_accepted(item):
            result += sum(item.values())
    return result


if __name__ == '__main__':
    print(f'Part 1 - Sum of rating number of all accepted parts: {get_sum_rating_numbers_accepted_parts()}')

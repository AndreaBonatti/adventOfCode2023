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


def get_distinct_combinations_accepted() -> int:
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

    def count(ranges, item_name="in"):
        if item_name == "R":
            return 0
        if item_name == "A":
            product = 1
            for lower_number, higher_number in ranges.values():
                product *= higher_number - lower_number + 1
            return product
        workflows_rules, fallback = workflows_dictionary[item_name]
        total = 0
        for k, op, n, t in workflows_rules:
            lower_number, higher_number = ranges[k]
            if op == "<":
                accepted = (lower_number, n - 1)
                not_accepted = (n, higher_number)
            else:
                accepted = (n + 1, higher_number)
                not_accepted = (lower_number, n)
            if accepted[0] <= accepted[1]:
                copy = dict(ranges)
                copy[k] = accepted
                total += count(copy, t)
            if not_accepted[0] <= not_accepted[1]:
                ranges = dict(ranges)
                ranges[k] = not_accepted
            else:
                break
        else:
            total += count(ranges, fallback)
        return total

    return count({key: (1, 4000) for key in "xmas"})


if __name__ == '__main__':
    print(f'Part 1 - Sum of rating number of all accepted parts: {get_sum_rating_numbers_accepted_parts()}')
    print(f'Part 2 - Number of distinct combinations of ratings accepted by the Elves\' workflows: '
          f'{get_distinct_combinations_accepted()}')

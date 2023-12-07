def get_file_rows(path: str) -> list[str]:
    with open(path) as file:
        data = file.read()
        return data.strip().split("\n")


def get_hand_strength(hand: str) -> int:
    # It contains the number of occurrences of every card in the hand
    counts = [hand.count(card) for card in hand]
    if 5 in counts:  # Five of a kind
        return 6
    if 4 in counts:  # Four of a kind
        return 5
    if 3 in counts:
        if 2 in counts:  # Full house
            return 4
        return 3  # Tree of kind
    # Now counts could be 2 2 1 in different order, so we can count the counts of 2
    if counts.count(2) == 4:  # Two pair
        return 2
    if 2 in counts:  # One pair
        return 1
    return 0  # High card


# To map the letters in the card value order, the numbers are already ok
# So we could have 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A (lower to high)
LETTER_MAP = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}


def get_hand_and_bid(row: str) -> tuple[str, int]:
    hand, bid = row.split(' ')
    return hand, int(bid)


# Hands order by the hand strength, if there are some hands with the same strength we order that by the higher card
def get_hands_ordered(hands: list[str]) -> list[tuple[str, int]]:
    hands_ordered = []
    for hand in hands:
        hands_ordered.append(get_hand_and_bid(hand))
    hands_ordered.sort(key=lambda hb: (get_hand_strength(hb[0]), [LETTER_MAP.get(char, char) for char in hb[0]]))
    # print(hands_ordered)
    return hands_ordered


def get_total_winnings() -> int:
    file_rows = get_file_rows('input.txt')
    ordered_hands = get_hands_ordered(file_rows)
    result = 0
    for rank, (hand, bid) in enumerate(ordered_hands, 1):
        result += rank * bid
    return result


def get_hand_strength_part_2(hand: str) -> int:
    cards_counter = {}
    for char in hand:
        if char in cards_counter.keys():
            cards_counter[char] += 1
        else:
            cards_counter[char] = 1
    # Limit case where the hand is made by only Joker card => the weakest 'five of a kind' hand
    if hand == 'JJJJJ':
        return 6
    # Transform the J in the most common card because is a Joker in the part 2
    joker = 'J'
    if joker in cards_counter.keys():
        to_replace = '?'
        to_replace_count = 0
        for card, count in cards_counter.items():
            if card != joker:
                if count > to_replace_count:
                    to_replace = card
                    to_replace_count = count
        cards_counter[to_replace] += cards_counter[joker]
        cards_counter.pop(joker)

    # It contains the number of occurrences of every card in the hand
    counts = cards_counter.values()
    if 5 in counts:  # Five of a kind
        return 6
    if 4 in counts:  # Four of a kind
        return 5
    if 3 in counts:
        if 2 in counts:  # Full house
            return 4
        return 3  # Tree of kind
    # Now counts could be 2 2 1 in different order, so we can count the counts of 2
    if 2 in counts:
        if len(counts) == 3:  # Two pair
            return 2
        return 1  # One pair
    return 0  # High card


# J is the weakest letter
LETTER_MAP_PART_2 = {'J': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G',
                     '8': 'H', '9': 'I', 'T': 'J', 'Q': 'K', 'K': 'L', 'A': 'M'}


# Hands order by the hand strength, if there are some hands with the same strength we order that by the higher card
def get_hands_ordered_part_2(hands: list[str]) -> list[tuple[str, int]]:
    hands_ordered = []
    for hand in hands:
        hands_ordered.append(get_hand_and_bid(hand))
    hands_ordered.sort(
        key=lambda hb: (get_hand_strength_part_2(hb[0]), [LETTER_MAP_PART_2.get(char, char) for char in hb[0]]))
    # print(hands_ordered)
    return hands_ordered


def get_total_winnings_part_2() -> int:
    file_rows = get_file_rows('input.txt')
    ordered_hands = get_hands_ordered_part_2(file_rows)
    result = 0
    for rank, (hand, bid) in enumerate(ordered_hands, 1):
        result += rank * bid
    return result


if __name__ == '__main__':
    print(f'Total winnings: {get_total_winnings()}')
    print(f'Total winnings part 2: {get_total_winnings_part_2()}')

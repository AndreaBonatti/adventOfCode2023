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


if __name__ == '__main__':
    print(f'Total winnings: {get_total_winnings()}')

import random
# Implementing Card class
class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.ranks[self.rank]}{Card.suits[self.suit]}"

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank


# Implementing Deck class
class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)


# Implementing  Hand class
class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])

    def get_label(self):
        return self.label

    def get_win_count(self):
        return self.win_count

    def round_winner(self):
        self.win_count = self.win_count + 1


# Simple game

deck = Deck()
hands = []
for i in range(1, 5):
    hands.append(Hand(f'P{i}'))

while len(deck) > 0:
    for hand in hands:
        hand.add_card(deck.pop_card())

print(hands[0])
for i in range(13):
    input()
    played_cards = []
    for hand in hands:
        played_cards.append(hand.pop_card())

    win_card = max(played_cards)
    win_hand = hands[played_cards.index(win_card)]
    win_hand.round_winner()

    print(f"R{i}: " + ' '.join(

        [str(card) for card in played_cards]) + f' Winner: {win_hand.get_label()} {str(win_card)}')

for hand in hands:
    print(f"Score for {hand.get_label()}: {hand.get_win_count()}")


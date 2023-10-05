import random


def deck():
    """Return a list of 52-card deck."""
    suits = '◆♥♠♣'
    digits = [str(number) for number in range(2, 11)]
    specials = 'AKQJ'
    special_cards = [special + suit for special in specials for suit in suits]
    numbered_cards = [number + suit for number in digits for suit in suits]
    cards = special_cards + numbered_cards
    return cards


def get_winner(card1, card2):
    """Determine winner and return 1 or 2 or 0 for a tie."""
    suit_ranks = {'♣': 1, '◆': 2, '♥': 3, '♠': 4}
    special_ranks = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    if card1 == card2:
        return 0
    if card1[0].isdecimal() and card2[0].isalpha():
        return 2
    if card1[0].isalpha() and card2[0].isdecimal():
        return 1
    if card1[0].isdecimal() and card2[0].isdecimal():
        if int(card1[0]) > int(card2[0]):
            return 1
        if int(card1[0]) < int(card2[0]):
            return 2
    if card1[0].isalpha() and card2[0].isalpha():
        if special_ranks[card1[0]] > special_ranks[card2[0]]:
            return 1
        if special_ranks[card1[0]] < special_ranks[card2[0]]:
            return 2
    if card1[-1] != card2[-1] and card1[:-1] == card2[:-1]:
        if suit_ranks[card1[-1]] > suit_ranks[card2[-1]]:
            return 1
        if suit_ranks[card1[-1]] < suit_ranks[card2[-1]]:
            return 2


def play_game():
    """Display rounds interactively and results at the end."""
    cards = deck()
    rounds = input('Enter the number of rounds to play: ')
    while not rounds.isdecimal():
        print('Invalid rounds number')
        rounds = input('Enter the number of rounds to play: ')
    games_played = 0
    p1_score, p2_score = 0, 0
    while games_played < int(rounds):
        confirm_round = input(f'Press enter to display round {games_played} or q to exit: ')
        while confirm_round and confirm_round != 'q':
            confirm_round = input(f'Press enter to display round {games_played} or q to exit: ')
        if confirm_round == 'q':
            print('Thank you for playing cards.')
            print(30 * '=')
            exit(0)
        player1_card = random.choice(cards)
        player2_card = random.choice(cards)
        print(f'player 1 card: {player1_card}')
        print(f'player 2 card: {player2_card}')
        winner = get_winner(player1_card, player2_card)
        if winner == 0:
            print('Tie!')
        if winner == 1:
            print('Player 1 wins.')
            p1_score += 1
        if winner == 2:
            print('Player 2 wins.')
            p2_score += 1
        games_played += 1
        print(30 * '=', '\n')
    print(30 * '=')
    print(f'Total rounds played: {games_played}')
    print(f'Player 1 {p1_score}-{p2_score} player 2')
    if p1_score > p2_score:
        print(f'Winner is Player 1 ({p1_score} out of {games_played} games played)')
    if p2_score > p1_score:
        print(f'Winner is Player 2 ({p2_score} out of {games_played} games played)')
    if p1_score == p2_score:
        print('TIE!!!')


if __name__ == '__main__':
    play_game()

# Krish Dhansinghani

def card_to_value(card):
    """
      Function gives the value of the card for each input of a card number or letter
     :param card: input a string of the type of card
     :return: the value of the card as an int
     """
    if "A" == card:
        return 1
    elif card == "K" or card == "Q" or card == "J" or card == "T":
        return 10
    else:
        return int(card)

def hard_score(hand):
    """
    Takes three characters that are input and calculates the total value of the hand
    :param hand: A string of characters that match card value
    :return: the sum of all characters and their corresponding value
    """
    value = 0
    for card in hand:
        value += card_to_value(card)
    return value

def soft_score(hand):
    """
    Takes three characters, but returns Ace as 11 if input as the first number
    :param hand: A string of characters that match card value
    :return: the sum of all characters and their corresponding values, but returns 11 instead of 1 for ace if A if the first character
    """
    value = 0
    if hand[0] == "A":
        value = 10
    elif hand[1] == "A":
        value = 10
    for card in hand:
        value += card_to_value(card)
    return value

import random

def shuffle_deck(decksNumber = 1):
	tempDeck = ['2:H', '3:H', '4:H', '5:H', '6:H', '7:H', '8:H', '9:H', '10:H', 'J:H', 'Q:H', 'K:H', 'A:H', 
				'2:S', '3:S', '4:S', '5:S', '6:S', '7:S', '8:S', '9:S', '10:S', 'J:S', 'Q:S', 'K:S', 'A:S', 
				'2:C', '2:C', '4:C', '5:C', '6:C', '7:C', '8:C', '9:C', '10:C', 'J:C', 'Q:S', 'K:C', 'A:C', 
				'2:D', '2:D', '4:D', '5:D', '6:D', '7:D', '8:D', '9:D', '10:D', 'J:D', 'Q:H', 'K:D', 'A:D']
	unshuffleDeck = []
	shuffleDeck = []

	for j in range(decksNumber):
		for i in range(52):
			unshuffleDeck.append(tempDeck[i])
	
	for i in range(len(unshuffleDeck)):
		num = random.randint(1, len(unshuffleDeck))
		shuffleDeck.append(unshuffleDeck.pop(num - 1))

	return shuffleDeck

def deal_card(deck):
	card = deck.pop(0)
	return card, deck

def deal_hands(deck, players = 1):
	dealerHand = []
	playerHands = []
	
	for j in range(2):
		dealerHand.append(deck.pop(0))
		for i in range(players):
			playerHands.append([])
			playerHands[i].append(deck.pop(0))

	return dealerHand, playerHands

def hit(hand, deck):
	card, deck = deal_card(deck)
	hand.append(card)
	return hand, deck

def calc_soft_hand(hand):
	value = 0
	for i in range(len(hand)):
		num = hand[i].split(":")[0]
		match num:
			case "J":
				value += 10
			case "Q":
				value += 10
			case "K":
				value += 10
			case "A":
				value += 1
			case _:
				value += int(num)
	return value

def calc_hard_hand(hand):
	value = 0
	for i in range(len(hand)):
		num = hand[i].split(":")[0]
		match num:
			case "J":
				value += 10
			case "Q":
				value += 10
			case "K":
				value += 10
			case "A":
				value += 11
			case _:
				value += int(num)
	return value


def calc_hand_value(hand):
	return [calc_soft_hand(hand), calc_hard_hand(hand)]









deck = shuffle_deck()

dealerHand, playerHands = deal_hands(deck, 2)

playerHands[0], deck = hit(playerHands[0], deck)

value = calc_hand_value(playerHands[0])

#print(", ".join(dealerHand))
print(", ".join(playerHands[0]))
#print(", ".join(playerHands[1]))
print(value)
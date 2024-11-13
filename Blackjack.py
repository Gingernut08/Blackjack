import random, time

def shuffle_deck(decksNumber = 1):
	tempDeck = ['2:H', '3:H', '4:H', '5:H', '6:H', '7:H', '8:H', '9:H', '10:H', 'J:H', 'Q:H', 'K:H', 'A:H', 
				'2:S', '3:S', '4:S', '5:S', '6:S', '7:S', '8:S', '9:S', '10:S', 'J:S', 'Q:S', 'K:S', 'A:S', 
				'2:C', '2:C', '4:C', '5:C', '6:C', '7:C', '8:C', '9:C', '10:C', 'J:C', 'Q:S', 'K:C', 'A:C', 
				'2:D', '2:D', '4:D', '5:D', '6:D', '7:D', '8:D', '9:D', '10:D', 'J:D', 'Q:D', 'K:D', 'A:D']
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
		for i in range(players):
			playerHands.append([])
			playerHands[i].append(deck.pop(0))
		dealerHand.append(deck.pop(0))


	return dealerHand, playerHands

def hit(hand, deck):
	card, deck = deal_card(deck)
	hand.append(card)
	return hand, deck

def calc_soft_hand(hand):
	value = 0
	for i in range(len(hand)):
		num = (hand[i].split(":"))[0]
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

def check_value(hand):
	value = calc_hand_value(hand)
	if value[0] > 21:
		return True, value[1]
	else:
		if value[1] > 21:
			return False, value[0] 
		else:
			return False, value[1]

def check_bust(hand):
	value = calc_hand_value(hand)
	if value[0] > 21:
		return True, "Bust"
	else:
		if value[1] > 21:
			return False, value[0] 
		else:
			return False, value[1]

def player_choice(hand, deck):
	action = input("Stand (s), Hit (h), Double Down (d)")
	match action:
		case "s":
			return hand, deck, "s"
		case "h":
			hand, deck, = hit(hand, deck)
			return hand, deck, "h"
		case "d":
			hand, deck = hit(hand, deck)
			return hand, deck, "d"
		case _:
			hand, deck = player_choice(hand, deck)
			return hand, deck

def setup(numPlayers = 1, decks = None):
	deck = shuffle_deck(decks)
	dealerHand, playerHands = deal_hands(deck, numPlayers)
	playerRecentChoice = []

	while len(playerHands) > numPlayers:
		playerHands.pop(len(playerHands) - 1)

	while len(playerRecentChoice) < numPlayers:
		playerRecentChoice.append("")

	shownDealerHand = [dealerHand[0]]

	return deck, dealerHand, shownDealerHand, playerHands, playerRecentChoice

def display_hands(playerHands, dealerHand = None):
	for i in range(100):
		print()
	if bool(dealerHand) == True:
		print("Dealer")
		print(", ".join(dealerHand))
		print("Total:", check_bust(dealerHand)[1])
		print()
	for i in range(len(playerHands)):
		print("Player", (i + 1))
		print(", ".join(playerHands[i]))
		print("Total:", check_bust(playerHands[i])[1])
		print()

def dealer_play(dealerHand, deck):
	while check_value(dealerHand)[1] < 17:
		for i in range(100):
			print()
		print("Dealer")
		print(", ".join(dealerHand))
		print("Total:", check_bust(dealerHand)[1])
		
		hit(dealerHand, deck)
		time.sleep(2)

	return dealerHand, deck

def main(deck, dealerHand, shownDealerHand, playerHands, playerRecentChoice, players):
	while True:
		for i in range(players):
			while check_bust(playerHands[i])[0] == False and playerRecentChoice[i] != "s":
				display_hands(playerHands, shownDealerHand)
				print("Player", (i + 1))
				playerHands[i], deck, playerRecentChoice[i] = player_choice(playerHands[i], deck)


		dealerHand, deck = dealer_play(dealerHand, deck)





	
		display_hands(playerHands, dealerHand)

		time.sleep(5)


		dealerHand, playerHands = deal_hands(deck, players)
		playerRecentChoice = []

		while len(playerHands) > players:
			playerHands.pop(len(playerHands) - 1)


		while len(playerRecentChoice) < players:
			playerRecentChoice.append("")

		shownDealerHand = [dealerHand[0]]




players = 1
decks = 1

deck, dealerHand, shownDealerHand, playerHands, playerRecentChoice = setup(players, decks)

main(deck, dealerHand, shownDealerHand, playerHands, playerRecentChoice, players)
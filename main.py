import random 

user = input("What is your username?\n")

print(f"Welcome {user}!")

# Starting balance
balance = 100

print(f"Your balance is ${balance}!")

# Empty color variables
color = [""]

# Roulette wheel colors
rouletteWheel = ["green"] + ["black", "red"] *7

# Coin sides
coin_sides = ["Heads", "Tails"]

# Roulette payouts  
numberPayout = 14
colorPayouts = {
    'green' : 14,
    'red' : 2,
    'black' : 2,
}

# Card values
card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

# Card deck
card_deck = list(card_values.keys())


while True:
    playIn = input(f"What do you want to do {user}?\n1. Roulette\n2. Blackjack\n3. Coinflip\n4. Balance\n")
    if playIn == "1":
        print("Roulette\n")
        # Generate random roulette number
        rouletteNumber = random.randint(0,14)

        # Place a bet
        bet = int(input("How much do you want to bet?\n"))
        if balance < bet:
            print("Sorry, you have insufficient funds.")
            continue
        balance -= bet

        # Check if the player wants to bet on a number        
        numberSel = input("Do you want to bet on a number (y/[n]\n")
        if numberSel.lower() == "y":
            number = input("What number do you want to bet on? \n")
            if number == rouletteNumber:
                print("You won!")
                balance += bet * numberPayout
            else:
                print(f"You lost ${bet}\n")
        else:
            # Player wants to bet on color
            color = input("What color do you want to bet on (black, red, green)?\n")
            if color.lower() == rouletteWheel[rouletteNumber]:
                print("You won!")
                balance += bet * colorPayouts[color.lower()]
            else: 
                print(f"You lost ${bet}\n")

        print(f"Roulette landed on {rouletteWheel[rouletteNumber]} {rouletteNumber} !\n")

    elif playIn == "2":
        print("Blackjack\n")
        # Place a bet
        bet = int(input("How much do you want to bet?\n"))
        if balance < bet:
            print("Sorry, you have insufficient funds.")
            continue

        # Deal initial cards
        player_hand = random.sample(card_deck, 2)
        dealer_hand = random.sample(card_deck, 2)

        print(f"\nPlayer's Hand: {', '.join(player_hand)}")
        print(f"Dealer's Hand: {dealer_hand[0]}, Hidden")

        # Helper function to calculate hand value
        def calculate_hand_value(hand):
            value = sum(card_values[card] for card in hand)
            if 'Ace' in hand and value <= 11:
                value += 10
            return value

        # Player's turn
        while True:
            action = input("\nDo you want to Hit or Stand? (h/s)\n")
            if action.lower() == 'h':
                new_card = random.choice(card_deck)
                player_hand.append(new_card)
                print(f"\nPlayer drew {new_card}")
                print(f"Player's Hand: {', '.join(player_hand)}")
                if calculate_hand_value(player_hand) > 21:
                    print("Bust! You lose.")
                    balance -= bet
                    break
            elif action.lower() == 's':
                break

        # Dealer's turn
        if calculate_hand_value(player_hand) <= 21:
            print("\nDealer's turn:")
            print(f"Dealer's Hand: {', '.join(dealer_hand)}")
            while calculate_hand_value(dealer_hand) < 17:
                new_card = random.choice(card_deck)
                dealer_hand.append(new_card)
                print(f"Dealer drew {new_card}")
                print(f"Dealer's Hand: {', '.join(dealer_hand)}")
                if calculate_hand_value(dealer_hand) > 21:
                    print("Dealer busts! You win.")
                    balance += bet
                    break

        # Compare hands and determine the winner
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        if player_value <= 21 and dealer_value <= 21:
            if player_value > dealer_value:
                print("You win!")
                balance += bet
    elif playIn == "3":
        print("Coinflip\n")
        bet = int(input("How much do you want to bet?\n"))
        if balance < bet:
            print("Sorry, you have insufficient funds.")
            continue

        # Flip the coin
        coin_result = random.choice(coin_sides)
        print("Flipping the coin...")
        print(f"The coin landed on {coin_result}!")

        # Determine the winner
        if coin_result == "Heads":
            winner = "Heads"
        else:
            winner = "Tails"

        if coin_result == winner:
            print("Congratulations! You won!")
            balance += bet
        else:
            print("Oops! You lost.")
            balance -= bet
    elif playIn == "4":
        print(f"Your balance is ${balance}\n")
    else:
        print("Invalid input\n")


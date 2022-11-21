import random 

user = input("What is your username?\n")

print(f"Welcome {user}!")

balance = 100
color = [""]
rouletteWheel = ["green"] + ["black", "red"] *7

numberPayout = 14
colorPayouts = {
    'green' : 14,
    'red' : 2,
    'black' : 2,
}

while True:
    playIn = input(f"What do you want to do {user}?\n1. Roulette\n2. Blackjack\n3. Coinflip\n4. Balance\n")
    if playIn == "1":
        print("Roulette\n")
        rouletteNumber = random.randint(0,14)
        bet = int(input("How much do you want to bet?\n"))
        if balance < bet:
            print("Sorry, you have insufficient funds.")
            continue
        balance -= bet
        numberSel = input("Do you want to bet on a number (y/[n]\n")
        if numberSel.lower() == "y":
            number = input("What number do you want to bet on? \n")
            if number == rouletteNumber:
                print("You won!")
                balance += bet * numberPayout
            else:
                print(f"You lost ${bet}\n")
        else:
            color = input("What color do you want to bet on (black, red, green)?\n")
            if color.lower() == rouletteWheel[rouletteNumber]:
                print("You won!")
                balance += bet * colorPayouts[color.lower()]
            else: 
                print(f"You lost ${bet}\n")

        print(f"Roulette landed on {rouletteWheel[rouletteNumber]} {rouletteNumber} !\n")

    elif playIn == "2":
        print("Blackjack\n")
    elif playIn == "3":
        print("Coinflip\n")
    elif playIn == "4":
        print(f"Your balance is ${balance}\n")
    else:
        print("Invalid input\n")


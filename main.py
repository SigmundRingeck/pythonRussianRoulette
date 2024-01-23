import random

print(f"\nWelcome to Russian Roulette!")
print(f"The most diabolical game ever invented.")
print(f"\nGood Luck!, you are going to need it!")
print(f"and if you lose, you wont know anyways!")
print(f"\nBecause you will be DEAD!\n")

def player_login():
    player_info = {}
    player_count = 2
    for i in range(1, player_count+1):
        name = input(f"What is player {i}'s name?")
        player_info[i] = name
    return player_info

def revolver(wheel, bullet_choice):
    if random.choice(wheel) == bullet_choice:
        print(f"Great Job! You blew your brains out moron!")
        return True, wheel
    else:
        print(f"You got lucky!")
        safe_chamber = random.choice([chamber for chamber in wheel if chamber != bullet_choice])
        wheel.remove(safe_chamber)
        return False, wheel

def main():
    wheel = [1, 2, 3, 4, 5, 6]
    bullet_choice = random.choice(wheel)
    player_info = player_login()
    round = 0

    while True:
        for i in range(1, len(player_info) + 1):
            print(f"\nIt is {player_info[i]}'s turn!")
            input(f"Press enter to pull the trigger.")
            game_over, wheel = revolver(wheel, bullet_choice)
            if game_over:
                other_player = 2 if i == 1 else 1
                print(f"\n{player_info[other_player]} won!")
                return
        round += 1

main()






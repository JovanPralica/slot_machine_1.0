import time
import random
from pynput import keyboard
import sys

emoji_list = ['🍒', '🍋', '🔔', '🍊', '⭐', '🍇','🚀']

win_dictionary = {1:"WIN",
                  2:"DOUBLE WIN",
                  3:"TRIPPLE WIN",
                  4:"QUADRA WIN",
                  5:"PENTA WIN",
                  6:"H E X A WIN J A C K P O T"}

special_dictionary = {'🍒':"🍒 Cherry BONUS 🍒",
                      '🚀':"🚀 Rocket BONUS 🚀"}

balance_options = [5,10,25,100,250]
bet_options = [0.5,1,2.5,5,10]

stop_loop = False

print("Welcome to Slot Machine 1.0\n\nPlease enter your balance and bet ammount\nPress SPACE for BET\nPress W for WITHDRAW\nGood Luck!\n")

balance = int(input("Please enter deposit (5,10,25,100,250): "))
bet = float(input("Enter bet(0.5,1,2.5,5,10): "))

while True:
    
    if balance not in balance_options:
        print("Please enter only avaliable deposits: ")

        balance = int(input("Please enter deposit (5,10,25,100,250): "))
    
    elif bet not in bet_options:
        print("Please enter only avaliable bets: ")

        bet = float(input("Enter bet(0.5,1,2.5,5,10): "))
        
    else:
        break

def on_press(key):
    global stop_loop
    if key == keyboard.Key.space:
        stop_loop = True
        return False  

listener = keyboard.Listener(on_press=on_press)
listener.start()

def rotation_animation():

    global balance
    global bet
    
    delay = 0.1
    count = 0

    win_count = 0
    special_count_horizontal = []
    special_count_vertical = []

    while not stop_loop:
        
        grid = [[random.choice(emoji_list) for _ in range(3)] for _ in range(3)]

        print("\033[H\033[J", end="")
        print("🎰💎🍀  SLOT MACHINE 1.0  🎰💎🍀\n\n")

        for row in grid:
            print("          " + "  ".join(row))
  
        time.sleep(delay)

    for i in range(11):  
        grid = [[random.choice(emoji_list) for _ in range(3)] for _ in range(3)]
        
        print("\033[H\033[J", end="")
        print("🎰💎🍀  SLOT MACHINE 1.0  🎰💎🍀\n\n")

        for row in grid:
            print("          " + "  ".join(row) )

        time.sleep(delay)
        delay *= 1.2  

    grid = [[random.choice(emoji_list) for _ in range(3)] for _ in range(3)]

    print("\033[H\033[J", end="")
    print("🎰💎🍀  SLOT MACHINE 1.0  🎰💎🍀\n\n")

    for row in grid:
        print("          " + "  ".join(row))
        
        if len(set(row)) == 1 and set(row) == {'🚀'}:
            
            balance += bet * 4
            special_count_horizontal.append(next(iter(set(row))))
        
        elif len(set(row)) == 1 and set(row) == {'🍒'}:
            
            balance += bet * 4
            special_count_horizontal.append(next(iter(set(row))))
        
        elif len(set(row)) == 1:
            balance += bet * 2
            win_count += 1

        elif len(set(row)) != 1:
            continue
    
    for i in range(3):
    
        if grid[0][count] == grid[1][count] and grid[0][count] == grid[2][count] and grid[1][count] == grid[2][count]:
            
            if grid[0][count] == '🍒' or grid[0][count] == '🚀':
                special_count_vertical.append(grid[0][count])

            balance += bet * 2
            count += 1
            win_count += 1
            continue
    
        else:
            count += 1
            continue 

    if len(special_count_vertical) != 0 and len(special_count_horizontal) != 0:
        
        for i in range(len(special_count_horizontal)):
            print(f'\n       {special_dictionary.get(special_count_horizontal[i])}')
        
        for i in range(len(special_count_vertical)):
            print(f'\n       {special_dictionary.get(special_count_vertical[i])}')
        
        print(f'\n         Balance:[{balance}]')

    
    elif len(special_count_horizontal) != 0:

        for i in range(len(special_count_horizontal)):
            print(f'\n       {special_dictionary.get(special_count_horizontal[i])}')
        
        print(f'\n         Balance:[{balance}]')
    
    elif len(special_count_vertical) != 0:

        for i in range(len(special_count_vertical)):
            print(f'\n      {special_dictionary.get(special_count_vertical[i])}')
        
        print(f'\n         Balance:[{balance}]')
    
    elif win_count > 0 and win_count <= 2:
        print(f'\n       Balance:[{balance}] [{win_dictionary.get(win_count)}]')

    elif win_count >= 3:
        balance += 8 * win_count
        print(f'\n       Balance:[{balance}] [{win_dictionary.get(win_count)}]')
    
    else:
        balance -= bet
        print(f'\n       More luck next time!')
        print(f'\n         Balance:[{balance}]')


    if balance <= 0:
        print("\n       You ran out of Ca$h")
        sys.exit()
    
    else:
        print(f'\n(W / SPACE) Withdraw / Bet: ')

rotation_animation()

def on_press(key):
    
    try:
        if key == keyboard.Key.space:
            rotation_animation()
    
    except AttributeError:
        pass  

def on_release(key):
    
    try:
        if key.char == 'w':
            print("\nThank you for playing! Withdraw complete!")
            print(f'\nYour balance is {balance}')
            return False
        
    except AttributeError:
        pass

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


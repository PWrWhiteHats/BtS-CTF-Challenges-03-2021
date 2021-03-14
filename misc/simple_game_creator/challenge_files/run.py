#!/usr/bin/env python2
import os, sys
from games import Singleplayer, Multiplayer

games = {
    'single': list(),
    'multi': list()
}
	
def user_choice():
    menu = """
    Welcome to Simple Game Creator where you can create your game of choice!

    1. View all games
    2. Create your own multiplayer game
    3. Create your own singleplayer game
    4. DEBUG //Added by Arqsz, remember to remove it before deploy
    """
    print(menu)

    sys.stdout.write("Choose wisely >> ")
    sys.stdout.flush()
    return sys.stdin.readline()

# TODO remember to remove this piece of code - just need it for debbuging. After cleanup remember to sanitize input from users
def debug():
    print("Loaded files:")
    with open('/home/ctf/games.py', 'r') as f:
        sys.stdout.write(f.read())
        sys.stdout.flush()
    with open(__file__, 'r') as f:
        sys.stdout.write(f.read())
        sys.stdout.flush()

def add_single():
    sys.stdout.write("Name your own singleplayer game >> ")
    sys.stdout.flush()
    name = sys.stdin.readline().strip()
    sys.stdout.write("What difficulty will it have (hard, easy)? >> ")
    sys.stdout.flush()
    diff = sys.stdin.readline().strip()

    games['single'].append(Singleplayer(name, diff))

    print("You created your own singleplayer game")

def add_multi():
    sys.stdout.write("Name your own multiplayer game >> ")
    sys.stdout.flush()
    name = sys.stdin.readline().strip()
    sys.stdout.write("What difficulty will it have (hard, easy)? >> ")
    sys.stdout.flush()
    diff = sys.stdin.readline().strip()
    sys.stdout.write("How many players can play this? >> ")
    sys.stdout.flush()
    players = sys.stdin.readline().strip()

    games['multi'].append(Multiplayer(name, diff, players))

    print("You created your own multiplayer game")
	
def show_games():
    print("\nYour games: ")
    print("\nSingleplayers: ")
    for single in games['single']:
        single.show_details()
    print("\nMultiplayers: ")
    for multi in games['multi']:
        multi.show_details()
    print("")

def main():
    banner = """\

 _____ _____  _____                _             
/  ___|  __ \/  __ \              | |            
\ `--.| |  \/| /  \/_ __ ___  __ _| |_ ___  _ __ 
 `--. \ | __ | |   | '__/ _ \/ _` | __/ _ \| '__|
/\__/ / |_\ \| \__/\ | |  __/ (_| | || (_) | |   
\____/ \____/ \____/_|  \___|\__,_|\__\___/|_|   
                                                 
    """

    while True:
        print(banner)
        sys.stdout.flush()
        choice = user_choice().strip()
        choices = {
            '1': show_games,
            '2': add_multi,
            '3': add_single,
            '4': debug
        }
        ans = choices.get(choice, None)
        if not ans:
            print("There is no such option mate")
        else:
            ans()

if __name__ == "__main__":
    main()
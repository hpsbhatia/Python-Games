import random
list_var = ["R", "P", "S"]
p2 = random.choice(list_var)
p = input("Enter your Name\n")
while True:
    p1 = input('''%s, Pick any one:
                   R for ROCK
                   P for PAPER
                   S for SCISSOR\n''' % p)
    if p1 == "R" or p1 == "S" or p1 == "P":
        print(p2)
        if p1 != p2:
            if p1 == "R" and p2 == "S":
                print("!!! You Win !!!")
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            elif p1 == "S" and p2 == 'P':
                print("!!! You Win !!!")
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            elif p1 == 'P' and p2 == 'R':
                print("!!! You Win !!!")
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            else:
                print("!!! You Lose !!!")
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
        else:
            print("It's a Tie !!")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
                break
    else:
        print("You need to learn the game kiddo. !! Enter the VALID input !! ")
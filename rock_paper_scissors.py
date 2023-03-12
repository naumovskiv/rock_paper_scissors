import random

def winning(user,comp):
    if user=='rock' and comp=='scissors':
        return True
    elif user=='paper' and comp=='rock':
        return True
    elif user=='scissors' and comp=='paper':
        return True
    else:
        return False
    
def rockpaperscissors():
    options=['rock','paper','scissors']
    userpick=''
    replay='y'
    while replay=="y":
        print("Game on!")
        computerpick = random.choice(options)
        userpick=input("3...2...1...Shoot!: ")
        print(f"Computer draws {computerpick}")
        if computerpick==userpick:
            print("Its a draw!")
        elif winning(userpick,computerpick)==True:
            print("User wins!")
        else:
            print("Computer wins!")
        replay=input("Replay? y or n: ")

rockpaperscissors()

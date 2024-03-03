#KÁMEN MŮŽKY PAPÍR HRA!!!
import random #vložení knihovny random
while True:
    print("Ahoj, zahrajeme si hru!") #uvítací zpráva
    user_action = input("Vyber si mezi kamenem, nůžkami a papírem ") #musíš si vybrat mezi možnostmi
    possible_actions = ["kámen", "nůžky", "papír"] #možnosti výběru
    computer_action = random.choice(possible_actions) #náhodný výběr počítače
    print(f"\nvybíráš {user_action}, počítač vybírá {computer_action} \n") 

    if computer_action == user_action:#podmínka pro remízu
        print("REMÍZOVAL JSI!")

    elif  user_action == "kámen": #podmínka pro kámen a nůžky
        if computer_action == "nůžky":
            print("VYHRÁL JSI!")
        else:
            print("PROHRÁL JSI!")

    elif user_action == "papír": #podmínka pro papír a kámen
        if computer_action == "kámen":
            print("VYHRÁL JSI!")
        else:
            print("PROHRÁL JSI!")

    elif user_action == "nůžky": #podmínka pro nůžky a papír
        if computer_action == "papír":
            print("VYHRÁL JSI!")
        else:
            print("PROHRÁL JSI!")

    play_again = input("Chceě hrát znovu? (a/n: ")
    if play_again.lower() != "a":
        break
#ende

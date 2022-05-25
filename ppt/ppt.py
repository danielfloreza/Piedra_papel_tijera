import random
def show(result):
    if result is False:
        print("¡Empate!\n")
        run()
    else:
        if result==str(1):
            result = "Piedra.\n"
        if result== str(2):
            result = "Papel.\n"
        if result == str(3) :
            result = "Tijeras.\n"

        print("Ganó quien saco: "+str(result))
        run()
    

def play(option_computer_r,option_user_r):
    print("Yo escogí: "+str(option_computer_r))
    print("Tu escogiste: "+str(option_user_r))
    win_rock_computer=[str(1),str(3)]
    win_rock_user=[str(3),str(1)]
    win_paper_computer=[str(2),str(1)]
    win_paper_user=[str(1),str(2)]
    win_scissors_computer=[str(3),str(2)]
    win_scissors_user=[str(2),str(3)]
    every_options_computer=[win_rock_computer,win_paper_computer,win_scissors_computer]
    every_options_user=[win_rock_user,win_paper_user,win_scissors_user]
    winner=False
    
    result=[str(option_computer_r),str(option_user_r)]
    for option in every_options_computer:
        if result== option:
            winner=option[0]
    for option in every_options_user:
        if result==option:
            winner=option[1]
    return winner


def option_user():
    option_user_r=input("""Ya generé aleatoriamente mi jugada.
Escoge la tuya.

1- piedra
2- papel
3- tijeras

: """)

    option_user_r=option_user_r.strip()
    if option_user_r != str(1) and option_user_r != str(2) and option_user_r != str(3):
        print("Escoge una opcion valida.\n")
        option_user()
    else:
        return option_user_r        
        
    
def option_computer():
    option_computer_r= random.randint(1,3)
    return option_computer_r


def start():
    option_computer_r=option_computer()
    option_user_r=option_user()
    result=play(option_computer_r,option_user_r)
    show(result)


def run():
    answer=input("""Quieres continuar con el juego?
                 1- Si
                 2- No
                 """)
    answer=answer.strip()
    if answer != str(1) and answer != str(2):
        print("Escoge una opcion valida.\n")
        run()
    else:
        if answer == str(1):
            print("\n")
            start()
        else:
            print("Hasta la próxima.\n")


if __name__ == '__main__':
    print("Bienvenido a PIEDRA, PAPEL O TIJERAS\n=============================")
    run()
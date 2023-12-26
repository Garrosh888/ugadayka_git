from random import randint
def logic_of_the_game(name):
    global game,list_vvedenue_chisla
    print(list_vvedenue_chisla)
    print(f"{name} угадай число")
    try:
        number = int(input())
        if number > 0 and number < 21:
            list_vvedenue_chisla.append(number)
            if number == qwerty:
                print(f"{name} победил")
                game = False
            else:
                if number > qwerty:
                    print("введите более маленькое число")
                else:
                    print("введите более большое число")

    except:
        print("некорректное значение,введите заново число")
        logic_of_the_game(name)

list_vvedenue_chisla = []
qwerty = randint(1,20)
game = True
print("введите имя первого игрока")
name1 = input()
print("введите имя второго игрока")
name2 = input()
while(game == True):
    if game == True:
        logic_of_the_game(name1)
    if game == True:
        logic_of_the_game(name2)


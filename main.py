# поле чудес
import random
import time

counter = 0


def create_cell(letter=' '):
    cell_borders = [['|‾', '‾', '‾|'], [
        '|', f' {letter} ', '|'], ['|_', '_', '_|']]
    """
    for i in range(3):
        for j in range(3):
            print(cell_borders[i][j], end=' ')
        print()
    """
    return cell_borders


def rearrange_array(input_array):
    new_vec = []
    new_vec2 = []
    new_vec3 = []

    for i in range(0, len(input_array)):
        for j in range(3):
            new_vec.append(input_array[i][0][j])
        new_vec.append(' ')

    for element in range(len(new_vec)):
        print(new_vec[element], end=' ')
    print()

    for i in range(0, len(input_array)):
        for j in range(3):
            new_vec2.append(input_array[i][1][j])
        new_vec2.append(' ')
    for element in range(len(new_vec2)):
        print(new_vec2[element], end=' ')
    print()

    for i in range(0, len(input_array)):
        for j in range(3):
            new_vec3.append(input_array[i][2][j])
        new_vec3.append(' ')
    for element in range(len(new_vec3)):
        print(new_vec3[element], end=' ')

    return input_array


def generate_word_table(word):
    some_list = []
    some_cell = create_cell()
    for i in range(len(word)):
        some_list.append(some_cell)
    return some_list


questions = { \
    'Какое животное обитает только в Китае?': 'Панда',
    'Какая птица питается только нектаром и мелкими насекомыми?': 'Колибри',
    'Как называются молодые рога марала, изюбря и пятнистого оленя?': 'Панты',
    'У какой птицы самый большой размах крыльев?': 'Альбатрос',
    'Какая наука изучает икопаемых животных?': 'Палеонтология'
}


def insert_letter():
    global counter
    global player_one_moves
    global player_two_moves
    if len(word) - counter == 1:
        print('Внимание, осталась последняя буква! Будьте аккуратнее!')
    letter = input('Введите букву: ')
    global my_word
    my_cell = create_cell(letter)

    if letter in word or letter.upper() in word:
        print('Поздравляю, вы отгадали букву!')
        print('Откройте букву')
        time.sleep(3)
        for i in range(len(word)):
            if word[i] == letter or word[i] == letter.upper():
                my_word[i] = my_cell
                counter = counter + 1
    else:
        print('Этой буквы в слове нет!')
        if player_one_moves:
            player_two_moves=True
            player_one_moves=False
        else:
            player_two_moves = False
            player_one_moves = True
    return my_word


points = [100, 200, 300, 500, 1000, 'банкрот']


def barrel_spin():
    global stand_player_one
    global stand_player_two
    global player_one_moves
    global player_two_moves
    print('Крутим барабан')
    time.sleep(2)
    points_gain = random.choice(points)
    print(f'Барабан остановился на отметке: {points_gain}')
    if points_gain == 'банкрот':
        print('К сожалению, вы банкрот!')
        if player_one_moves:
            stand_player_one = 0
            print(f'Право хода переходит вашему сопернику. Сегодня это: {name_player_two}')
            player_one_moves=False
            player_two_moves=True
        else:
            stand_player_two = 0
            print(f'Право хода переходит вашему сопернику. Сегодня это: {name_player_one}')
            player_two_moves = False
            player_one_moves = True
    else:
        print(f'Поздравляю, {points_gain} очков отправляются на ваш счёт!')
        if player_one_moves:
            stand_player_one = stand_player_one + points_gain
            print(f'На вашем счёте {stand_player_one} очков')
            time.sleep(2)
            print('Вы можете назвать букву!')
        else:
            stand_player_two = stand_player_two + points_gain
            print(f'На вашем счёте {stand_player_two} очков')
            time.sleep(2)
            print('Вы можете назвать букву!')


stand_player_one = 0
stand_player_two = 0

player_one_moves = False
player_two_moves = False
quest = random.choice(list(questions.keys()))
word = questions[quest]
my_word = generate_word_table(word)

name_player_one = input('Игрок 1, введите Ваше имя: ')
name_player_two = input('А теперь поприветствуем игрока 2, которого зовут: ')

quest = random.choice(list(questions.keys()))
word = questions[quest]
my_word = generate_word_table(word)
print('Добрый вечер, дамы и господа, поприветствуем первую и единственную двойку игроков!')
time.sleep(2)
print(f'Приветствуем вас, {name_player_one} и {name_player_two}!')
time.sleep(2)
print('Внимание, вопрос!')
time.sleep(2)
print(quest)
time.sleep(2)
arr = generate_word_table(word)
rearrange_array(arr)
time.sleep(1)

player_one_moves = True

while counter < len(word):
    if player_one_moves:
        print(f'{name_player_one}, ваш ход!')
        print('Вы можете вращать барабан!')
        time.sleep(2)
        print('Посмотрим, что же выпадет на барабане!')
        barrel_spin()
        new_wd = insert_letter()
        rearrange_array(new_wd)
    else:
        print(f'{name_player_two}, ваш ход!')
        print('Вы можете вращать барабан!')
        time.sleep(2)
        print('Посмотрим, что же выпадет на барабане!')
        barrel_spin()
        new_wd = insert_letter()
        rearrange_array(new_wd)
if player_one_moves:
    print(f'Игра окончена! {name_player_one}, Поздравляю вас, вы победили, на вашем счёте {stand_player_one} очков. Выберите ваш приз!')
else:
    print(f'Игра окончена! {name_player_two}, Поздравляю вас, вы победили, на вашем счёте {stand_player_two} очков. Выберите ваш приз!')
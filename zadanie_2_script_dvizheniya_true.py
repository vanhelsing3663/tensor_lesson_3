traffic_information = """Выбор движения персонажа
1 - вперед, 2 - назад, 3 - вправо, 4 - влево\n"""
man_steps = "Введите целое не отрицательное число : "
err = False
x = y = 0
print(f'Исходная позиция: {x, y}')


def move_human(x):
    '''
        Функция которая делает проверку числа
        :param x: целое число x
        :return: либо кол-во шагов или 'Число < 0 '
    '''
    step = int(input(x))
    if step >= 0:
        return step
    else:
        print('Число меньше 0')
        return 0


match int(input(f'{traffic_information}Введите число : ')):
    case 1:
        x += move_human(f'Вперед! {man_steps}')
    case 2:
        x -= move_human(f'Назад! {man_steps}')
    case 3:
        y += move_human(f'Вправо! {man_steps}')
    case 4:
        y -= move_human(f'Влево! {man_steps}')
    case _:
        print('Неправильный ввод!')
        err = True

if not err:
    print(f'Текущая позиция: {x, y}')

enter_where_to_go_man = input('Введите куда двигаться персонажу\n1)Влево\n'
                              '2)Вправо\n'
                              '3)Вверх\n'
                              '4)Вниз\n'
                              '5)Для остановки скрипта введите:СТОП\n'
                              'Вводите куда двигаться персонажу : ')

x = 0
y = 0
while True:
    if enter_where_to_go_man == 'СТОП':
        break
    enter_the_number_of_steps = int(input("Введите количество шагов: "))
    if enter_where_to_go_man == 'влево':
        x -= enter_the_number_of_steps
        print(x, y)
    elif enter_where_to_go_man == 'вправо':
        x += enter_the_number_of_steps
        print(x, y)
    elif enter_where_to_go_man == 'вверх':
        y += enter_the_number_of_steps
        print(x, y)
    elif enter_where_to_go_man == 'вниз':
        y -= enter_the_number_of_steps
        print(x, y)
    else:
        raise ValueError('Введена некоректная команда')
    enter_where_to_go_man = input('Вводите куда двигаться персонажу : ')



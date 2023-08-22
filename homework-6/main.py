from src.linked_list import LinkedList

def add_list(data, head: bool):
    print(f"\tДобавляем \033[35m{data}\033[39m в {'начало списка' if head else 'конец списка'}")

    if head:
        ll.insert_beginning(data)
    else:
        ll.insert_at_end(data)

    print(f'\t\033[32mСписок\033[39m: {ll}')
    print(f'\tНачало списка: \033[33m{ll.head.data}\033[39m, '
          f'Конец списка: \033[33m{ll.tail.data}\033[39m\n')


if __name__ == '__main__':
    #
    # НАЧАЛО ПРОГРАММЫ
    #

    # Создаем и наполняем односвязный список
    ll = LinkedList()
    print(f'\n\t\033[32mСписок\033[39m: {ll}')

    print('\nДобавляем данные в список:\n')
    for i in [({'id': 1, 'username': 'lazzy508509'}, True),
              ({'id': 2, 'username': 'mik.roz'}, False),
              ({'id': 3, 'username': 'mosh_s'}, False),
              ({'id': 0, 'username': 'serebro'}, True)]:
        add_list(i[0], i[1])

    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    # ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    # ll.insert_beginning({'id': 0, 'username': 'serebro'})

    print(f'\t\033[32mСписок\033[39m: {ll}')

    # метод to_list()
    lst = ll.to_list()
    print('\nСписок:')
    for item in lst:
        print(f'\t- {item}')
    # {'id': 0, 'username': 'serebro'}
    # {'id': 1, 'username': 'lazzy508509'}
    # {'id': 2, 'username': 'mik.roz'}
    # {'id': 3, 'username': 'mosh_s'}

    # метод get_data_by_id()
    for i in [2, 3, 8]:
        print(f'\nИщем в списке словарь с id = \033[32m{i}\033[39m: ')
        user_data = ll.get_data_by_id(i)
        # Данные не являются словарем или в словаре нет id.
        # Данные не являются словарем или в словаре нет id.
        temp_str = f"\033[32m{user_data}" if user_data != None else "\033[31mне найден"
        print(f'\tНайденный элемент: {temp_str}\033[39m')
        if i == 3:
            assert user_data == {'id': 3, 'username': 'mosh_s'}


    # user_data = ll.get_data_by_id(3)
    # print(user_data)
    # print()

    # работа блока try/except
    ll = LinkedList()
    print(f'\n\t\033[32mСписок\033[39m: {ll}')

    print('\nДобавляем данные в список:\n')
    for i in [({'id': 1, 'username': 'lazzy508509'}, True),
              ({'id_': 6, 'username': 'test_user'}, False),
              ('idusername', False),
              ([1, 2, 3], False),
              ({'id': 2, 'username': 'mosh_s'}, False)]:
        add_list(i[0], i[1])

    print(f'\t\033[32mСписок\033[39m: {ll}')

    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end({'id_': 6, 'username': 'test_user'})
    # ll.insert_at_end('idusername')
    # ll.insert_at_end([1, 2, 3])
    # ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    for i in [2, 6, 8]:
        print(f'\nИщем в списке словарь с id = \033[32m{i}\033[39m: ')
        user_data = ll.get_data_by_id(i)
        # Данные не являются словарем или в словаре нет id.
        # Данные не являются словарем или в словаре нет id.
        temp_str = f"\033[32m{user_data}" if user_data != None else "\033[31mне найден"
        print(f'\tНайденный элемент: {temp_str}\033[39m')
        # {'id': 2, 'username': 'mosh_s'}

    lst = ll.to_list()
    print('\nСписок:')
    for item in lst:
        print(f'\t- {item}')

    #
    # КОНЕЦ ПРОГРАММЫ
    #


from src.linked_list import LinkedList

ll = LinkedList()


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
    # Создаем пустой односвязный список
    # ll = LinkedList()
    print(f'\033[32mСписок\033[39m: {ll}')

    # Добавляем данные
    print('\nДобавляем данные в список:\n')
    for i in [(1, True),
              (2, False),
              (3, False),
              (0, True)]:
        add_list({'id': i[0]}, i[1])


    # Печатаем данные
    print(f'Список: {ll}')
    assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

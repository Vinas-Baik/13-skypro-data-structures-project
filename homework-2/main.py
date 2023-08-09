from src.stack import Node, Stack

if __name__ == '__main__':
    #
    #  НАЧАЛО программы
    #

    print('\nРабота со стеком (Домашняя работа № 2)\n'.upper())
    print('1-ая часть: \n')
    stack = Stack()
    print(f'-> Стек: {stack.print_stack()}')

    stack.push('data1')
    print(f'-> Стек: {stack.print_stack()}')

    data = stack.pop().data
    print(f'-> Стек: {stack.print_stack()}')

    # стэк стал пустой
    assert stack.top() is None

    # pop() удаляет элемент и возвращает данные удаленного элемента
    assert data == 'data1'

    print('\n2-ая часть: \n')

    stack = Stack()
    print(f'-> Стек: {stack.print_stack()}')
    stack.push('data1')
    print(f'-> Стек: {stack.print_stack()}')
    stack.push('data2')
    print(f'-> Стек: {stack.print_stack()}')
    data = stack.pop().data
    print(f'-> Стек: {stack.print_stack()}')

    # теперь последний элемента содержит данные data1
    assert stack.top.data == 'data1'

    # данные удаленного элемента
    assert data == 'data2'

    #
    #  КОНЕЦ программы
    #
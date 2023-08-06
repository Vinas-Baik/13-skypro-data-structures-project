from src.stack import Node, Stack

if __name__ == '__main__':
    #
    #  НАЧАЛО программы
    #
    print('\nРабота с узлом стека\n'.upper())
    n1 = Node(5)
    n2 = Node('a', n1)
    print(f'Узел стека n1: {n1}')
    print(f'Узел стека n2: {n2}')
    print(f'данные узла стека n1: {n1.data}')  # 5
    print(f'данные узла стека n2: {n2.data}')  # a
    # print(n1)  # <__main__.Node object at 0x0000022803036050>
    print(f'данные следующего узла стека n2: {n2.next_node}')  # <__main__.Node object at 0x0000022803036050>

    # Работа со стеком, добавление элементов
    print('\nРабота со стеком\n'.upper())
    stack = Stack()
    print(f'Стек: {stack.print_stack()}')

    stack.push('data1')
    print(f'Стек: {stack.print_stack()}')

    stack.push('data2')
    print(f'Стек: {stack.print_stack()}')

    stack.push('data3')
    print(f'Стек: {stack.print_stack()}')

    # Работа со стеком, просмотр вершины
    print()
    print(f'stack.top().data = {stack.top().data}')  # data3
    print(f'stack.top().next_node.data = {stack.top().next_node.data}')  # data2
    print(f'stack.top().next_node.next_node.data = {stack.top().next_node.next_node.data}')  # data1
    print(f'stack.top().next_node.next_node.next_node = {stack.top().next_node.next_node.next_node}')  # None
    # print(stack.top().next_node.next_node.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'

    # Работа со стеком, удаление элементов
    print()
    print(f'Удален из стека: {stack.pop().data}')
    print(f'Стек: {stack.print_stack()}')

    print(f'Удален из стека: {stack.pop().data}')
    print(f'Стек: {stack.print_stack()}')

    print(f'Удален из стека: {stack.pop().data}')
    print(f'Стек: {stack.print_stack()}')


    #
    #  КОНЕЦ программы
    #

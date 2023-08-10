from src.queue import Queue

if __name__ == '__main__':
    #
    # НАЧАЛО ПРОГРАММЫ
    #
    print('\n\t\t\tНАЧАЛО ПРОГРАММЫ\n')
    queue = Queue()

    # Магический метод __str__ возвращает пустую строку
    assert str(Queue()) == ""

    print(f'\033[32mОчередь\033[39m: {queue.print_queue()}')
    print(f'\033[32mОчередь в начале\033[39m: \n{queue}')

    # Добавляем данных в очередь
    queue.enqueue('data1')
    print(f'Добавлен элемент \033[32m{queue.tail().data}\033[39m в очередь')
    # print(f'\033[32mОчередь\033[39m: \n{queue.__repr__()}')
    print(f'\033[32mОчередь\033[39m: {queue.print_queue()}')
    queue.enqueue('data2')
    print(f'Добавлен элемент \033[32m{queue.tail().data}\033[39m в очередь')
    print(f'\033[32mОчередь\033[39m: {queue.print_queue()}')
    queue.enqueue('data3')
    print(f'Добавлен элемент \033[32m{queue.tail().data}\033[39m в очередь')
    print(f'\033[32mОчередь\033[39m: {queue.print_queue()}')
    print(f'\033[32mОчередь после добавления элементов\033[39m: \n{queue}')
    print()
    # Проверяем очередность хранения данных
    print(f'Голова очереди: \033[32m{queue.head().data}\033[39m')
    assert queue.head().data == 'data1'
    print(f'Следующий элемент после головы очереди: \033[32m{queue.head().next_node.data}\033[39m')
    assert queue.head().next_node.data == 'data2'
    print(f'Конец очереди: \033[32m{queue.tail().data}\033[39m')
    assert queue.tail().data == 'data3'
    print(f'Следующий элемент за концом очереди: \033[32m{queue.tail().next_node}\033[39m')
    assert queue.tail().next_node is None
    # print(queue.tail().next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'

    # Проверяем магический метод __str__
    assert str(queue) == "data1\ndata2\ndata3"

    #
    # КОНЕЦ ПРОГРАММЫ
    #

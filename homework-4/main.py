from src.queue import Queue

if __name__ == '__main__':
    # Создаем пустую очередь
    queue = Queue()

    # Добавляем данные в очередь
    print(f'Очередь: {queue.print_queue()}')
    for temp_st in ['data1', 'data2', 'data3']:
        print(f'Добавляем в очередь \033[32m{temp_st}\033[39m')
        queue.enqueue(temp_st)
        print(f'Очередь: \033[33m{queue.print_queue()}\033[39m')

    for temp_st in ['data1', 'data2', 'data3', None]:
        temp_data = queue.dequeue()
        assert temp_data == temp_st
        print(f'Удаляем \033[32m{temp_data}\033[39m')
        print(f'Очередь после удаления: \033[33m{queue.print_queue()}\033[39m')


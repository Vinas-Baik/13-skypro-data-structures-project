class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'{self.data} [{self.next_node if self.next_node != None else ""}]'

    def __repr__(self):
        return f'Node({self.data} [{self.next_node if self.next_node != None else ""}])'


class Queue:
    """Класс для очереди"""

    # элементы очереди
    all = []

    def __init__(self):
        """Конструктор класса Queue"""
        Queue.all = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        temp_node: Node = Node(data)
        if len(Queue.all) > 0:
            Queue.all[-1].next_node = temp_node
        Queue.all.append(temp_node)


    def dequeue(self) -> Node:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        # if Queue.all != []:
        #     return Queue.all.pop(0)
        # pass


    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return '\n'.join([temp_q.data for temp_q in Queue.all])

    def __repr__(self):
        """Магический метод для строкового представления объекта"""
        return '\n'.join([f"{temp_q}" for temp_q in Queue.all])

    def print_queue(self) -> str:
        """Магический метод для строкового представления объекта"""
        if Queue.all == []:
            return 'пустая'
        return ' -> '.join([temp_q.data for temp_q in Queue.all])

    def head(self) -> Node:
        if Queue.all == []:
            return None
        return Queue.all[0]

    def tail(self) -> Node:
        if Queue.all == []:
            return None
        return Queue.all[-1]

# queue = Queue()

# print(f'Очередь: {Queue()}')
# print(f'Очередь: {queue}')

# Добавляем данных в очередь
# queue.enqueue('data1')
# # print()
# print(f'Очередь: \n{queue.__repr__()}')
# # print()
# queue.enqueue('data2')
# # print()
# # print(f'Очередь: \n{queue.__repr__()}')
# # print()
# queue.enqueue('data3')
# # print()
# print(f'Очередь: {queue.print_queue()}')
# print()
# print(f'Очередь: \n{queue.__repr__()}')
# print()
# print(queue.head().data)
# print(queue.tail().data)
# print(queue.head().next_node.data)
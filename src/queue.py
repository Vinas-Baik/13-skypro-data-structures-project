class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.__next_node = next_node

    def __str__(self):
        return f'{self.__data} [{self.__next_node}]'

    def __repr__(self):
        return f'Node({self.__data} [{self.__next_node}])'


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
        if Queue.all == []:
            Queue.all.append(Node(data))
        else:
            Queue.all.append(Node(data, Queue.all[-1]))


    def dequeue(self) -> Node:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if Queue.all != []:
            return Queue.all.pop(0)

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return '\n'.join(temp_q.data for temp_q in Queue.all)

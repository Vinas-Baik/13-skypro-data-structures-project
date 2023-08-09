
class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        next_node - ссылка на следующий узел стека
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'{self.data} [{self.next_node}]'

    def __repr__(self):
        return f'Node({self.data} [{self.next_node}])'


class Stack:
    """Класс для стека"""

    #элементы стека
    all = []

    # возвращаем последний элемент списка
    def top(self):
        if Stack.all == []:
            return None
        else:
            return Stack.all[-1]


    def __init__(self):
        """Конструктор класса Stack"""
        Stack.all = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if Stack.all == []:
            Stack.all.append(Node(data))
        else:
            Stack.all.append(Node(data, Stack.all[-1]))

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if Stack.all != []:
            return Stack.all.pop(-1)

    def print_stack(self):
        """
        Метод формирования строки для печати стека

        :return: сттрока с данными стека
        """
        if Stack.all == []:
            result = 'пустой'
        for item in Stack.all:
            if item.next_node == None:
                result = f'{item.data}'
            else:
                result = f'{item.data} -> {result}'
        return result

class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node: 'Node'=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        next_node - ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'{self.data} [{self.next_node}]'

    def __repr__(self):
        return f'Node({self.data}, {self.next_node})'


class LinkedList:
    """Класс для односвязного списка"""

    __slots__ = ('head', 'tail')
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными
        в начало связанного списка
        """
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp_node = Node(data, self.head)
            self.head = temp_node


    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными
        в конец связанного списка
        """
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp_node = self.head
            while temp_node.next_node !=None:
                temp_node = temp_node.next_node
            temp_node.next_node = Node(data)
            self.tail = temp_node.next_node

    def to_list(self) -> list:
        """
        возвращает список с данными, содержащимися в односвязном списке
        `LinkedList`
        """
        t_list = []
        node = self.head
        if node is None:
            return []
        while node:
            t_list.append(node.data)
            node = node.next_node
        return t_list

    def get_data_by_id(self, id: int):
        """
        возвращает первый найденный в `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению.

        Добавлен блок `try/except` для перехвата ошибки `TypeError` и
        печати в консоль сообщения о неподходящем формате данных.

        """
        t_Node_data = None
        node = self.head
        if node is None:
            return None

        while node:
            try:
                if node.data['id'] == id:
                    t_Node_data = node.data
            except TypeError:
                print(f'\t\033[36m{node.data}:\033[31m данные не являются словарем '
                      f'или в словаре нет id.\033[39m')
            except KeyError:
                print(f'\t\033[36m{node.data}:\033[31m данные не являются словарем '
                      f'или в словаре нет id.\033[39m')
            node = node.next_node
        return t_Node_data


    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string



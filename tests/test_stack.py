import unittest
from src.stack import Node, Stack

"""Здесь надо написать тесты с использованием unittest для модуля stack."""

class TestArrs(unittest.TestCase):
    def test_Node(self):
        n1 = Node(5)
        n2 = Node('a', n1)
        self.assertEqual(n1.__str__(), '5 [None]')
        self.assertEqual(n1.__repr__(), 'Node(5 [None])')


    def test_Stack(self):
        stack = Stack()
        self.assertEqual(stack.top(), None)
        self.assertEqual(stack.all, [])
        self.assertEqual(stack.print_stack(), 'пустой')
        stack.push('data1')
        self.assertEqual(stack.print_stack(), 'data1')
        stack.push('data2')
        self.assertEqual(stack.print_stack(), 'data2 -> data1')
        self.assertEqual(stack.top().data, 'data2')
        self.assertEqual(stack.pop().data, 'data2')
        self.assertEqual(stack.print_stack(), 'data1')

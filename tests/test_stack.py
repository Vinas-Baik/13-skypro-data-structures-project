import unittest
from src.stack import Node, Stack

"""Здесь надо написать тесты с использованием unittest для модуля stack."""

def test_Node():
    n1 = Node(5)
    n2 = Node('a', n1)
    assert n1 == '5 [None]'
    assert n2 == 'a [5 [None]]'
    assert n1.__str__() == '5 [None]'
    assert n1.__repr__() == 'Node(5, None)'


def test_Stack():
    stack = Stack()
    assert stack.print_stack() == 'пустой'
    stack.push('data1')
    assert stack.print_stack() == 'data1'
    stack.push('data2')
    assert stack.print_stack() == 'data2 -> data1'
    assert stack.top().data == 'data2'
    assert stack.pop == 'data2'
    assert stack.print_stack() == 'data1'

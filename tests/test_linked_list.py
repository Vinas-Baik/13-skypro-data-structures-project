import unittest
from src.linked_list import LinkedList, Node


"""Здесь надо написать тесты с использованием unittest для модуля queue."""

class TestArrs(unittest.TestCase):
    def test_node(self):
        ll1 = Node(1)
        self.assertEqual(str(ll1), '1 [None]')
        self.assertEqual(repr(ll1), 'Node(1, None)')

    def test_linkedlist(self):
        ll1 = LinkedList()
        ll1.insert_at_end(1)
        self.assertEqual(str(ll1), ' 1 -> None')

        ll = LinkedList()
        self.assertEqual(str(ll), "None")
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        for i in [(1, True),
                  (2, False),
                  (3, False),
                  (0, True)]:
            if i[1]:
                ll.insert_beginning(i[0])
            else:
                ll.insert_at_end(i[0])

        self.assertEqual(str(ll), ' 0 -> 1 -> 2 -> 3 -> None')

        ll1 = LinkedList()
        self.assertEqual(ll1.to_list(), [])
        self.assertEqual(ll1.get_data_by_id(1), None)
        for i in [({'id': 1}, True),
                  ({'id': 2}, False),
                  ({'id': 3}, False),
                  ({'id': 0}, True)]:
            if i[1]:
                ll1.insert_beginning(i[0])
            else:
                ll1.insert_at_end(i[0])

        self.assertEqual(str(ll1), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
        self.assertEqual(str(ll1.get_data_by_id(1)), "{'id': 1}")
        self.assertEqual(ll.to_list(), [0, 1, 2, 3])
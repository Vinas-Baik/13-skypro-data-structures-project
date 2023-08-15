import unittest
from src.queue import Queue


"""Здесь надо написать тесты с использованием unittest для модуля queue."""

class TestArrs(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        self.assertEqual(str(Queue()), "")
        self.assertEqual(queue.head(), None)
        self.assertEqual(queue.tail(), None)
        self.assertEqual(queue.__repr__(), '')
        self.assertEqual(queue.print_queue(), 'пустая')
        queue.enqueue('data1')
        self.assertEqual(queue.__repr__(), 'data1 []')
        self.assertEqual(queue.all[0].__repr__(), 'Node(data1 [])')
        self.assertEqual(queue.head().data, 'data1')
        self.assertEqual(queue.head().data, queue.tail().data)
        queue.enqueue('data2')
        self.assertEqual(queue.tail().data, 'data2')
        self.assertEqual(queue.head().next_node.data, 'data2')
        self.assertEqual(queue.head().next_node.data, queue.tail().data)
        queue.enqueue('data3')
        self.assertEqual(queue.tail().data, 'data3')
        self.assertEqual(queue.all[-1].data, queue.tail().data)
        self.assertEqual(queue.all[0].data, queue.head().data)
        self.assertEqual(queue.print_queue(), 'data3 -> data2 -> data1')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.print_queue(), 'data3 -> data2')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.print_queue(), 'data3')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.print_queue(), 'пустая')







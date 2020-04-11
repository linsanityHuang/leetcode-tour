

class CircularQueue:
    """
    基于数组实现的循环队列
    """

    def __init__(self, capacity: int = 5):
        self._capacity = capacity
        self._items = [0 for _ in range(self._capacity)]
        self._head = 0
        self._tail = 0
    
    def enqueue(self, item) -> bool:
        # 队列满了
        if (self._tail + 1) % self._capacity == self._head:
            return False
        
        self._items[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        return True
    
    def dequeue(self):
        # 出队
        if self._tail == self._head:
            return None
        item = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        return item


def test_circular_queue_1():
    q = CircularQueue()
    
    assert q.enqueue(1) is True
    assert q.enqueue(10) is True
    assert q.enqueue(-11) is True
    assert q.enqueue(2) is True

    assert q.enqueue(14) is False

    assert q.dequeue() == 1
    assert q.dequeue() == 10
    assert q.dequeue() == -11
    assert q.dequeue() == 2
    assert q.dequeue() is None

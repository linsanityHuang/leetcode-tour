

class ArrayQueue:
    """
    基于数组实现的顺序队列
    """

    def __init__(self, capacity: int = 5):
        # 队列容量
        self.capacity = capacity
        # 底层数组
        self.items = [0 for _ in range(self.capacity)]
        # head表示对头下标
        self.head = 0
        # tail表示队尾下标
        self.tail = 0

    def enqueue(self, item) -> bool:
        """
        入队
        :param item:
        :return:
        """
        
        if self.tail == self.capacity:
            if self.head == 0:
                # 队列已满
                return False
            # 搬移数据
            for i in range(self.head, self.tail):
                self.items[i - self.head] = self.items[i]
            # 搬移完之后重新更新head和tail
            self.tail = self.tail - self.head
            self.head = 0
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):
        """
        出队
        :return:
        """
        if self.head == self.tail:
            return None
        item = self.items[self.head]
        self.head += 1
        return item


def test_array_queue_1():
    q = ArrayQueue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(10)

    assert q.enqueue(14) is False

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 10
    assert q.dequeue() is None

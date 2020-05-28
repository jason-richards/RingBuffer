
class RingBufferIterator:
    m_RingBuffer = None
    m_Index = None

    '''Ring Buffer Iterator'''
    def __init__(self, rb):
        self.m_RingBuffer = rb
        self.m_Index = 0

    def __next__(self):
        if self.m_Index >= self.m_RingBuffer.size:
            raise StopIteration
        self.m_Index += 1
        return self.m_RingBuffer.GetItem(self.m_Index + self.m_RingBuffer.head - 1) 

class RingBuffer:
    m_Capacity = 0
    m_Buffer = None
    m_Size = 0

    def __init__(self, capacity):
        self.Reset(capacity)

    def __iter__(self):
        return RingBufferIterator(self)

    def Reset(self, capacity=None):
        self.m_Capacity = self.m_Capacity if capacity is None else capacity
        self.m_Buffer = [None] * capacity
        self.m_Size = 0

    def AddItem(self, item):
        self.m_Buffer[self.m_Size % self.m_Capacity] = item
        self.m_Size += 1

    def GetItem(self, index):
        return self.m_Buffer[index % self.m_Capacity]

    @property
    def size(self):
        return self.m_Size if self.m_Size < self.m_Capacity else self.m_Capacity

    @property
    def get(self):
        return self.m_Buffer

    @property
    def tail(self):
        return self.m_Size % self.m_Capacity - 1

    @property
    def head(self):
        tail = self.tail
        if tail < 0:
            return tail
        if self.m_Size < self.m_Capacity:
            return 0
        return tail + 1

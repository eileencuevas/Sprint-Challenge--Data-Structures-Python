class RingBuffer:  # this is basically a FIFO queue
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        pass

    def get(self):
        pass

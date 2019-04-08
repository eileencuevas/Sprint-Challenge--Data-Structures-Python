class RingBuffer:  # this is similar to a FIFO queue
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0  # this is the current index in the storage to overwrite
        self.storage = [None]*capacity  # storage preset to be a certain length

    def append(self, item):
        self.storage[self.current] = item
        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]

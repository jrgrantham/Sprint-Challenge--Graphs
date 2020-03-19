class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def connect_rooms(previous, current, direction)
    pairs = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    previous[direction] = current
    current[side_pairs[direction]] = previous
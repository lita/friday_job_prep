import Queue

class Storage (object):
    def __init__(self):
        pass
    def get(self, element):
        pass
    def put(self, element):
        pass
    def isEmpty(self):
        pass

class DepthFirstStorage(Storage):
    def __init__(self):
        self.stack = []

    def get(self):
        if self.stack:
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) > 0

    def put(self, element):
        return self.stack.append(element)

class BreathFirstStorage(Storage):
    def __init__(self):
        self.queue = Queue.Queue()

    def get(self):
        return self.queue.get()

    def put(self, element):
        return self.queue.put(element)

    def isEmpty(self):
        return self.queue.isEmpty()



def print_graph(g, storage):



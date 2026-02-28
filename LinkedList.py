class Branch:
    def __init__(self, data):
        self.data = data
        self.next = None # Pointer to the next node, initialized to None

    def next(self, next):
        self.next = next
class Memory:
    def __init__(self):
        self.name = None
        self.email = None
        self.platform = None
        self.stage = None

    def is_complete(self):
        return self.name and self.email and self.platform
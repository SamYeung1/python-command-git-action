class Command:
    def __init__(self, name, args=None):
        if args is None:
            args = []
        self.name = name
        self.args = args

    def execute(self):
        pass

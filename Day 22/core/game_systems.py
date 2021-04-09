class Systems:
    """A systems class monitors gameplay"""

    def __init__(self):
        self.play = True

    def stop(self):
        self.play = False

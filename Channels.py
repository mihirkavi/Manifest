# Channels Class
class Channels:
    def __init__(self, channels=None):
        if channels is None:
            channels = []
        self.channels = channels  # List of channels

    def add_channel(self, channel):
        self.channels.append(channel)
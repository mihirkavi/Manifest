class RevenueStreams:
    def __init__(self, streams=None):
        if streams is None:
            streams = []
        self.streams = streams  # List of revenue streams

    def add_stream(self, stream):
        self.streams.append(stream)
# Customer Segments Class
class CustomerSegments:
    def __init__(self, segments=None):
        if segments is None:
            segments = []
        self.segments = segments  # List of customer segments

    def add_segment(self, segment):
        self.segments.append(segment)
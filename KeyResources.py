# Key Resources Class
class KeyResources:
    def __init__(self, resources=None):
        if resources is None:
            resources = []
        self.resources = resources  # List of key resources

    def add_resource(self, resource):
        self.resources.append(resource)
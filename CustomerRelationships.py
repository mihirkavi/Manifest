# Customer Relationships Class
class CustomerRelationships:
    def __init__(self, relationships=None):
        if relationships is None:
            relationships = []
        self.relationships = relationships  # List of customer relationships

    def add_relationship(self, relationship):
        self.relationships.append(relationship)
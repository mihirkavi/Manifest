# Cost Structure Class
class CostStructure:
    def __init__(self, costs=None):
        if costs is None:
            costs = []
        self.costs = costs  # List of cost elements

    def add_cost(self, cost):
        self.costs.append(cost)
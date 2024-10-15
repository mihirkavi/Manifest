# Value Propositions Class
class ValuePropositions:
    def __init__(self, propositions=None):
        if propositions is None:
            propositions = []
        self.propositions = propositions  # List of value propositions

    def add_proposition(self, proposition):
        self.propositions.append(proposition)
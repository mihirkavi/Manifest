# Key Partners Class
class KeyPartners:
    def __init__(self, partners=None):
        if partners is None:
            partners = []
        self.partners = partners  # List of key partners

    def add_partner(self, partner):
        self.partners.append(partner)
class BusinessModelCanvas:
    def __init__(self, key_partners, key_activities, key_resources, value_propositions, customer_relationships , channels , customer_segments , cost_structure, revenue_streams):
        self.key_partners = key_partners
        self.key_activities = key_activities
        self.key_resources = key_resources
        self.value_propositions = value_propositions
        self.customer_relationships = customer_relationships
        self.channels = channels
        self.customer_segments = customer_segments
        self.cost_structure = cost_structure
        self.revenue_streams = revenue_streams
    
    def show(self):
        print()
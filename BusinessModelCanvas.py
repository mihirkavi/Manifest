# Import all the classes from their respective files
from KeyPartners import KeyPartners
from KeyActivities import KeyActivities
from KeyResources import KeyResources
from ValuePropositions import ValuePropositions
from CustomerRelationships import CustomerRelationships
from Channels import Channels
from CustomerSegments import CustomerSegments
from CostStructure import CostStructure
from RevenueStreams import RevenueStreams

class BusinessModelCanvas:
    def __init__(self):
        self.key_partners = KeyPartners()
        self.key_activities = KeyActivities()
        self.key_resources = KeyResources()
        self.value_propositions = ValuePropositions()
        self.customer_relationships = CustomerRelationships()
        self.channels = Channels()
        self.customer_segments = CustomerSegments()
        self.cost_structure = CostStructure()
        self.revenue_streams = RevenueStreams()
    
    def show(self):
        print()
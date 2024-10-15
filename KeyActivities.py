# Key Activities Class
class KeyActivities:
    def __init__(self, activities=None):
        if activities is None:
            activities = []
        self.activities = activities  # List of key activities

    def add_activity(self, activity):
        self.activities.append(activity)

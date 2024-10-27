from datetime import datetime

class ProductRoadmap:
    def __init__(self, product_name):
        """
        Initialize a Product Roadmap for a specific product.
        
        Parameters:
        - product_name (str): The name of the product.
        """
        self.product_name = product_name
        self.milestones = []

    def add_milestone(self, milestone_name, description, estimated_completion, responsible_team):
        """
        Add a new milestone to the product roadmap.
        
        Parameters:
        - milestone_name (str): The name of the milestone.
        - description (str): A short description of the milestone.
        - estimated_completion (str): Estimated completion date (format: 'YYYY-MM-DD').
        - responsible_team (str): The team or individual responsible for the milestone.
        
        Returns:
        - str: A message indicating the addition status.
        """
        try:
            completion_date = datetime.strptime(estimated_completion, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD'."
        
        milestone = {
            "Milestone Name": milestone_name,
            "Description": description,
            "Estimated Completion": completion_date,
            "Responsible Team": responsible_team,
            "Features": []
        }
        self.milestones.append(milestone)
        return f"Milestone '{milestone_name}' has been added."

    def add_feature_to_milestone(self, milestone_name, feature_name, feature_description):
        """
        Add a feature to a specific milestone.
        
        Parameters:
        - milestone_name (str): The name of the milestone.
        - feature_name (str): The name of the feature.
        - feature_description (str): A short description of the feature.
        
        Returns:
        - str: A message indicating the addition status.
        """
        for milestone in self.milestones:
            if milestone["Milestone Name"] == milestone_name:
                milestone["Features"].append({
                    "Feature Name": feature_name,
                    "Description": feature_description
                })
                return f"Feature '{feature_name}' has been added to milestone '{milestone_name}'."
        return f"Milestone '{milestone_name}' not found."

    def display_roadmap(self):
        """
        Display the entire product roadmap.
        """
        print(f"=== Product Roadmap for {self.product_name} ===")
        for milestone in self.milestones:
            completion_date = milestone["Estimated Completion"].strftime("%Y-%m-%d")
            print(f"\nMilestone: {milestone['Milestone Name']}")
            print(f"Description        : {milestone['Description']}")
            print(f"Estimated Completion : {completion_date}")
            print(f"Responsible Team   : {milestone['Responsible Team']}")
            print("Features:")
            for feature in milestone["Features"]:
                print(f"  - {feature['Feature Name']}: {feature['Description']}")
            print("---------------------------------------------------")

    def update_milestone_date(self, milestone_name, new_date):
        """
        Update the estimated completion date of a milestone.
        
        Parameters:
        - milestone_name (str): The name of the milestone.
        - new_date (str): The new estimated completion date (format: 'YYYY-MM-DD').
        
        Returns:
        - str: A message indicating the update status.
        """
        try:
            new_completion_date = datetime.strptime(new_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use 'YYYY-MM-DD'."
        
        for milestone in self.milestones:
            if milestone["Milestone Name"] == milestone_name:
                milestone["Estimated Completion"] = new_completion_date
                return f"Milestone '{milestone_name}' completion date has been updated to {new_date}."
        return f"Milestone '{milestone_name}' not found."

    def remove_milestone(self, milestone_name):
        """
        Remove a milestone from the product roadmap.
        
        Parameters:
        - milestone_name (str): The name of the milestone to remove.
        
        Returns:
        - str: A message indicating the removal status.
        """
        for milestone in self.milestones:
            if milestone["Milestone Name"] == milestone_name:
                self.milestones.remove(milestone)
                return f"Milestone '{milestone_name}' has been removed."
        return f"Milestone '{milestone_name}' not found."
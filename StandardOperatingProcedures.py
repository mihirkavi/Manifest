from datetime import datetime

class StandardOperatingProcedure:
    def __init__(self, procedure_name, department, effective_date, version="1.0"):
        """
        Initialize a Standard Operating Procedure (SOP) with essential details.
        
        Parameters:
        - procedure_name (str): The name of the procedure.
        - department (str): The department responsible for the procedure.
        - effective_date (str): The date the SOP becomes effective (format: 'YYYY-MM-DD').
        - version (str): The version of the SOP.
        """
        try:
            self.effective_date = datetime.strptime(effective_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        self.procedure_name = procedure_name
        self.department = department
        self.version = version
        self.steps = []
        self.responsibilities = []
        self.reviewers = []
        self.approval_requirements = ""

    def add_step(self, step_description):
        """
        Add a step to the SOP.
        
        Parameters:
        - step_description (str): Description of the step in the procedure.
        """
        self.steps.append(step_description)

    def assign_responsibility(self, role, task):
        """
        Assign a responsibility to a specific role in the SOP.
        
        Parameters:
        - role (str): The role responsible for the task.
        - task (str): The task assigned to the role.
        """
        self.responsibilities.append({"Role": role, "Task": task})

    def add_reviewer(self, reviewer_name, role):
        """
        Add a reviewer for the SOP.
        
        Parameters:
        - reviewer_name (str): The name of the reviewer.
        - role (str): The role of the reviewer (e.g., "Quality Control").
        """
        self.reviewers.append({"Reviewer": reviewer_name, "Role": role})

    def set_approval_requirements(self, requirements):
        """
        Define the approval requirements for the SOP.
        
        Parameters:
        - requirements (str): Description of the requirements for SOP approval.
        """
        self.approval_requirements = requirements

    def display_sop(self):
        """
        Display the complete Standard Operating Procedure.
        """
        print(f"=== Standard Operating Procedure: {self.procedure_name} ===")
        print(f"Department           : {self.department}")
        print(f"Effective Date       : {self.effective_date.strftime('%Y-%m-%d')}")
        print(f"Version              : {self.version}")
        
        print("\nProcedure Steps:")
        for i, step in enumerate(self.steps, start=1):
            print(f"  Step {i}: {step}")
        
        print("\nResponsibilities:")
        for responsibility in self.responsibilities:
            print(f"  - {responsibility['Role']} is responsible for: {responsibility['Task']}")
        
        print("\nReviewers:")
        for reviewer in self.reviewers:
            print(f"  - {reviewer['Reviewer']} ({reviewer['Role']})")
        
        print(f"\nApproval Requirements: {self.approval_requirements}")
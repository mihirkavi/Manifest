class FoundersAgreement:
    def __init__(self, startup_name, business_address, founders, roles_responsibilities, ownership_percentage, vesting_schedule, ip_assignment, exit_conditions):
        """
        Initialize a Founders' Agreement document with required fields.
        
        Parameters:
        - startup_name (str): The legal name of the startup.
        - business_address (str): The primary address of the startup.
        - founders (list): List of founders' names.
        - roles_responsibilities (dict): A dictionary where keys are founder names and values are their roles and responsibilities.
        - ownership_percentage (dict): A dictionary of founders with their respective ownership percentage.
        - vesting_schedule (str): Description of the vesting schedule for equity distribution.
        - ip_assignment (str): Terms describing how intellectual property rights are assigned.
        - exit_conditions (str): Conditions under which a founder can exit and the handling of their shares.
        """
        self.startup_name = startup_name
        self.business_address = business_address
        self.founders = founders
        self.roles_responsibilities = roles_responsibilities
        self.ownership_percentage = ownership_percentage
        self.vesting_schedule = vesting_schedule
        self.ip_assignment = ip_assignment
        self.exit_conditions = exit_conditions

    def display_info(self):
        """
        Display the details of the Founders' Agreement.
        """
        print("=== Founders' Agreement ===")
        print(f"Startup Name                : {self.startup_name}")
        print(f"Business Address            : {self.business_address}")
        print(f"Founders                    : {', '.join(self.founders)}")
        print("Roles and Responsibilities  :")
        for founder, role in self.roles_responsibilities.items():
            print(f"  - {founder}: {role}")
        print(f"Ownership Percentage        : {', '.join([f'{name} ({ownership}%)' for name, ownership in self.ownership_percentage.items()])}")
        print(f"Vesting Schedule            : {self.vesting_schedule}")
        print(f"IP Assignment               : {self.ip_assignment}")
        print(f"Exit Conditions             : {self.exit_conditions}")
    
    def validate(self):
        """
        Validate required fields to ensure all fields are completed and valid.
        
        Returns:
        - bool: True if all fields are valid, otherwise False.
        """
        required_fields = [
            self.startup_name, 
            self.business_address, 
            self.founders, 
            self.roles_responsibilities, 
            self.ownership_percentage, 
            self.vesting_schedule, 
            self.ip_assignment, 
            self.exit_conditions
        ]
        
        if any(not field for field in required_fields):
            print("Error: All fields must be completed.")
            return False
        if not isinstance(self.ownership_percentage, dict) or not all(isinstance(ownership, (int, float)) for ownership in self.ownership_percentage.values()):
            print("Error: Ownership percentages should be a dictionary with founder names and percentages.")
            return False
        if sum(self.ownership_percentage.values()) != 100:
            print("Error: Total ownership percentage of all founders must be 100%.")
            return False
        if not isinstance(self.roles_responsibilities, dict) or not all(founder in self.roles_responsibilities for founder in self.founders):
            print("Error: Roles and responsibilities must be defined for each founder.")
            return False
        return True

    def submit(self):
        """
        Simulate submitting the Founders' Agreement.
        
        Returns:
        - str: A message indicating the submission status.
        """
        if self.validate():
            # Here we might save to a database or send to an API, etc.
            return f"Founders' Agreement for {self.startup_name} has been successfully submitted."
        else:
            return "Submission failed due to validation errors."
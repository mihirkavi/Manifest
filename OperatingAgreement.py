class OperatingAgreement:
    def __init__(self, llc_name, business_address, members, management_structure, profit_distribution, dissolution_terms):
        """
        Initialize an Operating Agreement document with required fields.
        
        Parameters:
        - llc_name (str): The legal name of the LLC.
        - business_address (str): The primary address of the LLC.
        - members (dict): A dictionary of members with their respective ownership percentage.
        - management_structure (str): Description of how the LLC will be managed (e.g., member-managed or manager-managed).
        - profit_distribution (str): Terms describing how profits and losses will be distributed.
        - dissolution_terms (str): Conditions under which the LLC will be dissolved.
        """
        self.llc_name = llc_name
        self.business_address = business_address
        self.members = members
        self.management_structure = management_structure
        self.profit_distribution = profit_distribution
        self.dissolution_terms = dissolution_terms

    def display_info(self):
        """
        Display the details of the Operating Agreement.
        """
        print("=== Operating Agreement ===")
        print(f"LLC Name             : {self.llc_name}")
        print(f"Business Address     : {self.business_address}")
        print(f"Members              : {', '.join([f'{name} ({ownership}%)' for name, ownership in self.members.items()])}")
        print(f"Management Structure : {self.management_structure}")
        print(f"Profit Distribution  : {self.profit_distribution}")
        print(f"Dissolution Terms    : {self.dissolution_terms}")
    
    def validate(self):
        """
        Validate required fields to ensure all fields are completed and valid.
        
        Returns:
        - bool: True if all fields are valid, otherwise False.
        """
        required_fields = [
            self.llc_name, 
            self.business_address, 
            self.members, 
            self.management_structure, 
            self.profit_distribution, 
            self.dissolution_terms
        ]
        
        if any(not field for field in required_fields):
            print("Error: All fields must be completed.")
            return False
        if not isinstance(self.members, dict) or not all(isinstance(ownership, (int, float)) for ownership in self.members.values()):
            print("Error: Members should be a dictionary with names and ownership percentages.")
            return False
        if sum(self.members.values()) != 100:
            print("Error: Total ownership percentage of all members must be 100%.")
            return False
        return True

    def submit(self):
        """
        Simulate submitting the Operating Agreement.
        
        Returns:
        - str: A message indicating the submission status.
        """
        if self.validate():
            # Here we might save to a database or send to an API, etc.
            return f"Operating Agreement for {self.llc_name} has been successfully submitted."
        else:
            return "Submission failed due to validation errors."
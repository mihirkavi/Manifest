class ShareholdersAgreement:
    def __init__(self, company_name, business_address, shareholders, board_structure, share_transfer_restrictions, voting_rights, dividend_policy, termination_conditions):
        """
        Initialize a Shareholders Agreement document with required fields.
        
        Parameters:
        - company_name (str): The legal name of the corporation.
        - business_address (str): The primary address of the corporation.
        - shareholders (dict): A dictionary of shareholders with their respective ownership percentage.
        - board_structure (str): Description of the board structure, including roles and responsibilities.
        - share_transfer_restrictions (str): Terms describing any restrictions on share transfers.
        - voting_rights (str): Details about voting rights of shareholders.
        - dividend_policy (str): Terms for distributing dividends among shareholders.
        - termination_conditions (str): Conditions under which the agreement or corporation may be terminated.
        """
        self.company_name = company_name
        self.business_address = business_address
        self.shareholders = shareholders
        self.board_structure = board_structure
        self.share_transfer_restrictions = share_transfer_restrictions
        self.voting_rights = voting_rights
        self.dividend_policy = dividend_policy
        self.termination_conditions = termination_conditions

    def display_info(self):
        """
        Display the details of the Shareholders Agreement.
        """
        print("=== Shareholders Agreement ===")
        print(f"Company Name                : {self.company_name}")
        print(f"Business Address            : {self.business_address}")
        print(f"Shareholders                : {', '.join([f'{name} ({ownership}%)' for name, ownership in self.shareholders.items()])}")
        print(f"Board Structure             : {self.board_structure}")
        print(f"Share Transfer Restrictions : {self.share_transfer_restrictions}")
        print(f"Voting Rights               : {self.voting_rights}")
        print(f"Dividend Policy             : {self.dividend_policy}")
        print(f"Termination Conditions      : {self.termination_conditions}")
    
    def validate(self):
        """
        Validate required fields to ensure all fields are completed and valid.
        
        Returns:
        - bool: True if all fields are valid, otherwise False.
        """
        required_fields = [
            self.company_name, 
            self.business_address, 
            self.shareholders, 
            self.board_structure, 
            self.share_transfer_restrictions, 
            self.voting_rights, 
            self.dividend_policy, 
            self.termination_conditions
        ]
        
        if any(not field for field in required_fields):
            print("Error: All fields must be completed.")
            return False
        if not isinstance(self.shareholders, dict) or not all(isinstance(ownership, (int, float)) for ownership in self.shareholders.values()):
            print("Error: Shareholders should be a dictionary with names and ownership percentages.")
            return False
        if sum(self.shareholders.values()) != 100:
            print("Error: Total ownership percentage of all shareholders must be 100%.")
            return False
        return True

    def submit(self):
        """
        Simulate submitting the Shareholders Agreement.
        
        Returns:
        - str: A message indicating the submission status.
        """
        if self.validate():
            # Here we might save to a database or send to an API, etc.
            return f"Shareholders Agreement for {self.company_name} has been successfully submitted."
        else:
            return "Submission failed due to validation errors."
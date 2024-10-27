class ArticlesOfIncorporation:
    def __init__(self, business_name, business_purpose, business_address, registered_agent, shares_authorized, incorporator_name):
        """
        Initialize an Articles of Incorporation document with required fields.
        
        Parameters:
        - business_name (str): The legal name of the corporation.
        - business_purpose (str): The purpose or nature of the business.
        - business_address (str): The primary address of the business.
        - registered_agent (str): The person or entity authorized to receive legal documents.
        - shares_authorized (int): The total number of shares the corporation is authorized to issue.
        - incorporator_name (str): The name of the individual filing the articles.
        """
        self.business_name = business_name
        self.business_purpose = business_purpose
        self.business_address = business_address
        self.registered_agent = registered_agent
        self.shares_authorized = shares_authorized
        self.incorporator_name = incorporator_name

    def display_info(self):
        """
        Display the details of the Articles of Incorporation.
        """
        print("=== Articles of Incorporation ===")
        print(f"Business Name        : {self.business_name}")
        print(f"Business Purpose     : {self.business_purpose}")
        print(f"Business Address     : {self.business_address}")
        print(f"Registered Agent     : {self.registered_agent}")
        print(f"Shares Authorized    : {self.shares_authorized}")
        print(f"Incorporator Name    : {self.incorporator_name}")
    
    def validate(self):
        """
        Validate required fields to ensure all fields are filled correctly.
        
        Returns:
        - bool: True if all fields are valid, otherwise False.
        """
        required_fields = [
            self.business_name, 
            self.business_purpose, 
            self.business_address, 
            self.registered_agent, 
            self.shares_authorized, 
            self.incorporator_name
        ]
        
        if any(not field for field in required_fields):
            print("Error: All fields must be completed.")
            return False
        if not isinstance(self.shares_authorized, int) or self.shares_authorized <= 0:
            print("Error: Shares authorized must be a positive integer.")
            return False
        return True

    def submit(self):
        """
        Simulate submitting the Articles of Incorporation.
        
        Returns:
        - str: A message indicating the submission status.
        """
        if self.validate():
            # Here we might save to a database or send to an API, etc.
            return f"Articles of Incorporation for {self.business_name} have been successfully submitted."
        else:
            return "Submission failed due to validation errors."
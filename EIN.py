class EINApplication:
    def __init__(self, business_name, business_address, business_structure, responsible_party, contact_phone, reason_for_applying):
        """
        Initialize an EIN Application with required fields.
        
        Parameters:
        - business_name (str): The legal name of the business.
        - business_address (str): The primary address of the business.
        - business_structure (str): The type of business entity (e.g., LLC, Corporation, Sole Proprietorship).
        - responsible_party (str): The name of the individual responsible for the business.
        - contact_phone (str): The phone number for contact purposes.
        - reason_for_applying (str): Reason for applying for an EIN (e.g., started a new business, hired employees).
        """
        self.business_name = business_name
        self.business_address = business_address
        self.business_structure = business_structure
        self.responsible_party = responsible_party
        self.contact_phone = contact_phone
        self.reason_for_applying = reason_for_applying

    def display_info(self):
        """
        Display the details of the EIN Application.
        """
        print("=== EIN Application ===")
        print(f"Business Name            : {self.business_name}")
        print(f"Business Address         : {self.business_address}")
        print(f"Business Structure       : {self.business_structure}")
        print(f"Responsible Party        : {self.responsible_party}")
        print(f"Contact Phone            : {self.contact_phone}")
        print(f"Reason for Applying      : {self.reason_for_applying}")
    
    def validate(self):
        """
        Validate required fields to ensure all fields are completed and valid.
        
        Returns:
        - bool: True if all fields are valid, otherwise False.
        """
        required_fields = [
            self.business_name, 
            self.business_address, 
            self.business_structure, 
            self.responsible_party, 
            self.contact_phone, 
            self.reason_for_applying
        ]
        
        if any(not field for field in required_fields):
            print("Error: All fields must be completed.")
            return False
        if not isinstance(self.contact_phone, str) or len(self.contact_phone) < 10:
            print("Error: A valid contact phone number is required.")
            return False
        return True

    def submit(self):
        """
        Simulate submitting the EIN Application.
        
        Returns:
        - str: A message indicating the submission status.
        """
        if self.validate():
            # Here we might save to a database or send to an API, etc.
            return f"EIN Application for {self.business_name} has been successfully submitted."
        else:
            return "Submission failed due to validation errors."
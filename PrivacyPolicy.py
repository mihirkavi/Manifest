from datetime import datetime

class PrivacyPolicy:
    def __init__(self, company_name, effective_date):
        """
        Initialize a Privacy Policy for a specific company.
        
        Parameters:
        - company_name (str): The name of the company.
        - effective_date (str): The date the policy becomes effective (format: 'YYYY-MM-DD').
        """
        try:
            self.effective_date = datetime.strptime(effective_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        self.company_name = company_name
        self.data_collection = ""
        self.data_usage = ""
        self.data_sharing = ""
        self.user_rights = ""
        self.security_measures = ""

    def set_data_collection(self, collection_info):
        """Define data collection practices."""
        self.data_collection = collection_info

    def set_data_usage(self, usage_info):
        """Define how collected data is used."""
        self.data_usage = usage_info

    def set_data_sharing(self, sharing_info):
        """Define data sharing practices with third parties."""
        self.data_sharing = sharing_info

    def set_user_rights(self, rights_info):
        """Define user rights regarding their data."""
        self.user_rights = rights_info

    def set_security_measures(self, security_info):
        """Define the security measures taken to protect user data."""
        self.security_measures = security_info

    def display_privacy_policy(self):
        """Display the complete privacy policy."""
        print(f"=== Privacy Policy of {self.company_name} ===")
        print(f"Effective Date       : {self.effective_date.strftime('%Y-%m-%d')}")
        print("\nData Collection:")
        print(f"  {self.data_collection}")
        
        print("\nData Usage:")
        print(f"  {self.data_usage}")
        
        print("\nData Sharing:")
        print(f"  {self.data_sharing}")
        
        print("\nUser Rights:")
        print(f"  {self.user_rights}")
        
        print("\nSecurity Measures:")
        print(f"  {self.security_measures}")

class TermsOfService:
    def __init__(self, company_name, effective_date):
        """
        Initialize Terms of Service for a specific company.
        
        Parameters:
        - company_name (str): The name of the company.
        - effective_date (str): The date the terms become effective (format: 'YYYY-MM-DD').
        """
        try:
            self.effective_date = datetime.strptime(effective_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        self.company_name = company_name
        self.user_obligations = ""
        self.acceptable_use = ""
        self.liability = ""
        self.account_termination = ""
        self.other_terms = ""

    def set_user_obligations(self, obligations_info):
        """Define user obligations under the terms of service."""
        self.user_obligations = obligations_info

    def set_acceptable_use(self, acceptable_use_info):
        """Define acceptable use policy for the service."""
        self.acceptable_use = acceptable_use_info

    def set_liability(self, liability_info):
        """Define the company's liability terms."""
        self.liability = liability_info

    def set_account_termination(self, termination_info):
        """Define account termination policy."""
        self.account_termination = termination_info

    def set_other_terms(self, other_terms_info):
        """Define any other relevant terms."""
        self.other_terms = other_terms_info

    def display_terms_of_service(self):
        """Display the complete terms of service."""
        print(f"=== Terms of Service of {self.company_name} ===")
        print(f"Effective Date       : {self.effective_date.strftime('%Y-%m-%d')}")
        
        print("\nUser Obligations:")
        print(f"  {self.user_obligations}")
        
        print("\nAcceptable Use:")
        print(f"  {self.acceptable_use}")
        
        print("\nLiability:")
        print(f"  {self.liability}")
        
        print("\nAccount Termination:")
        print(f"  {self.account_termination}")
        
        print("\nOther Terms:")
        print(f"  {self.other_terms}")
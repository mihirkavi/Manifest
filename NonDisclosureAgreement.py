from datetime import datetime

class NonDisclosureAgreement:
    def __init__(self, disclosing_party, receiving_party, effective_date, confidentiality_period):
        """
        Initialize a Non-Disclosure Agreement (NDA) between two parties.
        
        Parameters:
        - disclosing_party (str): The name of the party disclosing the confidential information.
        - receiving_party (str): The name of the party receiving the confidential information.
        - effective_date (str): The date the NDA takes effect (format: 'YYYY-MM-DD').
        - confidentiality_period (int): The duration of confidentiality in years.
        """
        try:
            self.effective_date = datetime.strptime(effective_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        self.disclosing_party = disclosing_party
        self.receiving_party = receiving_party
        self.confidentiality_period = confidentiality_period
        self.confidential_information = ""
        self.exclusions = []
        self.terms = []

    def add_confidential_information(self, information):
        """
        Set the confidential information covered by the NDA.
        
        Parameters:
        - information (str): Description of the confidential information.
        """
        self.confidential_information = information

    def add_exclusion(self, exclusion):
        """
        Add an exclusion to the NDA (e.g., information already known or publicly available).
        
        Parameters:
        - exclusion (str): Description of information excluded from confidentiality.
        """
        self.exclusions.append(exclusion)

    def add_term(self, term):
        """
        Add a specific term or condition to the NDA.
        
        Parameters:
        - term (str): A specific term or condition related to confidentiality.
        """
        self.terms.append(term)

    def display_agreement(self):
        """
        Display the full Non-Disclosure Agreement.
        """
        expiry_date = self.effective_date.replace(year=self.effective_date.year + self.confidentiality_period).strftime("%Y-%m-%d")
        
        print("=== Non-Disclosure Agreement (NDA) ===")
        print(f"Disclosing Party         : {self.disclosing_party}")
        print(f"Receiving Party          : {self.receiving_party}")
        print(f"Effective Date           : {self.effective_date.strftime('%Y-%m-%d')}")
        print(f"Confidentiality Expires  : {expiry_date}")
        print(f"Confidential Information : {self.confidential_information}")
        
        print("\nExclusions:")
        for exclusion in self.exclusions:
            print(f"  - {exclusion}")
        
        print("\nTerms and Conditions:")
        for term in self.terms:
            print(f"  - {term}")

    def is_expired(self):
        """
        Check if the NDA has expired based on the confidentiality period.
        
        Returns:
        - bool: True if the NDA has expired, otherwise False.
        """
        expiry_date = self.effective_date.replace(year=self.effective_date.year + self.confidentiality_period)
        return datetime.now() > expiry_date
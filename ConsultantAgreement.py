from datetime import datetime

class ConsultantAgreement:
    def __init__(self, consultant_name, company_name, start_date, end_date):
        """
        Initialize a Consultant Agreement between a company and a consultant.
        
        Parameters:
        - consultant_name (str): The name of the consultant.
        - company_name (str): The name of the company.
        - start_date (str): The start date of the agreement (format: 'YYYY-MM-DD').
        - end_date (str): The end date of the agreement (format: 'YYYY-MM-DD').
        """
        try:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        self.consultant_name = consultant_name
        self.company_name = company_name
        self.scope_of_work = ""
        self.payment_terms = ""
        self.confidentiality_clause = ""
        self.intellectual_property_clause = ""
        self.termination_conditions = ""

    def set_scope_of_work(self, scope):
        """
        Define the scope of work for the consultant.
        
        Parameters:
        - scope (str): Description of the work the consultant will perform.
        """
        self.scope_of_work = scope

    def set_payment_terms(self, terms):
        """
        Define the payment terms for the consultant.
        
        Parameters:
        - terms (str): Description of payment terms (e.g., hourly rate, payment schedule).
        """
        self.payment_terms = terms

    def set_confidentiality_clause(self, clause):
        """
        Define the confidentiality clause in the agreement.
        
        Parameters:
        - clause (str): Description of confidentiality obligations for the consultant.
        """
        self.confidentiality_clause = clause

    def set_intellectual_property_clause(self, clause):
        """
        Define the intellectual property rights clause in the agreement.
        
        Parameters:
        - clause (str): Description of IP ownership rights for work created by the consultant.
        """
        self.intellectual_property_clause = clause

    def set_termination_conditions(self, conditions):
        """
        Define the termination conditions of the agreement.
        
        Parameters:
        - conditions (str): Conditions under which the agreement can be terminated.
        """
        self.termination_conditions = conditions

    def display_agreement(self):
        """
        Display the complete consultant agreement.
        """
        print(f"=== Consultant Agreement between {self.company_name} and {self.consultant_name} ===")
        print(f"Start Date               : {self.start_date.strftime('%Y-%m-%d')}")
        print(f"End Date                 : {self.end_date.strftime('%Y-%m-%d')}")
        
        print("\nScope of Work:")
        print(f"  {self.scope_of_work}")
        
        print("\nPayment Terms:")
        print(f"  {self.payment_terms}")
        
        print("\nConfidentiality Clause:")
        print(f"  {self.confidentiality_clause}")
        
        print("\nIntellectual Property Clause:")
        print(f"  {self.intellectual_property_clause}")
        
        print("\nTermination Conditions:")
        print(f"  {self.termination_conditions}")
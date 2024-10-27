class IntellectualPropertyAgreement:
    def __init__(self, company_name, company_address, parties, confidentiality_clause, usage_rights, transfer_conditions):
        """
        Initialize an Intellectual Property Agreement with required fields.

        Parameters:
        - company_name (str): The name of the company owning the IP.
        - company_address (str): The primary address of the company.
        - parties (list): A list of names of the parties involved in the agreement.
        - confidentiality_clause (str): Clause specifying confidentiality requirements.
        - usage_rights (str): Terms outlining the rights and limitations for using the IP.
        - transfer_conditions (str): Conditions under which the IP ownership may be transferred.
        """
        self.company_name = company_name
        self.company_address = company_address
        self.parties = parties
        self.confidentiality_clause = confidentiality_clause
        self.usage_rights = usage_rights
        self.transfer_conditions = transfer_conditions
        self.patents = []
        self.copyrights = []
        self.trademarks = []

    def add_patent(self, patent_name, inventor, patent_number, filing_date, expiration_date):
        self.patents.append(self.Patent(patent_name, inventor, patent_number, filing_date, expiration_date))

    def add_copyright(self, title, author, registration_number, registration_date, work_type):
        self.copyrights.append(self.Copyright(title, author, registration_number, registration_date, work_type))

    def add_trademark(self, trademark_name, owner, registration_number, registration_date, description):
        self.trademarks.append(self.Trademark(trademark_name, owner, registration_number, registration_date, description))

    def display_info(self):
        """
        Display the details of the Intellectual Property Agreement.
        """
        print("=== Intellectual Property Agreement ===")
        print(f"Company Name              : {self.company_name}")
        print(f"Company Address           : {self.company_address}")
        print(f"Parties Involved          : {', '.join(self.parties)}")
        print(f"Confidentiality Clause    : {self.confidentiality_clause}")
        print(f"Usage Rights              : {self.usage_rights}")
        print(f"Transfer Conditions       : {self.transfer_conditions}")
        print("\nPatents:")
        for patent in self.patents:
            patent.display_info()
        print("\nCopyrights:")
        for copyright in self.copyrights:
            copyright.display_info()
        print("\nTrademarks:")
        for trademark in self.trademarks:
            trademark.display_info()

    def validate(self):
        """
        Validate required fields to ensure all fields are completed and valid.
        
        Returns:
        - bool: True if all fields are valid, otherwise False.
        """
        required_fields = [
            self.company_name, 
            self.company_address, 
            self.parties, 
            self.confidentiality_clause, 
            self.usage_rights, 
            self.transfer_conditions
        ]
        
        if any(not field for field in required_fields):
            print("Error: All fields must be completed.")
            return False
        if not isinstance(self.parties, list) or not all(isinstance(party, str) for party in self.parties):
            print("Error: Parties must be a list of names.")
            return False
        return True

    def submit(self):
        """
        Simulate submitting the Intellectual Property Agreement.
        
        Returns:
        - str: A message indicating the submission status.
        """
        if self.validate():
            # Here we might save to a database or send to an API, etc.
            return f"Intellectual Property Agreement for {self.company_name} has been successfully submitted."
        else:
            return "Submission failed due to validation errors."

    class Patent:
        def __init__(self, patent_name, inventor, patent_number, filing_date, expiration_date):
            self.patent_name = patent_name
            self.inventor = inventor
            self.patent_number = patent_number
            self.filing_date = filing_date
            self.expiration_date = expiration_date

        def display_info(self):
            print(f"  - Patent Name          : {self.patent_name}")
            print(f"    Inventor             : {self.inventor}")
            print(f"    Patent Number        : {self.patent_number}")
            print(f"    Filing Date          : {self.filing_date}")
            print(f"    Expiration Date      : {self.expiration_date}")

    class Copyright:
        def __init__(self, title, author, registration_number, registration_date, work_type):
            self.title = title
            self.author = author
            self.registration_number = registration_number
            self.registration_date = registration_date
            self.work_type = work_type

        def display_info(self):
            print(f"  - Title                : {self.title}")
            print(f"    Author               : {self.author}")
            print(f"    Registration Number  : {self.registration_number}")
            print(f"    Registration Date    : {self.registration_date}")
            print(f"    Work Type            : {self.work_type}")

    class Trademark:
        def __init__(self, trademark_name, owner, registration_number, registration_date, description):
            self.trademark_name = trademark_name
            self.owner = owner
            self.registration_number = registration_number
            self.registration_date = registration_date
            self.description = description

        def display_info(self):
            print(f"  - Trademark Name       : {self.trademark_name}")
            print(f"    Owner                : {self.owner}")
            print(f"    Registration Number  : {self.registration_number}")
            print(f"    Registration Date    : {self.registration_date}")
            print(f"    Description          : {self.description}")
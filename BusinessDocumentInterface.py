from abc import ABC, abstractmethod
from datetime import datetime

class BusinessDocumentInterface(ABC):
    def __init__(self, company_name, effective_date):
        """
        Initialize a business document with common attributes.
        
        Parameters:
        - company_name (str): The name of the company.
        - effective_date (str): The date the document becomes effective (format: 'YYYY-MM-DD').
        """
        self.company_name = company_name
        try:
            self.effective_date = datetime.strptime(effective_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
    @abstractmethod
    def set_parties_involved(self, parties):
        """
        Set the parties involved in the document (e.g., individuals, entities).
        
        Parameters:
        - parties (list): List of parties involved in the document.
        """
        pass

    @abstractmethod
    def set_terms_and_conditions(self, terms):
        """
        Set the terms and conditions of the document.
        
        Parameters:
        - terms (str): Description of the terms and conditions.
        """
        pass

    @abstractmethod
    def display_document(self):
        """
        Display the document details. Each subclass should implement this to display specific document content.
        """
        pass
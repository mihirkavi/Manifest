class InvestmentAgreement:
    def __init__(self, company_name):
        """
        Initialize an Investment Agreement for a company.
        
        Parameters:
        - company_name (str): The name of the company.
        """
        self.company_name = company_name
        self.investments = []

    def add_investor(self, investor_name, investment_amount, equity_percentage, rights_and_privileges, responsibilities):
        """
        Add an investment agreement for a new investor.
        
        Parameters:
        - investor_name (str): The name of the investor.
        - investment_amount (float): The amount of money invested by the investor.
        - equity_percentage (float): The percentage of equity granted to the investor.
        - rights_and_privileges (str): Special rights or privileges granted to the investor.
        - responsibilities (str): Responsibilities expected from the investor.
        
        Returns:
        - str: A message indicating the addition status.
        """
        if investment_amount <= 0 or equity_percentage <= 0:
            return "Investment amount and equity percentage must be positive."
        agreement = {
            "Investor Name": investor_name,
            "Investment Amount": investment_amount,
            "Equity Percentage": equity_percentage,
            "Rights and Privileges": rights_and_privileges,
            "Responsibilities": responsibilities
        }
        self.investments.append(agreement)
        return f"Added investment agreement for {investor_name}."

    def total_investment(self):
        """
        Calculate the total investment made by all investors.
        
        Returns:
        - float: The total investment amount.
        """
        return sum(agreement["Investment Amount"] for agreement in self.investments)

    def display_agreements(self):
        """
        Display all investment agreements for the company.
        """
        print(f"=== Investment Agreements for {self.company_name} ===")
        print("Investor Name       | Investment ($) | Equity (%) | Rights & Privileges        | Responsibilities")
        print("-----------------------------------------------------------------------------------------")
        for agreement in self.investments:
            print(f"{agreement['Investor Name']:<18} | ${agreement['Investment Amount']:<13,.2f} | {agreement['Equity Percentage']:<10.2f}% | {agreement['Rights and Privileges']:<25} | {agreement['Responsibilities']}")
        print("-----------------------------------------------------------------------------------------")
        print(f"Total Investment    : ${self.total_investment():,.2f}")

    def find_investor(self, investor_name):
        """
        Find and display an investment agreement for a specific investor.
        
        Parameters:
        - investor_name (str): The name of the investor.
        
        Returns:
        - dict or str: The investor's agreement if found, or a message if not found.
        """
        for agreement in self.investments:
            if agreement["Investor Name"] == investor_name:
                return agreement
        return f"No investment agreement found for {investor_name}."

    def update_investment(self, investor_name, new_investment_amount=None, new_equity_percentage=None):
        """
        Update the investment amount and/or equity percentage for an existing investor.
        
        Parameters:
        - investor_name (str): The name of the investor.
        - new_investment_amount (float, optional): The new investment amount.
        - new_equity_percentage (float, optional): The new equity percentage.
        
        Returns:
        - str: A message indicating the update status.
        """
        for agreement in self.investments:
            if agreement["Investor Name"] == investor_name:
                if new_investment_amount is not None and new_investment_amount > 0:
                    agreement["Investment Amount"] = new_investment_amount
                if new_equity_percentage is not None and new_equity_percentage > 0:
                    agreement["Equity Percentage"] = new_equity_percentage
                return f"Updated investment agreement for {investor_name}."
        return f"No investment agreement found for {investor_name}."

    def remove_investor(self, investor_name):
        """
        Remove an investor from the investment agreements.
        
        Parameters:
        - investor_name (str): The name of the investor to remove.
        
        Returns:
        - str: A message indicating the removal status.
        """
        for agreement in self.investments:
            if agreement["Investor Name"] == investor_name:
                self.investments.remove(agreement)
                return f"Removed investment agreement for {investor_name}."
        return f"No investment agreement found for {investor_name}."
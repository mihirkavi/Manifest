class CapitalizationTable:
    def __init__(self, company_name):
        """
        Initialize a Capitalization Table for a company.
        
        Parameters:
        - company_name (str): The name of the company for which the cap table is being created.
        """
        self.company_name = company_name
        self.shareholders = {}

    def add_shareholder(self, name, shares):
        """
        Add a shareholder to the cap table.
        
        Parameters:
        - name (str): The name of the shareholder.
        - shares (int): The number of shares owned by the shareholder.
        
        Returns:
        - str: A message indicating the addition status.
        """
        if shares <= 0:
            return "Share count must be positive."
        if name in self.shareholders:
            self.shareholders[name] += shares
        else:
            self.shareholders[name] = shares
        return f"Added {shares} shares for {name}. Total shares for {name}: {self.shareholders[name]}."

    def total_shares(self):
        """
        Calculate the total number of shares in the cap table.
        
        Returns:
        - int: The total number of shares.
        """
        return sum(self.shareholders.values())

    def ownership_percentage(self, name):
        """
        Calculate the ownership percentage of a shareholder.
        
        Parameters:
        - name (str): The name of the shareholder.
        
        Returns:
        - float: The ownership percentage of the shareholder.
        - str: Message if the shareholder does not exist.
        """
        total = self.total_shares()
        if name not in self.shareholders:
            return f"{name} is not a shareholder."
        return (self.shareholders[name] / total) * 100 if total > 0 else 0.0

    def display_cap_table(self):
        """
        Display the capitalization table with each shareholder's ownership percentage.
        """
        total = self.total_shares()
        print(f"=== Capitalization Table for {self.company_name} ===")
        print("Shareholder           | Shares       | Ownership (%)")
        print("---------------------------------------------------")
        for name, shares in self.shareholders.items():
            percentage = (shares / total * 100) if total > 0 else 0
            print(f"{name:<20} | {shares:<12} | {percentage:.2f}%")
        print("---------------------------------------------------")
        print(f"Total Shares          : {total}")

    def remove_shareholder(self, name):
        """
        Remove a shareholder from the cap table.
        
        Parameters:
        - name (str): The name of the shareholder to be removed.
        
        Returns:
        - str: A message indicating the removal status.
        """
        if name in self.shareholders:
            del self.shareholders[name]
            return f"{name} has been removed from the capitalization table."
        return f"{name} is not a shareholder."

    def update_shares(self, name, shares):
        """
        Update the number of shares for an existing shareholder.
        
        Parameters:
        - name (str): The name of the shareholder.
        - shares (int): The new number of shares for the shareholder.
        
        Returns:
        - str: A message indicating the update status.
        """
        if shares < 0:
            return "Share count must be non-negative."
        if name in self.shareholders:
            self.shareholders[name] = shares
            return f"{name}'s shares have been updated to {shares}."
        return f"{name} is not a shareholder."
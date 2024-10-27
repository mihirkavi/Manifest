from datetime import datetime

class SalesContract:
    def __init__(self, seller_name, buyer_name, effective_date):
        """
        Initialize a Sales Contract between a seller and a buyer.
        
        Parameters:
        - seller_name (str): The name of the seller.
        - buyer_name (str): The name of the buyer.
        - effective_date (str): The date the contract takes effect (format: 'YYYY-MM-DD').
        """
        try:
            self.effective_date = datetime.strptime(effective_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        self.seller_name = seller_name
        self.buyer_name = buyer_name
        self.products_services = []
        self.total_amount = 0.0
        self.payment_terms = ""
        self.delivery_terms = ""
        self.warranties = []
        self.termination_conditions = ""

    def add_product_or_service(self, name, description, quantity, unit_price):
        """
        Add a product or service to the contract.
        
        Parameters:
        - name (str): The name of the product or service.
        - description (str): Description of the product or service.
        - quantity (int): The quantity of the product or service.
        - unit_price (float): The price per unit of the product or service.
        
        Returns:
        - str: A message indicating the addition status.
        """
        if quantity <= 0 or unit_price <= 0:
            return "Quantity and unit price must be positive."
        
        product = {
            "Name": name,
            "Description": description,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Total Price": quantity * unit_price
        }
        self.products_services.append(product)
        self.total_amount += product["Total Price"]
        return f"Product/Service '{name}' has been added."

    def set_payment_terms(self, terms):
        """
        Set the payment terms of the contract.
        
        Parameters:
        - terms (str): Description of payment terms (e.g., "Net 30").
        """
        self.payment_terms = terms

    def set_delivery_terms(self, terms):
        """
        Set the delivery terms of the contract.
        
        Parameters:
        - terms (str): Description of delivery terms (e.g., "Delivery within 14 days of order").
        """
        self.delivery_terms = terms

    def add_warranty(self, warranty):
        """
        Add a warranty to the contract.
        
        Parameters:
        - warranty (str): A specific warranty or guarantee (e.g., "1-year product warranty").
        """
        self.warranties.append(warranty)

    def set_termination_conditions(self, conditions):
        """
        Set the conditions under which the contract can be terminated.
        
        Parameters:
        - conditions (str): Conditions for contract termination.
        """
        self.termination_conditions = conditions

    def display_contract(self):
        """
        Display the complete sales contract.
        """
        print("=== Sales Contract ===")
        print(f"Seller               : {self.seller_name}")
        print(f"Buyer                : {self.buyer_name}")
        print(f"Effective Date       : {self.effective_date.strftime('%Y-%m-%d')}")
        print("\nProducts/Services:")
        print("Name                | Description           | Quantity | Unit Price | Total Price")
        print("-------------------------------------------------------------------------------")
        for item in self.products_services:
            print(f"{item['Name']:<20} | {item['Description']:<20} | {item['Quantity']:<8} | ${item['Unit Price']:<10,.2f} | ${item['Total Price']:<10,.2f}")
        print("-------------------------------------------------------------------------------")
        print(f"Total Amount         : ${self.total_amount:,.2f}")
        print(f"\nPayment Terms        : {self.payment_terms}")
        print(f"Delivery Terms       : {self.delivery_terms}")
        
        print("\nWarranties:")
        for warranty in self.warranties:
            print(f"  - {warranty}")
        
        print(f"\nTermination Conditions: {self.termination_conditions}")

    def get_total_amount(self):
        """
        Get the total amount of the contract.
        
        Returns:
        - float: The total amount for the contract.
        """
        return self.total_amount
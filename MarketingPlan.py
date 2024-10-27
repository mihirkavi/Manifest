class MarketingPlan:
    def __init__(self, product_name, year):
        """
        Initialize a Marketing Plan for a specific product and year.
        
        Parameters:
        - product_name (str): The name of the product or service being marketed.
        - year (int): The year the marketing plan is for.
        """
        self.product_name = product_name
        self.year = year
        self.target_markets = []
        self.objectives = []
        self.strategies = []
        self.tactics = []
        self.budget = 0.0
        self.kpis = []

    def add_target_market(self, market_segment):
        """
        Add a target market segment to the plan.
        
        Parameters:
        - market_segment (str): Description of the target market segment.
        """
        self.target_markets.append(market_segment)

    def add_objective(self, objective):
        """
        Add a marketing objective to the plan.
        
        Parameters:
        - objective (str): A specific objective of the marketing plan.
        """
        self.objectives.append(objective)

    def add_strategy(self, strategy):
        """
        Add a strategy to the marketing plan.
        
        Parameters:
        - strategy (str): A high-level approach for achieving the objectives.
        """
        self.strategies.append(strategy)

    def add_tactic(self, tactic):
        """
        Add a tactic to the marketing plan.
        
        Parameters:
        - tactic (str): A specific action to execute the strategy.
        """
        self.tactics.append(tactic)

    def set_budget(self, amount):
        """
        Set the total marketing budget.
        
        Parameters:
        - amount (float): The budget amount.
        
        Returns:
        - str: A message indicating the budget status.
        """
        if amount < 0:
            return "Budget amount must be non-negative."
        self.budget = amount
        return f"Budget set to ${self.budget:,.2f}"

    def add_kpi(self, kpi):
        """
        Add a Key Performance Indicator (KPI) to measure success.
        
        Parameters:
        - kpi (str): Description of a measurable performance indicator.
        """
        self.kpis.append(kpi)

    def display_plan(self):
        """
        Display the complete marketing plan.
        """
        print(f"=== Marketing Plan for {self.product_name} ({self.year}) ===")
        print("\nTarget Markets:")
        for market in self.target_markets:
            print(f"  - {market}")
        
        print("\nObjectives:")
        for obj in self.objectives:
            print(f"  - {obj}")
        
        print("\nStrategies:")
        for strategy in self.strategies:
            print(f"  - {strategy}")
        
        print("\nTactics:")
        for tactic in self.tactics:
            print(f"  - {tactic}")
        
        print(f"\nBudget: ${self.budget:,.2f}")
        
        print("\nKey Performance Indicators (KPIs):")
        for kpi in self.kpis:
            print(f"  - {kpi}")

    def get_total_budget(self):
        """
        Get the total budget for the marketing plan.
        
        Returns:
        - float: The total marketing budget.
        """
        return self.budget
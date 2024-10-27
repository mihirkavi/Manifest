from Idea import Idea
from BusinessModelCanvas import BusinessModelCanvas
# Legal Formation and Structure
from ArticlesOfIncorporation import ArticlesOfIncorporation
from OperatingAgreement import OperatingAgreement
from ShareholdersAgreement import ShareholdersAgreement
from FoundersAgreement import FoundersAgreement
# Compliance
from EIN import EINApplication
from IntellectualProperty import IntellectualPropertyAgreement
# Financial Documents
from BankAccount import BankAccount
from CapitalizationTable import CapitalizationTable
from InvestmentAgreement import InvestmentAgreement
# Product Development and IP
from ProductRoadmap import ProductRoadmap
from NonDisclosureAgreement import NonDisclosureAgreement
# Sales and Marketing
from MarketingPlan import MarketingPlan
from SalesContract import SalesContract
# Human Resources
#from EmployeeContract import EmployeeContract, OfferLetter
from EmployeeHandbook import EmployeeHandbook
from ConsultantAgreement import ConsultantAgreement
# Operational Documents
#from StandardOperatingProcedure import StandardOperatingProcedure
from PrivacyPolicy import PrivacyPolicy, TermsOfService
# Interface Class
from BusinessDocumentInterface import BusinessDocumentInterface


idea = Idea("Blockchain for water")
business_model_canvas = BusinessModelCanvas()

# Creating an instance of the ArticlesOfIncorporation
articles = ArticlesOfIncorporation(
    business_name="Tech Innovations Inc.",
    business_purpose="Develop and sell innovative tech products.",
    business_address="123 Innovation Drive, Silicon Valley, CA",
    registered_agent="John Doe",
    shares_authorized=10000,
    incorporator_name="Jane Smith"
)

# Display information
articles.display_info()

# Attempt to submit the document
print(articles.submit())

#Operating agreement usage
# Creating an instance of the Operating Agreement
operating_agreement = OperatingAgreement(
    llc_name="Green Energy Solutions LLC",
    business_address="456 Sustainability Avenue, Austin, TX",
    members={"Alice Johnson": 50, "Bob Smith": 50},
    management_structure="Member-managed",
    profit_distribution="Profits and losses will be distributed according to ownership percentage.",
    dissolution_terms="The LLC will be dissolved upon mutual agreement of all members or if no active members remain."
)

# Display information
operating_agreement.display_info()

# Attempt to submit the document
print(operating_agreement.submit())


# Creating an instance of the Shareholders Agreement
shareholders_agreement = ShareholdersAgreement(
    company_name="Tech Ventures Inc.",
    business_address="789 Innovation Blvd, San Francisco, CA",
    shareholders={"Alice Green": 40, "Bob Blue": 30, "Charlie Red": 30},
    board_structure="The board consists of a CEO, CFO, and CTO with equal decision-making authority.",
    share_transfer_restrictions="Shares cannot be transferred without board approval.",
    voting_rights="Each share entitles the holder to one vote on major company decisions.",
    dividend_policy="Dividends will be distributed based on ownership percentage, subject to board approval.",
    termination_conditions="The company will be dissolved upon unanimous shareholder agreement or court order."
)

# Display information
shareholders_agreement.display_info()

# Attempt to submit the document
print(shareholders_agreement.submit())


# Creating an instance of the Founders' Agreement
founders_agreement = FoundersAgreement(
    startup_name="Smart Solutions Inc.",
    business_address="101 Startup Lane, New York, NY",
    founders=["Alice Johnson", "Bob Smith"],
    roles_responsibilities={
        "Alice Johnson": "CEO, responsible for overall business strategy and fundraising.",
        "Bob Smith": "CTO, responsible for product development and technical leadership."
    },
    ownership_percentage={"Alice Johnson": 60, "Bob Smith": 40},
    vesting_schedule="4-year vesting with a 1-year cliff.",
    ip_assignment="All IP developed under the company belongs to Smart Solutions Inc.",
    exit_conditions="A founder must offer shares to other founders before selling externally; terms apply if a founder exits within the first 2 years."
)

# Display information
founders_agreement.display_info()

# Attempt to submit the document
print(founders_agreement.submit())


# Creating an instance of the EIN Application
ein_application = EINApplication(
    business_name="NextGen Solutions LLC",
    business_address="123 Business Park, Miami, FL",
    business_structure="LLC",
    responsible_party="Jane Doe",
    contact_phone="123-456-7890",
    reason_for_applying="Started a new business"
)

# Display information
ein_application.display_info()

# Attempt to submit the document
print(ein_application.submit())

# Creating an instance of the Intellectual Property Agreement
ip_agreement = IntellectualPropertyAgreement(
    company_name="Innovative AI Corp",
    company_address="456 AI Blvd, San Francisco, CA",
    parties=["Alice Green", "Bob Blue", "Innovative AI Corp"],
    confidentiality_clause="All parties must keep proprietary information confidential and not disclose it without consent.",
    usage_rights="The company retains exclusive rights to use, modify, and distribute the IP.",
    transfer_conditions="IP ownership may be transferred only upon board approval and written agreement."
)

# Adding a patent
ip_agreement.add_patent(
    patent_name="Smart AI Algorithm",
    inventor="Alice Green",
    patent_number="US1234567A",
    filing_date="2023-01-01",
    expiration_date="2043-01-01"
)

# Adding a copyright
ip_agreement.add_copyright(
    title="Innovative AI Handbook",
    author="Bob Blue",
    registration_number="TX123456",
    registration_date="2023-06-01",
    work_type="Literary Work"
)

# Adding a trademark
ip_agreement.add_trademark(
    trademark_name="Innovative AI",
    owner="Innovative AI Corp",
    registration_number="TM789012",
    registration_date="2023-07-15",
    description="Logo and brand name for AI products."
)

# Display information
ip_agreement.display_info()

# Attempt to submit the document
print(ip_agreement.submit())

# Creating an instance of the BankAccount
account = BankAccount(
    account_holder="John Doe",
    account_number="123456789",
    bank_name="ABC Bank",
    balance=500.0
)

# Display account information
account.display_info()

# Deposit money
print(account.deposit(150.0))

# Withdraw money
print(account.withdraw(200.0))

# Check balance
print(f"Current Balance: ${account.get_balance():.2f}")

# Creating an instance of the Capitalization Table
cap_table = CapitalizationTable(company_name="Tech Innovators Inc.")

# Adding shareholders
print(cap_table.add_shareholder("Alice Johnson", 5000))
print(cap_table.add_shareholder("Bob Smith", 3000))
print(cap_table.add_shareholder("Charlie Brown", 2000))

# Display the cap table
cap_table.display_cap_table()

# Update shares for an existing shareholder
print(cap_table.update_shares("Bob Smith", 3500))

# Calculate ownership percentage
print(f"Alice Johnson's Ownership: {cap_table.ownership_percentage('Alice Johnson'):.2f}%")

# Remove a shareholder
print(cap_table.remove_shareholder("Charlie Brown"))

# Display updated cap table
cap_table.display_cap_table()

# Creating an instance of the Investment Agreement
investment_agreements = InvestmentAgreement(company_name="Green Energy Solutions")

# Adding investors
print(investment_agreements.add_investor(
    investor_name="Alice Johnson", 
    investment_amount=500000.0, 
    equity_percentage=20.0, 
    rights_and_privileges="Board Observer Rights", 
    responsibilities="Attend quarterly board meetings"
))

print(investment_agreements.add_investor(
    investor_name="Bob Smith", 
    investment_amount=300000.0, 
    equity_percentage=15.0, 
    rights_and_privileges="Voting Rights", 
    responsibilities="Approve major financial decisions"
))

# Display all investment agreements
investment_agreements.display_agreements()

# Find a specific investor's agreement
print(investment_agreements.find_investor("Alice Johnson"))

# Update an investor's equity
print(investment_agreements.update_investment("Bob Smith", new_equity_percentage=18.0))

# Remove an investor
print(investment_agreements.remove_investor("Alice Johnson"))

# Display updated investment agreements
investment_agreements.display_agreements()


# Creating an instance of the Product Roadmap
product_roadmap = ProductRoadmap(product_name="AI Analytics Platform")

# Adding milestones
print(product_roadmap.add_milestone(
    milestone_name="MVP Release",
    description="Release the minimum viable product.",
    estimated_completion="2024-12-31",
    responsible_team="Development Team"
))

print(product_roadmap.add_milestone(
    milestone_name="Feature Enhancement",
    description="Add advanced analytics features.",
    estimated_completion="2025-06-30",
    responsible_team="Product Team"
))

# Adding features to milestones
print(product_roadmap.add_feature_to_milestone(
    milestone_name="MVP Release",
    feature_name="User Authentication",
    feature_description="Implement basic login and registration functionality."
))

print(product_roadmap.add_feature_to_milestone(
    milestone_name="Feature Enhancement",
    feature_name="Predictive Analytics",
    feature_description="Implement predictive analytics for data insights."
))

# Display the entire roadmap
product_roadmap.display_roadmap()

# Update milestone date
print(product_roadmap.update_milestone_date("MVP Release", "2025-01-15"))

# Remove a milestone
print(product_roadmap.remove_milestone("Feature Enhancement"))

# Display updated roadmap
product_roadmap.display_roadmap()


# Creating an instance of the Non-Disclosure Agreement
nda = NonDisclosureAgreement(
    disclosing_party="Tech Innovators Inc.",
    receiving_party="John Doe",
    effective_date="2024-01-01",
    confidentiality_period=3
)

# Setting the confidential information
nda.add_confidential_information("Proprietary technology and product designs.")

# Adding exclusions
nda.add_exclusion("Information already known to the receiving party.")
nda.add_exclusion("Information that becomes publicly available without breach.")

# Adding terms
nda.add_term("The receiving party shall not disclose the confidential information to any third party.")
nda.add_term("The receiving party shall use the confidential information solely for evaluation purposes.")

# Display the NDA
nda.display_agreement()

# Check if the NDA has expired
print("Is the NDA expired?", nda.is_expired())

# Creating an instance of the Marketing Plan
marketing_plan = MarketingPlan(product_name="Eco-Friendly Water Bottle", year=2024)

# Adding target markets
marketing_plan.add_target_market("Environmentally conscious consumers")
marketing_plan.add_target_market("Young professionals")

# Adding objectives
marketing_plan.add_objective("Increase brand awareness by 50% in target markets")
marketing_plan.add_objective("Achieve a 20% increase in sales by year-end")

# Adding strategies
marketing_plan.add_strategy("Use social media influencers to reach target markets")
marketing_plan.add_strategy("Offer special discounts for bulk purchases")

# Adding tactics
marketing_plan.add_tactic("Launch a social media campaign with eco-influencers")
marketing_plan.add_tactic("Partner with local stores to increase product visibility")

# Setting the budget
print(marketing_plan.set_budget(50000.0))

# Adding KPIs
marketing_plan.add_kpi("Number of new social media followers")
marketing_plan.add_kpi("Sales revenue generated from new customers")

# Display the full marketing plan
marketing_plan.display_plan()

# Get the total budget
print(f"Total Marketing Budget: ${marketing_plan.get_total_budget():,.2f}")

# Creating an instance of the Sales Contract
contract = SalesContract(
    seller_name="Green Tech Supplies",
    buyer_name="Eco Builders Inc.",
    effective_date="2024-11-01"
)

# Adding products or services
print(contract.add_product_or_service(
    name="Solar Panel",
    description="High-efficiency solar panel",
    quantity=100,
    unit_price=250.0
))

print(contract.add_product_or_service(
    name="Battery Storage",
    description="Energy storage system",
    quantity=20,
    unit_price=500.0
))

# Setting payment and delivery terms
contract.set_payment_terms("50% upfront, 50% upon delivery")
contract.set_delivery_terms("Delivery within 30 days of order confirmation")

# Adding warranties and termination conditions
contract.add_warranty("2-year warranty on all solar panels")
contract.add_warranty("1-year warranty on battery storage")
contract.set_termination_conditions("Either party may terminate with 30-day written notice if terms are breached")

# Display the full contract
contract.display_contract()

# Get the total amount of the contract
print(f"Total Contract Amount: ${contract.get_total_amount():,.2f}")


# Creating an instance of the Employee Contract
employee_contract = EmployeeContract(
    employee_name="John Doe",
    position="Software Engineer",
    start_date="2024-11-01",
    salary=90000.0,
    employment_type="Full-Time"
)

# Adding benefits, confidentiality clause, and termination conditions
employee_contract.add_benefit("Health Insurance")
employee_contract.add_benefit("401(k) Retirement Plan")
employee_contract.set_confidentiality_clause("The employee agrees to maintain the confidentiality of all proprietary information.")
employee_contract.set_termination_conditions("The company may terminate employment with a 30-day notice if performance requirements are not met.")

# Display the full employee contract
employee_contract.display_contract()

# Creating an instance of the Offer Letter
offer_letter = OfferLetter(
    employee_name="John Doe",
    position="Software Engineer",
    start_date="2024-11-01",
    starting_salary=90000.0,
    hiring_manager="Jane Smith"
)

# Display the offer letter
offer_letter.display_offer_letter()

# Creating an instance of the Employee Handbook
handbook = EmployeeHandbook(company_name="Tech Innovations Inc.")

# Adding company values
handbook.add_company_value("Integrity and honesty in all business dealings.")
handbook.add_company_value("Commitment to sustainable practices and eco-friendly solutions.")

# Adding code of conduct rules
handbook.add_code_of_conduct("Respectful communication with all colleagues and clients.")
handbook.add_code_of_conduct("Maintain confidentiality of company and client information.")

# Adding employee benefits
handbook.add_employee_benefit("Comprehensive health insurance")
handbook.add_employee_benefit("Paid parental leave")
handbook.add_employee_benefit("401(k) retirement plan with company matching")

# Setting policies
handbook.set_attendance_policy("Employees are expected to arrive on time and notify management in case of absence.")
handbook.set_leave_policy("Employees accrue vacation days based on their length of service. Sick leave is provided as per company policy.")
handbook.set_termination_policy("The company may terminate employment for violations of conduct, performance issues, or downsizing.")

# Adding workplace rules
handbook.add_workplace_rule("No personal devices are allowed on the production floor.")
handbook.add_workplace_rule("Work areas should be kept clean and organized.")

# Display the complete handbook
handbook.display_handbook()

# Creating an instance of the Consultant Agreement
consultant_agreement = ConsultantAgreement(
    consultant_name="Alex Johnson",
    company_name="Tech Innovations Inc.",
    start_date="2024-01-01",
    end_date="2024-12-31"
)

# Setting the scope of work, payment terms, confidentiality clause, and termination conditions
consultant_agreement.set_scope_of_work("Provide software development and consulting services on project XYZ.")
consultant_agreement.set_payment_terms("Hourly rate of $100, payable bi-weekly upon submission of timesheets.")
consultant_agreement.set_confidentiality_clause("Consultant agrees to keep all company information confidential during and after the contract period.")
consultant_agreement.set_intellectual_property_clause("All IP developed during the contract shall be the property of Tech Innovations Inc.")
consultant_agreement.set_termination_conditions("Either party may terminate with a 30-day written notice. Immediate termination in case of breach of contract.")

# Display the full agreement
consultant_agreement.display_agreement()


# Creating an instance of the Standard Operating Procedure
sop = StandardOperatingProcedure(
    procedure_name="Customer Complaint Handling",
    department="Customer Service",
    effective_date="2024-01-01",
    version="1.0"
)

# Adding steps to the SOP
sop.add_step("Receive the complaint and acknowledge receipt within 24 hours.")
sop.add_step("Classify the complaint based on severity and urgency.")
sop.add_step("Investigate the complaint by consulting relevant teams.")
sop.add_step("Provide a resolution to the customer within 7 business days.")
sop.add_step("Follow up with the customer to ensure satisfaction.")

# Assigning responsibilities
sop.assign_responsibility("Customer Service Representative", "Receive and log complaints.")
sop.assign_responsibility("Quality Assurance Team", "Investigate and analyze complaints.")
sop.assign_responsibility("Customer Service Manager", "Approve resolutions and monitor compliance.")

# Adding reviewers
sop.add_reviewer("Jane Smith", "Quality Control Manager")
sop.add_reviewer("John Doe", "Compliance Officer")

# Setting approval requirements
sop.set_approval_requirements("Approved by Customer Service Manager and Quality Control Manager.")

# Display the full SOP
sop.display_sop()


# Creating an instance of Privacy Policy
privacy_policy = PrivacyPolicy(company_name="Tech Innovations Inc.", effective_date="2024-01-01")
privacy_policy.set_data_collection("We collect data such as name, email, and browsing history.")
privacy_policy.set_data_usage("Data is used to enhance user experience and for targeted advertising.")
privacy_policy.set_data_sharing("Data may be shared with trusted third-party partners for analytics.")
privacy_policy.set_user_rights("Users can request data deletion or modification by contacting support.")
privacy_policy.set_security_measures("We use encryption and secure servers to protect user data.")

# Display the privacy policy
privacy_policy.display_privacy_policy()

# Creating an instance of Terms of Service
terms_of_service = TermsOfService(company_name="Tech Innovations Inc.", effective_date="2024-01-01")
terms_of_service.set_user_obligations("Users must provide accurate information and comply with all terms.")
terms_of_service.set_acceptable_use("Prohibited activities include hacking, spamming, and harassment.")
terms_of_service.set_liability("The company is not liable for damages resulting from misuse of the service.")
terms_of_service.set_account_termination("Accounts may be terminated for violations of terms or inactivity.")
terms_of_service.set_other_terms("These terms may be updated periodically, and users will be notified.")

# Display the terms of service
terms_of_service.display_terms_of_service()
from Idea import Idea
from BusinessModelCanvas import BusinessModelCanvas

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
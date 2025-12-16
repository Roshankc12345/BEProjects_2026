# Create INR-specific expense categories and budget data based on Indian spending patterns
import json

# Indian expense categories with INR budgets and patterns
indian_expense_data = {
    "expense_categories_inr": [
        {
            "category": "Food & Dining",
            "subcategories": ["Restaurants", "Groceries", "Street Food", "Sweets", "Tea/Coffee"],
            "average_monthly_inr": 8000,
            "percentage": 25,
            "description": "Food expenses including groceries, dining out, and traditional Indian foods"
        },
        {
            "category": "Transportation", 
            "subcategories": ["Petrol/Diesel", "Auto/Taxi", "Bus/Metro", "Parking", "Vehicle Maintenance"],
            "average_monthly_inr": 4500,
            "percentage": 15,
            "description": "Transport costs including fuel, public transport, and vehicle expenses"
        },
        {
            "category": "Bills & Utilities",
            "subcategories": ["Electricity", "Water", "Gas (LPG)", "Internet", "Mobile", "DTH/Cable"],
            "average_monthly_inr": 5000,
            "percentage": 18,
            "description": "Monthly utility bills and essential services"
        },
        {
            "category": "Shopping",
            "subcategories": ["Clothing", "Electronics", "Home Items", "Personal Care", "Books"],
            "average_monthly_inr": 6000,
            "percentage": 20,
            "description": "Shopping for clothes, electronics, and personal items"
        },
        {
            "category": "Healthcare",
            "subcategories": ["Medical Bills", "Medicine", "Health Insurance", "Gym/Fitness", "Dental"],
            "average_monthly_inr": 3000,
            "percentage": 8,
            "description": "Healthcare expenses including insurance and medical bills"
        },
        {
            "category": "Entertainment",
            "subcategories": ["Movies", "OTT Subscriptions", "Games", "Events", "Sports"],
            "average_monthly_inr": 2500,
            "percentage": 7,
            "description": "Entertainment and leisure activities"
        },
        {
            "category": "Education",
            "subcategories": ["Fees", "Books", "Online Courses", "Coaching", "Stationery"],
            "average_monthly_inr": 2000,
            "percentage": 4,
            "description": "Educational expenses including fees and learning materials"
        },
        {
            "category": "Investment & Savings",
            "subcategories": ["SIP/Mutual Funds", "FD/RD", "PPF", "Insurance Premium", "Gold"],
            "average_monthly_inr": 6000,
            "percentage": 20,
            "description": "Investments and savings for future financial goals"
        },
        {
            "category": "Family & Personal",
            "subcategories": ["Gifts", "Family Support", "Personal Loan EMI", "Charity", "Festivals"],
            "average_monthly_inr": 3000,
            "percentage": 8,
            "description": "Family expenses, gifts, and personal commitments"
        }
    ],
    "income_brackets_inr": [
        {
            "bracket": "Entry Level",
            "range": "₹15,000 - ₹30,000",
            "typical_budget": {
                "Food & Dining": 6000,
                "Transportation": 3000,
                "Bills & Utilities": 4000,
                "Shopping": 3000,
                "Healthcare": 2000,
                "Entertainment": 1500,
                "Education": 1000,
                "Investment & Savings": 3000,
                "Family & Personal": 2000
            }
        },
        {
            "bracket": "Mid Level",
            "range": "₹30,000 - ₹75,000",
            "typical_budget": {
                "Food & Dining": 10000,
                "Transportation": 6000,
                "Bills & Utilities": 7000,
                "Shopping": 8000,
                "Healthcare": 4000,
                "Entertainment": 3500,
                "Education": 2500,
                "Investment & Savings": 12000,
                "Family & Personal": 5000
            }
        },
        {
            "bracket": "High Income",
            "range": "₹75,000+",
            "typical_budget": {
                "Food & Dining": 15000,
                "Transportation": 10000,
                "Bills & Utilities": 10000,
                "Shopping": 15000,
                "Healthcare": 8000,
                "Entertainment": 8000,
                "Education": 5000,
                "Investment & Savings": 25000,
                "Family & Personal": 10000
            }
        }
    ],
    "common_indian_merchants": [
        # Food & Dining
        {"name": "Swiggy", "category": "Food & Dining", "type": "Food Delivery"},
        {"name": "Zomato", "category": "Food & Dining", "type": "Food Delivery"},
        {"name": "BigBasket", "category": "Food & Dining", "type": "Groceries"},
        {"name": "Grofers", "category": "Food & Dining", "type": "Groceries"},
        {"name": "DMart", "category": "Food & Dining", "type": "Groceries"},
        {"name": "Reliance Fresh", "category": "Food & Dining", "type": "Groceries"},
        
        # Transportation
        {"name": "Uber", "category": "Transportation", "type": "Ride Sharing"},
        {"name": "Ola", "category": "Transportation", "type": "Ride Sharing"},
        {"name": "Indian Oil", "category": "Transportation", "type": "Fuel"},
        {"name": "Bharat Petroleum", "category": "Transportation", "type": "Fuel"},
        {"name": "HP Petrol Pump", "category": "Transportation", "type": "Fuel"},
        
        # Bills & Utilities
        {"name": "BSES", "category": "Bills & Utilities", "type": "Electricity"},
        {"name": "Airtel", "category": "Bills & Utilities", "type": "Mobile/Internet"},
        {"name": "Jio", "category": "Bills & Utilities", "type": "Mobile/Internet"},
        {"name": "Vi", "category": "Bills & Utilities", "type": "Mobile"},
        {"name": "TATA Sky", "category": "Bills & Utilities", "type": "DTH"},
        
        # Shopping
        {"name": "Amazon", "category": "Shopping", "type": "E-commerce"},
        {"name": "Flipkart", "category": "Shopping", "type": "E-commerce"},
        {"name": "Myntra", "category": "Shopping", "type": "Fashion"},
        {"name": "Ajio", "category": "Shopping", "type": "Fashion"},
        {"name": "Croma", "category": "Shopping", "type": "Electronics"},
        
        # Entertainment
        {"name": "Netflix", "category": "Entertainment", "type": "OTT"},
        {"name": "Disney+ Hotstar", "category": "Entertainment", "type": "OTT"},
        {"name": "Amazon Prime", "category": "Entertainment", "type": "OTT"},
        {"name": "BookMyShow", "category": "Entertainment", "type": "Movies/Events"},
        
        # Healthcare
        {"name": "Apollo Pharmacy", "category": "Healthcare", "type": "Medicine"},
        {"name": "1mg", "category": "Healthcare", "type": "Medicine"},
        {"name": "Practo", "category": "Healthcare", "type": "Consultation"},
        {"name": "Cult.fit", "category": "Healthcare", "type": "Fitness"}
    ],
    "payment_modes_india": [
        {"mode": "UPI", "usage_percentage": 45, "description": "Most popular digital payment method"},
        {"mode": "Debit Card", "usage_percentage": 25, "description": "Traditional card payments"},
        {"mode": "Credit Card", "usage_percentage": 15, "description": "Credit-based purchases"},
        {"mode": "Cash", "usage_percentage": 10, "description": "Physical cash payments"},
        {"mode": "Net Banking", "usage_percentage": 5, "description": "Direct bank transfers"}
    ]
}

# Sample Indian transactions with realistic INR amounts and local merchants
sample_transactions_inr = [
    {"id": 1, "date": "2025-01-28", "description": "Swiggy Order - Biryani", "amount": 450, "category": "Food & Dining", "payment_mode": "UPI"},
    {"id": 2, "date": "2025-01-27", "description": "Uber Ride to Office", "amount": 180, "category": "Transportation", "payment_mode": "UPI"},
    {"id": 3, "date": "2025-01-26", "description": "Amazon - Phone Case", "amount": 599, "category": "Shopping", "payment_mode": "Credit Card"},
    {"id": 4, "date": "2025-01-25", "description": "BSES Electricity Bill", "amount": 2400, "category": "Bills & Utilities", "payment_mode": "Net Banking"},
    {"id": 5, "date": "2025-01-24", "description": "BookMyShow - Movie Tickets", "amount": 360, "category": "Entertainment", "payment_mode": "UPI"},
    {"id": 6, "date": "2025-01-23", "description": "Apollo Pharmacy", "amount": 280, "category": "Healthcare", "payment_mode": "Debit Card"},
    {"id": 7, "date": "2025-01-22", "description": "Indian Oil - Petrol", "amount": 2000, "category": "Transportation", "payment_mode": "Debit Card"},
    {"id": 8, "date": "2025-01-21", "description": "DMart - Groceries", "amount": 1850, "category": "Food & Dining", "payment_mode": "UPI"},
    {"id": 9, "date": "2025-01-20", "description": "Netflix Subscription", "amount": 199, "category": "Entertainment", "payment_mode": "Credit Card"},
    {"id": 10, "date": "2025-01-19", "description": "Airtel Mobile Recharge", "amount": 399, "category": "Bills & Utilities", "payment_mode": "UPI"},
    {"id": 11, "date": "2025-01-18", "description": "Myntra - Shirt", "amount": 1299, "category": "Shopping", "payment_mode": "Credit Card"},
    {"id": 12, "date": "2025-01-17", "description": "Zomato - Lunch", "amount": 320, "category": "Food & Dining", "payment_mode": "UPI"},
    {"id": 13, "date": "2025-01-16", "description": "Ola Auto Ride", "amount": 65, "category": "Transportation", "payment_mode": "UPI"},
    {"id": 14, "date": "2025-01-15", "description": "SIP Investment - Mutual Fund", "amount": 5000, "category": "Investment & Savings", "payment_mode": "Net Banking"},
    {"id": 15, "date": "2025-01-14", "description": "1mg Medicine Order", "amount": 450, "category": "Healthcare", "payment_mode": "UPI"}
]

print("Indian Expense Categories (INR):")
print(json.dumps(indian_expense_data, indent=2))
print("\n" + "="*50 + "\n")

print("Sample Indian Transactions:")
for txn in sample_transactions_inr:
    print(f"₹{txn['amount']} - {txn['description']} ({txn['category']}) - {txn['payment_mode']}")
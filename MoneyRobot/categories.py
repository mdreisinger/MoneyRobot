"""
A dictionary that maps subcategories to main categories.
"""


categories = {
    "Rent": ["Rent"],
    "Utilities": ["Xcel energy", "xfinity", "Parking permit", "Conservice", "T-mobile", "AWS"],
    "Groceries": ["Groceries"],
    "Transportation": ["Vehicle maintenance", "Gas", "Car wash", 
                       "Parking fees", "DMV fees", "Tolls", "Transportation"],
    "Medical Expenses": ["Prescriptions", "Medical Appointments"],
    "Personal Expenses": ["Wardrobe", "Home stuff", "Toiletries"],
    "Entertainment and Hobbies": ["Eating out & drinks", "Entertainment", "Snowboarding", 
                                  "Course fees", "Subscriptions", "Hobbies", "Tools", "AWS",
                                  "Guns", "Ammo", "Gun stuff", "Plant stuff", "Bike stuff"],
    "Pets": ["Dog vet fees", "Cat vet fees", "Dog medication", "Cat medication",
             "Dog food", "Cat food", "Dog supplies", "Cat supplies", 
             "Dog sitting", "Cat sitting", "Dog license", "ESA Fees"],
    "Gifts": ["Gifts"],
    "Investments": ["Investments"],
    "Other": ["Other"],
    "Income": ["Income", "Support from dad", "Income - Other"],
    "Debt" : ["Garmin repayment"],
    "Business" : ["Business"]
}

def print_categories():
    """
    Print the categories and subcategories in a human readable form.
    """
    for key, val in categories.items():
        print(f"{key}:")
        for value in val:
            print(f"\t{value}")

#Finish API (read, update, delete) using basic sql queries
#Update later to do it the "proper" way.
#Create Grapher to Plot expenses for the month
#Create budget object
#Create new table (I'd, month, budget)
#Enforce new transactions to be one of the subcategories.
# Fix/remove tax thing since it doesnt work
# Fix transaction date not working.

#READ
# Get sum from category:
# SELECT sum(transaction_amount) from transactions WHERE transaction_category in ("Guns","Gun Stuff");

#UPDATE
# UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;

# UPDATE
# DELETE FROM transactions WHERE transaction_id=350;

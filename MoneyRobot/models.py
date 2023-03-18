from django.db import models

class expenses(models.Model):

    class expense_categories(models.TextChoices):
        RENT = 'Rent'
        CONSERVICE = 'Conservice'
        XCEL = 'Xcel'
        XFINITY = 'Xfinity'
        TMOBILE = 'T-Mobile'
        PARKING_PERMIT = 'Parking Permit'
        SPOTIFY = 'Spotify'
        GAS = 'Gas'
        VEHICLE_MAINTENANCE = 'Vehicle Maintenance'
        CAR_WASH = 'Car Wash'
        TOLL_FEES = 'Toll Fees'
        PARKING_FEES = 'Parking Fees'
        GROCERIES = 'Groceries'
        HOUSEHOLD_ITEMS = 'Household Items'
        INSURANCE = 'Insurance'
        PRESRIPTIONS = 'Prescriptions'
        MEDICAL_APPOINTMENTS = 'Medical Appointments'
        SAVINGS = 'Savings'
        INVESTMENTS = 'Investments'
        DEBT_PAYMENTS = 'Debt Payments'
        CLOTHES_AND_ACCESSORIES = 'Clothes and Accessories'
        TOILETRIES = 'Toiletries'
        PLANTS_AND_PLANT_SUPPLIES = 'Plants and Plant Supplies'
        EATING_OUT = 'Eating Out'
        DRINKS = 'Drinks'
        ENTERTAINMENT = 'Entertainment'
        SKIING = 'Skiing'
        SUBSCRIPTIONS = 'Subscriptions'
        DOG_VET_FEES = 'Dog Vet Fees'
        DOG_MEDICATION = 'Dog Pet Medication'
        DOG_FOOD = 'Dog Food'
        DOG_SUPPLIES = 'Dog Supplies'
        CAT_VET_FEES = 'Cat Vet Fees'
        CAT_MEDICATION = 'Cat Pet Medication'
        CAT_FOOD = 'Cat Food'
        CAT_SUPPLIES = 'Cat Supplies'
        OTHER = 'Other'

    expense_id = models.BinaryField()
    expense_date = models.DateField()
    expense = models.DecimalField()
    payee = models.TextField()
    expense_category = models.TextChoices(choices=expense_categories.choices)
    items = models.TextField()
    time_modified = models.DateTimeField()
	
    class Meta:  
        db_table = "expenses"
        app_label = ''
	
    def __str__(self):
        return self

class expense_notes(models.Model):
    expense_note_id = models.BinaryField()
    note = models.TextField()
    time_create = models.DateTimeField()
    time_modified = models.DateField()
    expense_id = models.TextField()
	
    class Meta:  
        db_table = "incomes"
        app_label = ''
	
    def __str__(self):
        return self

class income(models.Model):

    class income_categories(models.TextChoices):
        REGULAR_INCOME = 'Regular Income'
        HELP_FROM_DAD = 'Help From Dad'

    income_id = models.BinaryField()
    income_date = models.DateField()
    income = models.DecimalField()
    payor = models.TextField()
    income_category = models.TextChoices(choices=income_categories.choices)
    items = models.TextField()
    time_modified = models.TimeField()
	
    class Meta:  
        db_table = "income"
        app_label = ''
	
    def __str__(self):
        return self


class Patient: #defines the class Patient
    def __init__(self, name: str, bill_amount: float): #init constructor initializes the patient object with name and bill amount
        self._name = name #stores the patient's name as an attribute
        self._bill_amount = bill_amount #stores the patient's bill amount as an attribute

    @property #allows name to be accessed like an attribute
    def name(self): #defines the name method, particularly a getter method 
        return self._name #returns the patient's name

    @property #allows name to be accessed like an attribute
    def name(self, name): #defines the name method, particularly a setter method
        self.name = name #sets the patient's name to the provided value
        
    @property #allows bill_amount to be accessed like an attribute
    def bill_amount(self): #defines the bill_amount method, particularly a getter method
        return self._bill_amount #returns the patient's bill amount

    @property #allows bill_amount to be accessed like an attribute
    def bill_amount(self, bill_amount): #defines the bill_amount method, particularly a setter method
        self.bill_amount = bill_amount #sets the patient's bill amount to the provided value

    @property #allows calculate_bill to be accessed like an attribute
    def calculate_bill(self): #defines the calculate_bill method, which calculates the total bill amount for the patient
        total_bill = self._bill_amount #equates the total bill to the original bill amount since there is no discount for regular patients
        return total_bill #returns the total bill amount for the patient

    @property #allows display_patient_type to be accessed like an attribute
    def display_patient_type(self): #defines the display_patient_type method, which displays the type of patient
        print(f"Patient Type: Regular Patient") #prints the type of patient as "Regular Patient" since this is the base class for all patients

class Senior_Patient(Patient): #defines the class Senior_Patient, which inherits from the Patient class
    def __init__(self, name: str, bill_amount: float): #init constructor initializes the senior patient object with name and bill amount
        super().__init__(name, bill_amount) #calls the parent class constructor to initialize the name and bill amount attributes

    @property #allows calculate_bill to be accessed like an attribute
    def calculate_bill(self): #defines the calculate_bill method, which calculates the total bill amount for the senior patient
        discount = 0.20 #sets the discount for senior patients to 20%
        total_bill = self._bill_amount - (self._bill_amount * discount) #calculates the total bill amount for the senior patient by subtracting the discount from the original bill amount
        return total_bill #returns the total bill amount for the senior patient

    @property #allows display_patient_type to be accessed like an attribute
    def display_patient_type(self): #defines the display_patient_type method, which displays the type of patient
        print(f"Patient Type: Senior Citizen") #prints the type of patient as "Senior Citizen" since this is the subclass for senior patients

class PhilHealth_Patient(Patient): #defines the class PhilHealth_Patient, which inherits from the Patient class
    def __init__(self, name: str, bill_amount: float):  #init constructor initializes the PhilHealth patient object with name and bill amount
        super().__init__(name, bill_amount) #calls the parent class constructor to initialize the name and bill amount attributes

    @property #allows calculate_bill to be accessed like an attribute
    def calculate_bill(self): #defines the calculate_bill method, which calculates the total bill amount for the PhilHealth patient
        discount = 0.15 #sets the discount for PhilHealth patients to 15%
        total_bill = self._bill_amount - (self._bill_amount * discount) #calculates the total bill amount for the PhilHealth patient by subtracting the discount from the original bill amount
        return total_bill #returns the total bill amount for the PhilHealth patient

    @property #allows display_patient_type to be accessed like an attribute
    def display_patient_type(self): #defines the display_patient_type method, which displays the type of patient
        print(f"Patient Type: PhilHealth Member") #prints the type of patient as "PhilHealth Member" since this is the subclass for PhilHealth patients

patient1 = Patient("Juan Dela Cruz", 15000)#creates a Patient object with the name Juan Dela Cruz and a bill amount of 15000
seniorp1 = Senior_Patient("Maria Santos", 15000)#creates a Senior_Patient object with the name Maria Santos and a bill amount of 15000
philhealthp1 = PhilHealth_Patient("Pedro Reyes", 15000)#creates a PhilHealth_Patient object with the name Pedro Reyes and a bill amount of 15000

print("Hospital Billing System") #prints the header for the hospital billing system
print("-----------------------") #prints a divider for the hospital billing system

print(f"Patient Name: {patient1._name}") #prints the name of the regular patient
patient1.display_patient_type #prints the type of patient as "Regular Patient"
print(f"Original Bill: ₱{patient1._bill_amount:,.2f}") #prints the original bill amount for the regular patient
print(f"Final Bill: ₱{patient1.calculate_bill:,.2f}") #prints the final bill amount for the regular patient, which is the same as the original bill amount since there is no discount for regular patients

print(f"\nPatient Name: {seniorp1._name}") #prints the name of the senior patient
seniorp1.display_patient_type #prints the type of patient as "Senior Citizen"
print(f"Original Bill: ₱{seniorp1._bill_amount:,.2f}") #prints the original bill amount for the senior patient
print(f"Final Bill: ₱{seniorp1.calculate_bill:,.2f}") #prints the final bill amount for the senior patient, which is the original bill amount minus the 20% discount for senior patients

print(f"\nPatient Name: {philhealthp1._name}") #prints the name of the PhilHealth patient
philhealthp1.display_patient_type #prints the type of patient as "PhilHealth Member"
print(f"Original Bill: ₱{philhealthp1._bill_amount:,.2f}") #prints the original bill amount for the PhilHealth patient
print(f"Final Bill: ₱{philhealthp1.calculate_bill:,.2f}") #prints the final bill amount for the PhilHealth patient, which is the original bill amount minus the 15% discount for PhilHealth patients
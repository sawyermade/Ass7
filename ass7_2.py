import csv

# Customer Class
class Customer:
    # Constructor with customer info
    def __init__(
        self, cust_id, first_name, last_name, 
        company_name, address, city, state, zipcode
    ):
        # Set customer attributes/variables
        self.cust_id      = cust_id.strip()
        self.first_name   = first_name.strip()
        self.last_name    = last_name.strip()
        self.company_name = company_name.strip()
        self.address      = address.strip()
        self.city         = city.strip()
        self.state        = state.strip()
        self.zip          = zipcode.strip()

    # Gets full name formatted
    def getFullName(self):
        return f'{self.first_name} {self.last_name}'

    # Gets full name and address formatted
    def getFullAddress(self):
        # Get full name formatted
        address = f'{self.getFullName()}\n'
        
        # If customer with company
        if self.company_name:
            address += f'{self.company_name}\n'

        # Rest of address
        address += f'{self.address}\n'
        address += f'{self.city}, {self.state} {self.zip}'

        return address

# Get customers from csv
def get_customers():
    with open('customers.csv') as cf:
        return [Customer(*cust) for cust in list(csv.reader(cf))[1:]]


# Find customer by ID
def find_customer_by_id(customers, cust_id):
    for cust in customers:
        if cust.cust_id == cust_id:
            return cust

# Main function
def main():
    ''' Main is fully implemented with no modification expected '''

    # Program Title
    print("Customer Viewer\n")

    # Get customers data from csv
    customers = get_customers()

    # Display customer info until quit
    cont_flag = True
    while cont_flag:
        # Get customer ID from user
        cust_id = input("Enter customer ID: ").strip()
        print()

        # Get customer info, if customer exists
        customer = find_customer_by_id(customers, cust_id)
        if customer:
            print(f"{customer.getFullAddress()}\n")

        else:
            print("No customer with that ID.\n")
        
        # Ask if user wants to continue
        cont = input("Continue? (y/n): ").lower()
        print()

        # If user wants to quit, end loop
        if cont != "y":
            cont_flag = False

    # See you later :)
    print("Bye!")

# If running file directly, not imported
if __name__ == "__main__":
    main()

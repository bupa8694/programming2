"""
Solutions to exam tasks for module M4
Name:
Code:
"""

# A9
def get_balance(index):
    """This method opens customers.json and returns the field
    'balance' for the person with the given index.
    Leave this method as is.
    Note that '$' and ',' are removed from 'balance' in the jason file"""
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return float(data[index]['balance'].replace('$', '').replace(',', ''))
def get_total_balance():
    """Method that runs get_balance in parallel for each index 0-111.
    The method should return the sum of all balances."""
    pass # remove and write your code here
    
# A10

def get_mean_balances():
    """Method that return the mean balance for male and female customes. Gender 
    is set in the field 'gender' ('male' or 'female')"""
    pass # remove and write your code here
    
# B4
def leapyears(years):
    """A method the returns the leap years of the years in the in argument years"""
    pass # remove and write your code here


def main():
    print('Test of A9 ')
    print(get_total_balance())
    print('Test of A10 ')
    print(get_mean_balances())
    print('Test of B4 ')
    ly=leapyears(range(1900,2101))
    print(ly)
    if ly != None:
        print(len(ly))

if __name__ == "__main__":
    main()
    print('Over and out')

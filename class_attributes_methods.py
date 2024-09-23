'''
Description:
Define a class User who receives 2 attributes in the initializer, a first name, and a last name.
Create a method called full_name, which returns the user's full name
Create 2 users with 2 different names and print their full name
Change the first name of the first object and print the full name again
'''

class User:
    '''Define a class User'''
    
    def __init__(self, first_name, last_name):
        '''Initialize a new User'''
        self.first_name = first_name
        self.last_name = last_name
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    

# Create 2 users with 2 different names
farah = User("Farahnosh", "Yousofi")
print(farah.full_name())
yosuf = User("Husna", "Ahmadi")
print(yosuf.full_name())
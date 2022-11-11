class User:
    """A class to hold user information"""
    
    def __init__(self, first_name, last_name, age, occupation):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        
    def describer_user(self):
        """Describe user profile"""
        print(f"""
              Name: {self.first_name.title()} {self.last_name.title()}
              Age: {self.age}
              Occupation: {self.occupation.title()}
              """)
        
    def name(self):
        """Format full name"""
        print(f"{self.first_name.title()} {self.last_name.title()}")
    
    def greet_user(self):
        """Greet user"""
        name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {name}, welcome! \n------------------------------------")
        
profile1 = User('john', 'kinyua', '28', 'software engineer')
profile2 = User('alice', 'wanjiku', '27', 'education consultant')

print(f"{profile1.first_name.title()} is {profile1.age} years old")
profile1.describer_user()
profile1.greet_user()

profile2.name()
profile2.describer_user()
profile2.greet_user()


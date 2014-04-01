import re
import unittest

def email_validator(email): 
    if "@" in email:
        separating_email = re.split('@', email)
        name = separating_email[0]
        domain = separating_email[1]
        
        if len(domain) >= 3 and len(domain) <= 256 and len(name) >=1 and len(name) <=128:
            print domain, name #checking
            return True 
            
                
email_validator("william@me.com")


#tests


class EmailValidatorTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(email_validator("hello@me.com"))

def main():
    unittest.main()

if __name__ == '__main__':
    main()




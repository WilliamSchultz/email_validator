import re
import unittest

def email_validator(email): 
    if "@" in email:
        separating_email = re.split('@', email)
        name = separating_email[0]
        domain = separating_email[1]
        
        if len(domain) >= 3 and len(domain) <= 256 and len(name) >=1 and len(name) <=128:
            return True
            
                
email_validator("william@me.com")


#tests


class EmailValidatorTests(unittest.TestCase):
    
    def testOne(self):
        self.assertFalse(email_validator("hellome.com")) #testing no @ presence 

    def testTwo(self):
        self.assertTrue(email_validator("hello@me.com")) #testing @ presence
        
    def testThree(self):
        self.assertFalse(email_validator("william@me")) #testing domain length: too short
        
    def testFour(self):
        self.assertFalse(email_validator("william@%s" % ("a" * 257))) #testing domain length: too long
    
    def testFive(self):
        self.assertTrue(email_validator("william@me.com")) #testing domain length: ok
        
    def testSix(self):
      self.assertFalse(email_validator("@me.com")) #testing name length: too short
      
    def testSeven(self):
      self.assertFalse(email_validator("%s@me.com" % ("a" * 129))) #testing name length: too long
  
    def testEight(self):
      self.assertTrue(email_validator("william@me.com")) #testing name length: ok

def main():
    unittest.main()

if __name__ == '__main__':
    main()




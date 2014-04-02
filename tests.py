import unittest
from email_validator import email_validator

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
      
    def testNine(self):
      self.assertFalse(email_validator("william@-me.com")) #domain begins with - 
      
    def testTen(self):
      self.assertFalse(email_validator("william@me.com-")) #domain ends with - 
  
    def testEleven(self):
      self.assertTrue(email_validator("william@me.com")) #domain doesn't begin or end with - 

def main():
    unittest.main()

if __name__ == '__main__':
    main()
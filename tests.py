import unittest
from email_validator import email_validator

class EmailValidatorTests(unittest.TestCase):
    
    def test1(self):
        self.assertFalse(email_validator("hellome.com")) #testing no @ presence 

    def test2(self):
        self.assertTrue(email_validator("hello@me.com")) #testing @ presence
        
    def test3(self):
        self.assertFalse(email_validator("william@me")) #testing domain length: too short
        
    def test4(self):
        self.assertFalse(email_validator("william@%s" % ("a" * 257))) #testing domain length: too long
    
    def test5(self):
        self.assertTrue(email_validator("william@me.com")) #testing domain length: ok
        
    def test6(self):
      self.assertFalse(email_validator("@me.com")) #testing name length: too short
      
    def test7(self):
      self.assertFalse(email_validator("%s@me.com" % ("a" * 129))) #testing name length: too long
  
    def test8(self):
      self.assertTrue(email_validator("william@me.com")) #testing name length: ok
      
    def test9(self):
      self.assertFalse(email_validator("william@-me.com")) #domain begins with - 
      
    def test10(self):
      self.assertFalse(email_validator("william@me.com-")) #domain ends with - 
  
    def test11(self):
      self.assertTrue(email_validator("william@me.com")) #domain doesn't begin or end with - 
     
    def test12(self):
        self.assertTrue(email_validator("williaa-z0-9.\"_-am@me.com")) #testing required characters name
    
    def test13(self):
        self.assertFalse(email_validator("willi&#*?!;^@me.com")) #testing some characters outside of a-z0-9.\"_- for name
    
    def test14(self):
        self.assertTrue(email_validator("william@me.c_-9om")) #testing required characters for domain
        
    def test15(self):
        self.assertFalse(email_validator("william@me.c&#*?!;^om"))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
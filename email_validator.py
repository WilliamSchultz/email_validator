import re

def email_validator(email): 
    if "@" in email:
        separating_email = re.split('@', email)
        name = separating_email[0]
        domain = separating_email[1]
        
        if len(domain) >= 3 and len(domain) <= 256 and len(name) >=1 and len(name) <=128:
            
            if re.search('[-]$', domain) == None and re.search('^[-]', domain) == None:
                return True
            
           
            
            
                
email_validator("william@me.com-")










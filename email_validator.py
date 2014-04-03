import re

def email_validator(email): 
    if "@" in email:
        separating_email = re.split('@', email)
        name = separating_email[0]
        domain = separating_email[1]
        
        if len(domain) >= 3 and len(domain) <= 256 and len(name) >=1 and len(name) <=128: #checking name and domain length
            print name
            if re.search('[-]$', domain) == None and re.search('^[-]', domain) == None: #checking beginning and end of domain doesn't have -
               print name
               name_index = 0 #checking name characters
               for i in name:
                   if re.search('[a-zA-Z0-9."_-]', i) != None: 
                       name_index += 1
                       if len(name) == name_index:
                           domain_index = 0 #checking domain characters
                           for i in domain:
                               if re.search('[a-zA-Z0-9._-]', i) != None: 
                                   domain_index += 1
                                   if len(domain) == domain_index:
                                       return True
                           
            
           
            
            
                
email_validator("willam@me.com")










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
               
               if name.find('"') != -1: #presence of double qoutes
                 if name.count('"') % 2 == 0: #double quotes have to exist in pairs
                     
                     quotesTest = re.findall(r'"([^"]*)"', name) #find quotes, make sure they are in pairs, put these pairs in an array
                     for i in range(len(quotesTest)): 
                         if re.search('[!,:a-zA-Z0-9."_-]', quotesTest[i]) != None: #check each arrary object
                             
                             new_name = re.sub(r'"([^"]*)"', "a", name) #remove " " objects so the rest of the string can be checked
                             
                             name_index = 0 #checking name characters
                             for i in new_name:
                                 if re.search('[a-zA-Z0-9."_-]', i) != None: 
                                     name_index += 1
                                     if len(new_name) == name_index:
                                         domain_index = 0 #checking domain characters
                                         for i in domain:
                                             if re.search('[a-zA-Z0-9._-]', i) != None: 
                                                 domain_index += 1
                                                 if len(domain) == domain_index:
                                                     if name.find("..") == -1: #checking for two .. in a row
                                                         return True
                       
             
               else: # no presence of double quotes
                    
                    name_index = 0 #checking name characters
                    for i in name:
                        if re.search('[a-zA-Z0-9._-]', i) != None: 
                            name_index += 1
                            if len(name) == name_index:
                                domain_index = 0 #checking domain characters
                                for i in domain:
                                    if re.search('[a-zA-Z0-9._-]', i) != None: 
                                        domain_index += 1
                                        if len(domain) == domain_index:
                                            if name.find("..") == -1: #checking for two .. in a row
                                                return True
           









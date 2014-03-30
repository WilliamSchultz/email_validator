def email_validator(email): 
    if "@" in email:
        at_location = email.find("@")
        domain_with_at = email[at_location:]
        
        name = email[:at_location]
        domain = domain_with_at[1:]
        print name, domain #checking
        
        if len(domain) >= 3 and len(domain) <= 256 and len(name) >=1 and len(name) <=128:
            print domain, name #checking
            
        
        
email_validator("william@me.com")


class Details:
      def __init__(self,site,password):            
        self.site = site
        self.password = password

contact_passwords = []

def save_site(self):
    Details.user_passwords.append(self)

def delete_site(self):
    Details.user_passwords.remove(self)

@classmethod
def diplay_site(cls):
    return cls.user_passwords

@classmethod
def find_by_site(cls,page):
    for pwd in cls.user_passwords:
      if pwd.site == page:
        return pwd

@classmethod
def site_exists(cls,page):
    for pwd in cls.user_passwords:
      if pwd.site == page:
        return pwd
    return False
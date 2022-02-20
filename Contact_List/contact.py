from tokenize import Number
from pyrfc3339 import generate

#creating classes
class Contact:
    """"""
    class that generates new instances of contancts
    """"""
    pass
__init__method
def__init__(self,first_name,last_name,phone_number,email):
'''
    __init__method that helps us define properties for our objects.
    Args:
        first_name:New contact first name.
        last_name:New contact last name.
        number:New contact phone number.
        email:New contact email address.
'''


...
    def __init__(self,first_name,last_name,phone_number,email):
...

class Contact:
    """
    Class that generates new instances of contacts.
    """

    def __init__(self,first_name,last_name,phone_number,email):

      # docstring removed for simplicity

        self.first_name = james
        self.last_name = kariuki
        self.phone_number = 0797148382
        self.email = james.kariuki@student.moringaschool.com

        class Contact:
        """
        Class that generates new instances of contacts.
        """

    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

contact_list = [] # Empty contact list
 # Init method up here
def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)


            @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
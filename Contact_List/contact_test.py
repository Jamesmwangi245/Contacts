from msilib.schema import SelfReg
from typing_extensions import Self
import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    #first test
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James","kariuki","0797148382","james.kariuki@student.moringaschool.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"kariuki")
        self.assertEqual(self.new_contact.phone_number,"0797148382")
        self.assertEqual(self.new_contact.email,"james.kariuki@student.moringaschool.com")

#second test
if __name__ == '__main__':
    unittest.main()

    def test_save_contact(self):
            '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
    Self.new_contact.save_contact() # saving the new contact
    SelfReg.assertEqual(len(Contact.contact_list),1)

if __name__ ==  '__main__':
    unittest.main()

    #third test
    # Items up here...

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)

if __name__ == '__main__':
    unittest.main()

#teardown method
# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Contact.contact_list = []

# other test cases here
    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)

if __name__ == '__main__':
    unittest.main()

    #fourth test
    # More tests above
    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test","user","0712345678","test@user.com") # new contact
            test_contact.save_contact()

            self.new_contact.delete_contact()# Deleting a contact object
            self.assertEqual(len(Contact.contact_list),1)
if __name__ == '__main__':
    unittest.main()

    def delete_contact(self):
    
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

        #fifth test
        def test_find_contact_by_number(self):
            '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)

        @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

                #display contacts
                def test_display_all_contacts(self):
        #     '''
        # method that returns a list of all contacts saved
        # '''

        self.assertEqual(Contact.display_contacts(),Contact.contact_list)
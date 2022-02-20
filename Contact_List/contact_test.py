from msilib.schema import SelfReg
from typing_extensions import Self
import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):
     def tearDown(self):
          Contact.user_info = []

def setUp(self):
    '''
    runs before every test occurs
    '''
    self.new_user = Contact('James','Kariuki','0712345678','+254KK')

def test_init(self):
    '''
    test case to test if object properly initialized
    '''
    self.assertEqual(self.new_user.fname,'James')
    self.assertEqual(self.new_user.sname,'Kariuki')
    self.assertEqual(self.new_user.user_name,'user123')
    self.assertEqual(self.new_user.password,'+254KK')

def test_new_acc(self):
    '''
    test to see if an account is added
    '''
    self.new_user.new_acc()
    test_user = Contact('James','Kariuki','user123','+254KK')
    test_user.new_acc()
    self.assertEqual(len(Contact.user_info),2)

def test_del_acc(self):
    '''
    test delete account function
    '''
    self.new_user.new_acc('James','Kariuki','user123','+254KK')
    test_user = Contact()
    test_user.new_acc()
    self.new_user.del_acc()
    self.assertEqual(len(Contact.user_info),1)

def test_find_by_username(self):
    '''
    test find user function
    '''
    self.new_user.new_acc()
    test_user = Contact('James','Kariuki','user123','+254KK')
    test_user.new_acc()
    find_user = Contact.find_by_username('user123')
    self.assertEqual(find_user.username, test_user.username)

def test_user_exists(self):
    '''
    test user exists function
    '''
    self.new_user.new_acc()
    test_user = Contact('James','Kariuki','user123','+254KK')
    test_user.new_acc()
    user_exists = Contact.user_exists('user123')
    self.assertTrue(user_exists)

def test_display_users(self):
    '''
    test display function
    '''
    self.assertEqual(Contact.display_users(),Contact.user_info)


if __name__ == '__main__':
  unittest.main()

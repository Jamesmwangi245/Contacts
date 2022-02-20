from Details import Details
import unittest


class Details(unittest.TestCase):
  def tearDown(self):
    '''
    clears user passwords before every test
    '''
    Details.user_passwords = []

  def setUp(self):
    '''
    creates new instance of passwords class before every test
    '''
    self.new_password = Details('Tang','12345')

  def test_init(self):
    '''
    tests whether data entered can be returned
    '''
    self.assertEqual(self.new_password.site,'Tang')
    self.assertEqual(self.new_password.password,'12345')
  
  def test_save_site(self):
    '''
    check whether value is added to passwords list
    '''
    self.new_password.save_site()
    self.assertEqual(len(Details.user_passwords),1)

  def test_save_multiple(self):
    '''
    check addition of many passwords
    '''
    self.new_password.save_site()
    test_pass = Details('Tang','12345')
    test_pass.save_site()
    self.assertEqual(len(Details.user_passwords),2)

  def test_delete_site(self):
    '''
    check if password can be deleted
    '''
    self.new_password.save_site()
    test_pass = Details('Tang','12345')
    test_pass.save_site()
    self.new_password.delete_site()
    self.assertEqual(len(Details.user_passwords),1)

  def test_display_site(self):
    self.assertEqual(Details.diplay_site(),Details.user_passwords)

  def test_find_by_site(self):
    '''
    test to check if saved site pwd can be searched
    '''
    self.new_password.save_site()
    test_pass = Details('Tang','12345')
    test_pass.save_site()
    site_exists = Details.site_exists('Tang')
    self.assertTrue(site_exists)


if __name__ == '__main__':
  unittest.main()
  
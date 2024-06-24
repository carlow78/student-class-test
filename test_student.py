import unittest
from student import Student

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        print("test_full_name")
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        student = Student("John", "Doe")
        student.alert_santa()
        self.assertTrue(student.naughty_list)

    
    def test_email(self):
        print("test_email")
        student = Student("John", "Doe")
        self.assertEqual(student.email, "john.doe@email.com")

if __name__ == '__main__':
    unittest.main()
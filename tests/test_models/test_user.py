#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = client.Client


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.client_f = inspect.getmembers(Client, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestClient(unittest.TestCase):
    """Test the Client class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        client = Client()
        self.assertIsInstance(client, BaseModel)
        self.assertTrue(hasattr(client, "id"))
        self.assertTrue(hasattr(client, "created_at"))
        self.assertTrue(hasattr(client, "updated_at"))

    def test_email_attr(self):
        """Test that client has attr email, and it's an empty string"""
        client = Client()
        self.assertTrue(hasattr(client, "email"))
        if models.storage_t == 'db':
            self.assertEqual(client.email, None)
        else:
            self.assertEqual(client.email, "")

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        client = Client()
        self.assertTrue(hasattr(client, "password"))
        if models.storage_t == 'db':
            self.assertEqual(client.password, None)
        else:
            self.assertEqual(client.password, "")

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        client = Client()
        self.assertTrue(hasattr(client, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(client.first_name, None)
        else:
            self.assertEqual(client.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        client = Client()
        self.assertTrue(hasattr(client, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(client.last_name, None)
        else:
            self.assertEqual(client.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Client()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Client()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Client")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        client = Client()
        string = "[Client] ({}) {}".format(client.id, client.__dict__)
        self.assertEqual(string, str(client))

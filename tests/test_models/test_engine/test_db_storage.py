#!/usr/bin/python3
"""
Contains the TestdbStorage
"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class Test_dbstorage(unittest.TestCase):
    """Test to check"""

    def test_pep8_db_storage(self):
        """Test PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors found.")

    def test_db_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNotNone(file_storage.__doc__, "fix a docstring")

if __name__ == "__main__":
    unittest.main()

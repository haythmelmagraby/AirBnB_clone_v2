import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUp(cls):
        try:
            os.rename("my_file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownMethod(cls):
        try:
            os.rename("tmp", "my_file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("my_file.json")
        except IOError:
            pass

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as my_file:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", my_file.getvalue())
        with patch("sys.stdout", new=StringIO()) as my_file:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", my_file.getvalue())

    def test_kargs(self):
        with patch("sys.stdout", new=StringIO()) as my_file:
            call = (f'create Place city_id="0022" name="My name" number_rooms=2
                    latitude=55.55 longitude=66.66')
            self.HBNB.onecmd(call)
            pl = my_file.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as my_file:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0022'", output)
            self.assertIn("'name': 'My name'", output)
            self.assertIn("'number_rooms': 2", output)
            self.assertIn("'latitude': 55.55", output)
            self.assertIn("'longitude': 66.66", output)


if __name__ == "__main__":
    unittest.main()

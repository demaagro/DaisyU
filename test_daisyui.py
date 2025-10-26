# test_daisyui.py
"""
Tests for DaisyUI module.
"""

import unittest
from daisyui import DaisyUI

class TestDaisyUI(unittest.TestCase):
    """Test cases for DaisyUI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DaisyUI()
        self.assertIsInstance(instance, DaisyUI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DaisyUI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

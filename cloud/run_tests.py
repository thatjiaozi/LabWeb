import sys
sys.path.append('./tests')

import unittest

# First make sure we configure correctly the database

import db_config_for_tests

# Import all the test cases here in order to run them all

# Dummy test case just to ilustrate how to import tests
import dummy_test
suite = unittest.TestLoader().loadTestsFromModule(dummy_test)
unittest.TextTestRunner(verbosity=2).run(suite)


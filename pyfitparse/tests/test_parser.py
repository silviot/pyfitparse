import unittest
import os


HERE = os.path.dirname(__file__)
TESTFILE = os.path.join(HERE, 'data', 'Activity.fit')
TESTDATA = open(TESTFILE).read()

class TestParser(unittest.TestCase):
    def test_basic(self):
        from pyfitparse.parser import parse_fit_data
        result = parse_fit_data(TESTDATA)
        #Dummy test
        assert len(result.records) == 0

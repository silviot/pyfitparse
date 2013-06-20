#!/usr/bin/env python
from activityextractor import extract_from_fit
from StringIO import StringIO
import datetime
import os
import unittest


FILENAME = os.path.join(os.path.dirname(__file__), 'data', "unico_che_ho.FIT")
DATA = open(FILENAME, 'rb').read()


class FitFileTestCase(unittest.TestCase):
    def test_fitfile_extractor(self):
        out = extract_from_fit(StringIO(DATA))
        assert out == {
            'activity_type': 'running',
            'duration': 2007.162,
            'distance': 2880.21,
            'calories': 159,
            'start_time': datetime.datetime(2013, 6, 6, 11, 28, 15),
        }


if __name__ == '__main__':
    unittest.main()

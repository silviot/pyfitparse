#!/usr/bin/env python
import os
import unittest

from activityextractor import extract_from_fit


def filecontents(*filename):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'data',
        os.path.join(*filename),
    )


class FitFileTestCase(unittest.TestCase):
    def test_fitfile_extractor(self):
        out = extract_from_fit(filecontents("unico_che_ho.FIT"))

        self.assertEquals(out[0]['total_calories']['units'], 'kcal')
        self.assertEquals(out[0]['total_calories']['data'], 159)


if __name__ == '__main__':
    unittest.main()

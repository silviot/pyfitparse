#!/usr/bin/env python

import os
import sys
import unittest

PROJECT_PATH = os.path.realpath(os.path.join(sys.path[0], '..'))
sys.path.append(PROJECT_PATH)
from activityextractor import ActivityExtractor


def filecontents(*filename):
	return os.path.join(
		os.path.dirname(os.path.realpath(__file__)),
		'data',
		os.path.join(*filename),
	)


class FitFileTestCase(unittest.TestCase):
	def test_fitfile_extractor(self):
		fit = ActivityExtractor()
		out = fit.extractFIT(filecontents("unico_che_ho.FIT"))

		self.assertEquals(out[0]['total_calories']['units'], 'kcal')
		self.assertEquals(out[0]['total_calories']['data'], 159)


if __name__ == '__main__':
    unittest.main()

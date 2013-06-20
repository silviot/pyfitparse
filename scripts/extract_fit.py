#!/usr/bin/env python

import os
import sys

PROJECT_PATH = os.path.realpath(os.path.join(sys.path[0], '..'))
sys.path.append(PROJECT_PATH)
from activityextractor import ActivityExtractor

fit = ActivityExtractor()
out = fit.extractFIT("../tests/data/unico_che_ho.FIT")
for v in out:
	print v

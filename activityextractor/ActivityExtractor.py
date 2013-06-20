#!/usr/bin/env python

import os
import sys

PROJECT_PATH = os.path.realpath(os.path.join(sys.path[0], '..'))
sys.path.append(PROJECT_PATH)
from fitparse import Activity


class ActivityExtractor(object):

	# private members
	_interesting_fields_names = ['timestamp', 'start_time', 'start_position_lat', 'start_position_long', 'total_elapsed_time', 'total_timer_time', 'total_distance', 'total_calories', 'avg_speed', 'sport', 'sub_sport']
	_file_handler = None

	def extractFIT(self, file_handler):
		self._file_handler = file_handler
		
		activity = Activity(self._file_handler)
		activity.parse()

		# Records, in an activity file that represent actual data points in your workout
		records = activity.get_records_by_type('session')

		out = []

		for record in records:
			d = {}
	
			# get the list of valid fields on this record
			valid_field_names = record.get_valid_field_names()

			# Examine only >>> event='session' and trigger='activity_end' <<<
			if not ('trigger' in valid_field_names) and (record.get_data('trigger') == 'activity_end'):
				continue    
	
			for field_name in list(set(self._interesting_fields_names) & set(valid_field_names)):
				# Get the data and units for the field
				field_data = record.get_data(field_name)
				field_units = record.get_units(field_name)

				if not field_units:
					field_units = None

				d[field_name] = {'data': field_data, 'units': field_units}
    
			out.append(d)

		return out

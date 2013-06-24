from fitparse import Activity
from pytz import UTC


INTERESTING_FIELD_NAMES = [
    'timestamp',
    'start_time',
    'start_position_lat',
    'start_position_long',
    'total_elapsed_time',
    'total_timer_time',
    'total_distance',
    'total_calories',
    'avg_speed',
    'sport',
    'sub_sport'
]


def extract_from_fit_raw(file_handler):
    """Extract records from a FIT file handler.
       Filters interesting records from each activity and
       returns an activity iterator.
    """
    activity = Activity(file_handler)
    activity.parse()

    # Records, in an activity file that represent actual data points in your workout
    records = activity.get_records_by_type('session')

    for record in records:
        d = {}
        # get the list of valid fields on this record
        valid_field_names = record.get_valid_field_names()

        # Examine only >>> event='session' and trigger='activity_end' <<<
        if ('trigger' not in valid_field_names) and (record.get_data('trigger') == 'activity_end'):
            continue

        for field_name in list(set(INTERESTING_FIELD_NAMES) & set(valid_field_names)):
            # Get the data and units for the field
            field_data = record.get_data(field_name)
            field_units = record.get_units(field_name)

            d[field_name] = {'data': field_data}
            if field_units:
                d[field_name]['units'] = field_units

        yield d


def extract_from_fit(fh):
    "Extract activities from fit file in a format directly usable"
    for activity in extract_from_fit_raw(fh):
        converted = {}

        converted['activity_type'] = activity['sport']['data']

        assert activity['total_elapsed_time']['units'] == 's'
        converted['duration'] = activity['total_elapsed_time']['data']

        assert activity['total_distance']['units'] == 'm'
        converted['distance'] = activity['total_distance']['data']

        assert activity['total_calories']['units'] == 'kcal'
        converted['calories'] = activity['total_calories']['data']

        # TODO this requires more investigation:
        # The fit format uses UTC timestamp from 1/1/1990 epoch but
        # we need to be sure it makes it to us without being misinterpreted

        # For now we assume the value is correct and just needs a UTC tzinfo
        converted['start_time'] = UTC.localize(activity['timestamp']['data'])

        yield converted

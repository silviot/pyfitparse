from collections import namedtuple

Field = namedtuple('Field', ('name', 'type', 'units', 'scale', 'offset'))

FitFile = namedtuple('FitFile', ('records'))

from setuptools import setup
import os


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='pyfitparse',
    version='0.1',
    description='pyfitparse',
    long_description=README,
    packages=['fitparse'],
    install_requires=['pytz'],
    include_package_data=True,
)

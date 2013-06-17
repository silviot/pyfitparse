import os
from setuptools import setup
from distutils.core import Command


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='pyfitparse',
    version='0.1',
    description='pyfitparse',
    long_description=README,
    cmdclass = {'test': PyTest},
)

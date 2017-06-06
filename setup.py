from distutils.core import setup

setup(
    name='fndetector',
    version='1.0',
    packages=['fndetector', 'fndetector.detectors', 'fndetector.tests', 'fndetector.resources'],
    url='',
    license='MIT',
    author='Michał Zezyk',
    author_email='zezyk.michal@gmail.com',
    description='', requires=['urlparse', 'numpy', 'python-twitter', 'urllib']
)
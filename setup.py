from distutils.core import setup

setup(
    name='fndetector',
    version='1.0',
    packages=['fndetector', 'fndetector.detectors'],
    package_data = {
    	"fndetector.resources": [
    		"domain_database.csv",
    	],
    },
    include_package_data = True,
    url='',
    license='MIT',
    author='Michał Zezyk',
    author_email='zezyk.michal@gmail.com',
    description='',
    zip_safe=False
)
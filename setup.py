from setuptools import (
    find_packages,
    setup
)

INSTALL_REQUIRES = (
    'requests',
    'pandas',
    'reverse_geocoder',
    'cached_property'
)

setup(
    name='fixyourstreet_data',
    version='0.0.1',
    python_requires='>=3.6',
    author='Robert Lucey',
    url='https://github.com/RobertLucey/fixyourstreet-data',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'update_fixyourstreet_data = fixyourstreet_data.bin.update_data:main',
        ]
    }
)
